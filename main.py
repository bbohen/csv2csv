from collections import OrderedDict
import csv

with open('new_headers.csv', 'r') as csvfile:
    new_headers_csv = csv.reader(csvfile)
    fieldnames = next(new_headers_csv)
    fieldname_mappings = next(new_headers_csv)

with open('input.csv', 'r') as infile, open('output.csv', 'a') as outfile:
    writer = csv.DictWriter(
        outfile, extrasaction='ignore', fieldnames=fieldnames)
    writer.writeheader()

    def adjust_row(row_items):
        """TODO: Clean this up or remove need for it"""
        adjusted_items = row_items

        for mapped_fieldname in fieldname_mappings:
            if mapped_fieldname:
                indices = [i for i, x in enumerate(
                    fieldname_mappings) if x == mapped_fieldname]

                if len(indices) > 1:
                    for index in indices:
                        field_key = fieldnames[index]
                        mapped_key = fieldname_mappings[index]
                        row_dict = dict(row_items)
                        value = row_dict[mapped_key]
                        adjusted_items.append((field_key, value))

        return adjusted_items

    def mapper(item):
        value = item[1]
        try:
            indices = [i for i, x in enumerate(
                fieldname_mappings) if x == item[0]]
            field_name_index = fieldname_mappings.index(item[0])
            if len(indices) > 1:
                key = item[0]
            else:
                key = fieldnames[field_name_index]
        except (IndexError, ValueError):
            key = item[0]

        return (key, value)

    for row in csv.DictReader(infile):
        row_items = list(row.items())
        updated_items = adjust_row(row_items)
        mapped_items = list(map(mapper, updated_items))

        writer.writerow(OrderedDict(mapped_items))
