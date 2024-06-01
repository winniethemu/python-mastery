def print_table(records, attributes, formatter):
    formatter.headings(attributes)
    for record in records:
        row_data = [getattr(record, attribute) for attribute in attributes]
        formatter.row(row_data)


class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

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


def create_formatter(type: str):
    format = {
        'html': HTMLTableFormatter,
        'text': TextTableFormatter,
        'csv': CSVTableFormatter,
    }
    return format[type]()
