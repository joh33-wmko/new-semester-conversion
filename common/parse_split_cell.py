#!/usr/bin/env python3

"""
Utility to expand slash-delimited cell values in a single row of CSV data
Input: single row of cell values
Checks cells that contain "/" for highest split pattern
    and only cells matching the highest slash count are treated as split cells
Low slash count cells are treated as non-split plain text
Non-split cells are replicated in each generated row
Outliers split cell row is returned as entered with "error" key
Results are stored in a dict and returned
"""

from __future__ import annotations
from pprint import pprint
from typing import Any, Dict, List, Sequence


def _count_slashes(value: Any) -> int:
    """ Returns: slash count for string-like values; 0 for non-strings """
    if value is None:
        return 0
    text = str(value)
    return text.count("/")


def _build_result(key: str, rows: List[List[str]]) -> Dict[str, List[List[str]]]:
    result = {key: rows}
    pprint(result)
    return result


def parse_split_row(row_values: Sequence[Any]) -> Dict[str, List[List[str]]]:
    """ Parse a single row that may contain slash-delimited multi-value cells
    Args: row_values: Sequence of values from one source row
    Returns: Dict with key "rows" for valid input or "error" for malformed input
    Example: {"rows": [[...], [...], ...]} or
             {"error": [[...], [...], ...]} for outlier split cell row
    """
    if not isinstance(row_values, (list, tuple)):
        raise TypeError("row_values must be a list or tuple")

    str_values = ["" if value is None else str(value) for value in row_values]
    slash_counts = [_count_slashes(value) for value in str_values]
    split_indexes = [idx for idx, count in enumerate(slash_counts) if count > 0]

    if not split_indexes:
        return _build_result("rows", [str_values])

    highest_slash_count = max(slash_counts[idx] for idx in split_indexes)
    split_candidate_indexes = [
        idx for idx in split_indexes if slash_counts[idx] == highest_slash_count
    ]
    split_row_count = highest_slash_count + 1

    split_values_by_col: Dict[int, List[str]] = {}
    for idx in split_candidate_indexes:
        parts = [part.strip() for part in str_values[idx].split("/")]
        if len(parts) != split_row_count:
            return _build_result(
                "error", [str_values[:] for _ in range(split_row_count)]
            )
        split_values_by_col[idx] = parts

    expanded_rows: List[List[str]] = []
    for split_idx in range(split_row_count):
        new_row: List[str] = []
        for col_idx, original_value in enumerate(str_values):
            if col_idx in split_values_by_col:
                new_row.append(split_values_by_col[col_idx][split_idx])
            else:
                new_row.append(original_value)
        expanded_rows.append(new_row)

    return _build_result("rows", expanded_rows)

# direct execution testing only
# def main() -> None:
#     """Main function for testing parse_split_row."""
#     sample_row = ["2026-08-01", "2026-08-31", "SA", "343", "8/8, 9/26, 12/16, 01/04/27"]
#     parse_split_row(sample_row)

# if __name__ == "__main__":
#     main()