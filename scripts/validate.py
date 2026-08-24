#!/usr/bin/env python3
"""Validate the canonical catalog and its README presentation."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.yaml"
README = ROOT / "README.md"

REQUIRED_FIELDS = {
    "id",
    "title",
    "authors",
    "year",
    "venue",
    "status",
    "paper_type",
    "urls",
    "taxonomy",
    "reading",
    "artifacts",
    "curation",
}
STATUSES = {"accepted", "peer-reviewed", "preprint", "technical-report"}
PAPER_TYPES = {
    "benchmark",
    "dataset",
    "empirical-study",
    "method",
    "perspective",
    "sok",
    "survey",
    "system",
}
SECURITY_ROLES = {"defensive", "dual-use", "offensive"}
PRIORITIES = {"emerging", "essential", "recommended"}
PAPER_SECTIONS = {
    "## Surveys, SoKs, and Perspectives",
    "## Benchmark Papers",
    "### Vulnerability Discovery and Analysis",
    "### Program Understanding and Reverse Engineering",
    "### AI for Cryptography and Cryptanalysis",
    "### Exploitation and Offensive Security",
    "### Remediation and Secure Software Engineering",
    "### Malware and Unwanted Software",
    "### Network, Host, and Infrastructure Defense",
    "### Social Engineering, Identity, and Abuse",
    "### Threat Intelligence, SOC, and Incident Response",
    "## Defending Against AI-Enabled Cyber Attacks",
}
TITLE_LINE = re.compile(r"^- \*\*(.+)\*\*  $")
YEAR = re.compile(r"\b(19|20)\d{2}\b")


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"duplicate key: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_url(errors: list[str], paper_id: str, name: str, value: object) -> None:
    if value is None:
        return
    if not isinstance(value, str):
        fail(errors, f"{paper_id}: urls.{name} must be a string or null")
        return
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(errors, f"{paper_id}: urls.{name} is not a valid HTTP(S) URL")


def read_catalog(errors: list[str]) -> list[dict]:
    source_lines = CATALOG.read_text(encoding="utf-8").splitlines()
    inline_fields = {
        "authors": ("[", "]"),
        "contribution": ('"', '"'),
        "why_read": ('"', '"'),
        "limitations": ("[", "]"),
        "notes": ('"', '"'),
    }
    for line_number, line in enumerate(source_lines, start=1):
        match = re.match(r"^\s+(authors|contribution|why_read|limitations|notes):\s*(.*)$", line)
        if not match:
            continue
        field, value = match.groups()
        opening, closing = inline_fields[field]
        if not value.startswith(opening) or not value.endswith(closing):
            fail(errors, f"data/papers.yaml:{line_number}: {field} must stay on one physical line")

    try:
        document = yaml.load("\n".join(source_lines), Loader=UniqueKeyLoader)
    except (OSError, yaml.YAMLError) as exc:
        fail(errors, f"cannot read {CATALOG.relative_to(ROOT)}: {exc}")
        return []

    if not isinstance(document, dict) or set(document) != {"papers"}:
        fail(errors, "data/papers.yaml must contain exactly one top-level key: papers")
        return []
    papers = document["papers"]
    if not isinstance(papers, list) or not papers:
        fail(errors, "data/papers.yaml: papers must be a non-empty list")
        return []
    return papers


def validate_catalog(papers: list[dict], errors: list[str]) -> None:
    ids: Counter[str] = Counter()
    titles: Counter[str] = Counter()

    for index, paper in enumerate(papers, start=1):
        if not isinstance(paper, dict):
            fail(errors, f"paper #{index} must be a mapping")
            continue
        paper_id = paper.get("id", f"paper #{index}")
        missing = REQUIRED_FIELDS - set(paper)
        if missing:
            fail(errors, f"{paper_id}: missing fields: {', '.join(sorted(missing))}")

        if isinstance(paper.get("id"), str):
            ids[paper["id"]] += 1
        else:
            fail(errors, f"paper #{index}: id must be a string")
        if isinstance(paper.get("title"), str):
            titles[paper["title"]] += 1
        else:
            fail(errors, f"{paper_id}: title must be a string")

        authors = paper.get("authors")
        if not isinstance(authors, list) or not authors or not all(
            isinstance(author, str) and author.strip() for author in authors
        ):
            fail(errors, f"{paper_id}: authors must be a non-empty list of strings")
        if not isinstance(paper.get("year"), int):
            fail(errors, f"{paper_id}: year must be an integer")
        if paper.get("status") not in STATUSES:
            fail(errors, f"{paper_id}: unsupported status {paper.get('status')!r}")
        if paper.get("paper_type") not in PAPER_TYPES:
            fail(errors, f"{paper_id}: unsupported paper_type {paper.get('paper_type')!r}")

        urls = paper.get("urls")
        if not isinstance(urls, dict) or not urls:
            fail(errors, f"{paper_id}: urls must be a non-empty mapping")
        else:
            for name, value in urls.items():
                validate_url(errors, str(paper_id), str(name), value)

        taxonomy = paper.get("taxonomy")
        if not isinstance(taxonomy, dict):
            fail(errors, f"{paper_id}: taxonomy must be a mapping")
        elif taxonomy.get("security_role") not in SECURITY_ROLES:
            fail(errors, f"{paper_id}: unsupported taxonomy.security_role")

        reading = paper.get("reading")
        if not isinstance(reading, dict):
            fail(errors, f"{paper_id}: reading must be a mapping")
        else:
            if reading.get("priority") not in PRIORITIES:
                fail(errors, f"{paper_id}: unsupported reading.priority")
            for field in ("contribution", "why_read", "limitations"):
                if field not in reading:
                    fail(errors, f"{paper_id}: reading.{field} is required")

    for duplicate in sorted(key for key, count in ids.items() if count > 1):
        fail(errors, f"duplicate paper id: {duplicate}")
    for duplicate in sorted(key for key, count in titles.items() if count > 1):
        fail(errors, f"duplicate paper title: {duplicate}")


def section_ranges(lines: list[str], errors: list[str]) -> list[tuple[str, int, int]]:
    ranges = []
    headings = [(i, line) for i, line in enumerate(lines) if line.startswith("##")]
    for heading in PAPER_SECTIONS:
        starts = [i for i, line in headings if line == heading]
        if len(starts) != 1:
            fail(errors, f"README: expected one heading {heading!r}, found {len(starts)}")
            continue
        start = starts[0]
        level = len(heading) - len(heading.lstrip("#"))
        end = len(lines)
        for candidate, line in headings:
            candidate_level = len(line) - len(line.lstrip("#"))
            if candidate > start and candidate_level <= level:
                end = candidate
                break
        ranges.append((heading, start + 1, end))
    return ranges


def validate_readme(papers: list[dict], errors: list[str]) -> int:
    lines = README.read_text(encoding="utf-8").splitlines(keepends=True)
    plain_lines = [line.rstrip("\n") for line in lines]
    ranges = section_ranges(plain_lines, errors)
    entries: list[tuple[str, int, str]] = []
    papers_by_title = {
        paper["title"]: paper for paper in papers if isinstance(paper.get("title"), str)
    }

    for heading, start, end in ranges:
        section_entries: list[tuple[int, str, int]] = []
        for i in range(start, end):
            match = TITLE_LINE.match(plain_lines[i])
            if not match:
                continue
            title = match.group(1)
            line_number = i + 1
            if i + 4 >= len(plain_lines):
                fail(errors, f"README:{line_number}: incomplete five-line entry")
                continue
            author, links, description, label = plain_lines[i + 1 : i + 5]
            for offset, value in enumerate((author, links, description, label), start=1):
                if not value.startswith("  ") or not value.endswith("  ") and offset < 4:
                    fail(errors, f"README:{line_number + offset}: malformed entry line")
            if not links.lstrip().startswith("["):
                fail(errors, f"README:{line_number + 2}: links line must begin with a link")
            if not label.startswith("  **"):
                fail(errors, f"README:{line_number + 4}: label line must begin with bold text")
            year_match = YEAR.search(author)
            if not year_match:
                fail(errors, f"README:{line_number + 1}: author/venue line has no year")
                continue
            year = int(year_match.group())
            entries.append((title, line_number, heading))
            section_entries.append((year, title, line_number))

            paper = papers_by_title.get(title)
            if paper and isinstance(paper.get("authors"), list) and paper["authors"]:
                authors = paper["authors"]
                if len(authors) == 1:
                    display_authors = authors[0]
                elif len(authors) == 2:
                    display_authors = f"{authors[0]} and {authors[1]}"
                elif len(authors) == 3:
                    display_authors = f"{authors[0]}, {authors[1]}, and {authors[2]}"
                else:
                    display_authors = f"{authors[0]} et al."
                punctuation = "" if len(authors) >= 4 else "."
                if not author.startswith(f"  {display_authors}{punctuation} *"):
                    fail(errors, f"README:{line_number + 1}: author display does not match YAML")

        expected = sorted(section_entries, key=lambda item: (-item[0], item[1].casefold()))
        if section_entries != expected:
            for actual, wanted in zip(section_entries, expected):
                if actual != wanted:
                    fail(
                        errors,
                        f"README:{actual[2]}: {heading} is not newest-first/alphabetical; "
                        f"expected {wanted[1]!r} here",
                    )
                    break

    catalog_titles = {paper["title"] for paper in papers if isinstance(paper.get("title"), str)}
    display_counts = Counter(title for title, _, _ in entries)
    for title in sorted(catalog_titles):
        count = display_counts[title]
        if count not in {1, 2}:
            fail(errors, f"README: catalog title must appear once or twice, found {count}: {title}")
    for title in sorted(set(display_counts) - catalog_titles):
        fail(errors, f"README: entry has no canonical YAML record: {title}")

    return len(entries)


def main() -> int:
    errors: list[str] = []
    papers = read_catalog(errors)
    if papers:
        validate_catalog(papers, errors)
        entry_count = validate_readme(papers, errors)
    else:
        entry_count = 0

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(papers)} papers and {entry_count} README entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
