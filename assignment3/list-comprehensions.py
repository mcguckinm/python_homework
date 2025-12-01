import csv

with open('../csv/employees.csv', 'r') as f:
    reader = csv.DictReader(f)
    data_rows=list(reader)

    employee_names = [r['first_name'] + ' ' + r['last_name'] for r in data_rows]
    print(employee_names)

    names_with_e = [r['first_name'] + ' ' + r['last_name'] for r in data_rows if 'e' in (r['first_name']+ ' ' + r['last_name']).lower()]
    print(names_with_e)
