#Task 2
import csv

def read_employees():
    employees = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            fields = next(reader)  # Skip header row
            employees['fields'] = fields
            
            for row in reader:
                rows.append(row)
            employees['rows'] = rows
                
        return employees
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

employees = read_employees()
print(employees)

#Task 3
def column_index(column_name):
    if 'fields' in employees:
        try:
            index = employees['fields'].index(column_name)
            return index
        except ValueError:
            print(f"Column '{column_name}' not found.")
            return None
    else:
        print("No fields found in employees data.")
        return None

print(column_index('employee_id'))


#task 4
def first_name(row_number):
    if 'rows' in employees:
        try:
            row = employees['rows'][row_number]
            first_name_index = column_index('first_name')
            if first_name_index is not None:
                return row[first_name_index]
        except IndexError:
            print(f"Row number {row_number} is out of range.")
            return None
    else:
        print("No rows found in employees data.")
        return None
    
print(first_name(3)) 

#Task 5
def employee_find(employee_id):
    if 'rows' in employees:
        for row in employees['rows']:
            def employee_match(row):
                return row[column_index('employee_id')] == employee_id
            matches=list(filter(employee_match, employees['rows']))
            if matches:
                return matches[0]
        print(f"Employee with ID {employee_id} not found.")
        return None
    else:
        print("No rows found in employees data.")
        return None
    
print(employee_find('10'))

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: row[column_index('employee_id')] == employee_id, employees['rows']))
    return matches
print(employee_find_2('10'))

def sort_by_last_name():
    if 'rows' in employees:
        sorted_employees = sorted(employees['rows'], key=lambda row: row[column_index('last_name')])
        return sorted_employees
    else:
        print("No rows found in employees data.")
        return None
    
print(sort_by_last_name())