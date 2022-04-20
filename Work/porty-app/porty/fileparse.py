# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(csvlines, *, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    """
    Parse a csv file into a list of dictionary (records)
    """
    if select is not None and has_headers is False:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(csvlines, delimiter=delimiter)

    headers = next(rows) if has_headers else []
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []
    records = []
    for no, row in enumerate(rows, 1):
        if not row:
            continue
        try:
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]

            record = dict(zip(headers, row)) if has_headers else tuple(row)
            records.append(record)
        except ValueError as e:
            if silence_errors is False:
                log.warning(f"Row {no}: Couldn't convert {row}")
                log.debug(f"Row {no}: Reason {e}")

    return records
