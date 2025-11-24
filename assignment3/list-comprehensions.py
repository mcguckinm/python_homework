import csv

with open('../csv/employees.csv', 'r') as f:
    reader = csv.DictReader(f)
    row=list(reader)

    data_rows = row[1:]
    employee_names = [row['first_name'] + ' ' + row['last_name'] for row in data_rows]
    print(employee_names)

    names_with_e = [row['first_name'] + ' ' + row['last_name'] for row in data_rows if 'e' in row['first_name']]
    print(names_with_e)
