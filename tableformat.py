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
        self.column_width = column_width

    def headings(self, headers):
        header = ' '.join([f'%{self.column_width}s' %
                           header for header in headers])
        divider = ('-' * self.column_width + ' ') * len(headers)
        print(header)
        print(divider)

    def row(self, row_data):
        print(' '.join([f'%{self.column_width}s' % d for d in row_data]))
