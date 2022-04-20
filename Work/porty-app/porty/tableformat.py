class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print("<tr>", end='')
        for h in headers:
            print(f"<th>{h}</th>", end='')
        print("</tr>", end='')
        print()

    def row(self, rowdata):
        print("<tr>", end='')
        for d in rowdata:
            print(f"<td>{d}</td>", end='')
        print("</tr>", end='')
        print()


class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')
    return formatter


def print_table(lst, colnames, formatter):
    formatter.headings(colnames)
    for obj in lst:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)
