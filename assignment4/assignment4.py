import pandas as pd
import json

#Task 1

data = {'Name' : ['Alice', 'Bob', 'Charlie'], 
        'Age' : [25, 30, 35], 
        'City' : ['New York', 'Los Angeles', 'Chicago']
        }
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)
task1_data_frame.to_csv('people.csv', index=False)

#adding new column and creating a copy with salary
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)
# modifying the exisitng column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

#saving to csv
task1_older.to_csv('employees.csv', index=False)

#Task 2
#read from CSV and JSON
task2_employees = pd.read_csv('employees.csv')

additional_employees = [{"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
                        {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}]

with open('additional_employees.json', 'w') as json_file:
    #load into new dataframe
    json.dump(additional_employees, json_file)


with open('additional_employees.json', 'r') as json_file:
    json_loaded = json.load(json_file)

    json_employees = pd.DataFrame(json_loaded)
#combine dataframes
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

#Task 3
first_three= more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)
employee_shape = more_employees.shape
print(employee_shape)
employee_info = more_employees.info()
print(employee_info)

#task 4
dirty_data = pd.read_csv('dirty_data.csv')

clean_data= dirty_data.copy()
print(clean_data)

for col in clean_data.columns:
    if clean_data[col].dtype == 'object':
        clean_data[col] = clean_data[col].map(lambda x: x.strip() if isinstance(x, str) else x)

print(clean_data)
clean_data = clean_data.drop_duplicates()
print(clean_data)

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
print(clean_data)

clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].mean())
print(clean_data)

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
clean_data['Hire Date'] = clean_data['Hire Date'].fillna(clean_data['Hire Date'].mean())
print(clean_data)

clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
print(clean_data)
