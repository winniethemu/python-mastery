def print_table(records, attributes):
    column_width = 10
    header = ' '.join([f'%{column_width}s' %
                      attribute for attribute in attributes])
    divider = ('-' * column_width + ' ') * len(attributes)
    print(header)
    print(divider)

    for record in records:
        row = ' '.join([f'%{column_width}s' % getattr(
            record, attribute) for attribute in attributes])
        print(row)
