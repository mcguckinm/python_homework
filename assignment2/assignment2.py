#Task 2
import csv
import os
import traceback
import custom_module
from datetime import datetime

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
    
employee_id_column = column_index('employee_id')
print(employee_id_column)



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
    emp_col = column_index('employee_id')
    employee_id = int(employee_id)
    matches = list(filter(lambda row: int(row[emp_col]) == employee_id, employees['rows']))
    return matches
    
print(employee_find('10'))

#Task 6
def employee_find_2(employee_id):
    emp_col = column_index('employee_id')
    return list(filter(lambda row: int(row[emp_col]) == employee_id, employees['rows']))
print(employee_find_2('10'))

#Task 7

def sort_by_last_name():
    if 'rows' in employees:
        sorted_employees = sorted(employees['rows'], key=lambda row: row[column_index('last_name')])
        return sorted_employees
    else:
        print("No rows found in employees data.")
        return None
    
print(sort_by_last_name())

#Task 8
def employee_dict(employee_row):
    if 'fields' in employees:
        employee_dict = {}
        for i, field in enumerate(employees['fields']):
            if field != 'employee_id':  # Exclude employee_id
                employee_dict[field] = employee_row[i]
        return employee_dict
    else:
        print("No fields found in employees data.")
        return None
    
print(employee_dict(employees['rows'][0]))

#Task 9
def all_employees_dict():
    if 'rows' in employees:
        all_employees = {}
        for row in employees['rows']:
            emp_id = row[column_index('employee_id')]
            all_employees[emp_id] = employee_dict(row)
        return all_employees
    else:
        print("No rows found in employees data.")
        return None
    
print(all_employees_dict())

#Task 10
def get_this_value():
    THISVALUE = os.getenv('THISVALUE', 'ABC')
    return THISVALUE
print(get_this_value())

#Task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    print(new_secret)

#Task 12

def read_csv_as_dict(path):
    result = {}
    with open(path, 'r') as file:
        reader = csv.reader(file)
        result['fields']=next(reader)
        result['rows'] = [tuple(row) for row in reader]
    return result

def read_minutes():
    try:
        minutes1 = read_csv_as_dict('../csv/minutes1.csv')
        minutes2 = read_csv_as_dict('../csv/minutes2.csv')
        return minutes1, minutes2
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace= []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]} , Func.Name : {trace[2]} , Message : {trace[3]}')
        print(f"An error occurred: {e}")
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        return None, None
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)    
    #Task 13
def create_minutes_set():
    minutes_set = set()
    minutes1, minutes2 = read_minutes()
    if minutes1 and minutes2:
        for row in minutes1['rows']:
            minutes_set.add(row)
        for row in minutes2['rows']:
            minutes_set.add(row)
    return minutes_set

print(create_minutes_set())

#Task 14
def create_minutes_list():
    minutes_set= create_minutes_set()
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], '%B %d, %Y')), minutes_set))

    return minutes_list

#Task 15
def write_sorted_list():
    minutes_list = create_minutes_list()
    minutes_list.sort(key=lambda x: x[1])
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Date'])
        for name, date in minutes_list:
            writer.writerow([name, date.strftime('%B %d, %Y')])

    return minutes_list

