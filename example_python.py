import json
import unittest
                #--- USE UNITTEST AND THE -INTERNET- TO DO TESTING, NOT CHATGPT. ---#

def tableJSON():
    filename = input("Enter file name... ")

    with open(filename, 'r') as file:
        data = json.load(file)

    def flatten_json(y, prefix=''):
        out = {}
        if isinstance(y, dict):
            for k, v in y.items():
                full_key = f"{prefix}.{k}" if prefix else k
                out.update(flatten_json(v, full_key))
        elif isinstance(y, list):
            for i, v in enumerate(y):
                full_key = f"{prefix}[{i}]" if prefix else f"[{i}]"
                out.update(flatten_json(v, full_key))
        else:
            out[prefix] = str(y)
        return out

    def extract_records(obj):
        records = []
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict):
                    records.append(flatten_json(item))
        elif isinstance(obj, dict):
            for val in obj.values():
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, dict):
                            records.append(flatten_json(item))
        return records

    rows = extract_records(data)

    all_keys = set()
    for row in rows:
        for k, v in row.items():
            if v.strip() != '':
                all_keys.add(k)

    all_keys = sorted(all_keys)

    def last_key_only(key):
        return key.split('.')[-1].split('[')[0] if '.' in key or '[' in key else key

    def truncate(s, width):
        return s if len(s) <= width else s[:width-3] + "..."

    def is_number(s):
        try:
            float(s)
            return True
        except:
            return False

    col_widths = {}
    for k in all_keys:
        col_widths[k] = max(len(last_key_only(k)), max(len(row.get(k, '')) for row in rows))

    max_col_width = 20
    for k in col_widths:
        col_widths[k] = min(col_widths[k], max_col_width)

    row_num_width = max(len(str(len(rows))), 3)

    def format_cell(val, width, numeric=False):
        val = truncate(val, width)
        return val.rjust(width) if numeric else val.ljust(width)

    header = format_cell("RowID", row_num_width)
    for k in all_keys:
        header += "   " + format_cell(last_key_only(k), col_widths[k])
    print(header)
    print(" " * row_num_width + " " + "-" * (len(header) - row_num_width - 1))

    for idx, row in enumerate(rows, 1):
        line = format_cell(str(idx), row_num_width, numeric=True)
        for k in all_keys:
            v = row.get(k, '')
            numeric = is_number(v)
            line += "   " + format_cell(v, col_widths[k], numeric)
        print(line)

tableJSON()