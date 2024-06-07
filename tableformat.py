import sys
from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, row_data):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def __init__(self, column_width=10):
        super().__init__()
        self.column_width = column_width

    def headings(self, headers):
        header = ' '.join([f'%{self.column_width}s' %
                           header for header in headers])
        divider = ('-' * self.column_width + ' ') * len(headers)
        print(header)
        print(divider)

    def row(self, row_data):
        print(' '.join([f'%{self.column_width}s' % d for d in row_data]))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join([header for header in headers]))

    def row(self, row_data):
        print(','.join(str(d) for d in row_data))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        inner = ''.join((HTMLTableFormatter.wrap(header, 'th')
                        for header in headers))
        print(HTMLTableFormatter.wrap(inner, 'tr'))

    def row(self, row_data):
        inner = ''.join(HTMLTableFormatter.wrap(d, 'td') for d in row_data)
        print(HTMLTableFormatter.wrap(inner, 'tr'))

    @staticmethod
    def wrap(content, tag):
        return f'<{tag}>{content}</{tag}>'


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.stdout


class ColumnFormatMixin:
    formats = []

    def row(self, row_data):
        row_data = [(fmt % d) for fmt, d in zip(self.formats, row_data)]
        super().row(row_data)


class UpperHeaderMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def create_formatter(type: str):
    format = {
        'html': HTMLTableFormatter,
        'text': TextTableFormatter,
        'csv': CSVTableFormatter,
    }
    return format[type]()


def print_table(records, attributes, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.headings(attributes)
    for record in records:
        row_data = [getattr(record, attribute) for attribute in attributes]
        formatter.row(row_data)
