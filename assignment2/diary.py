import traceback

try:
    with open('diary.txt', 'w') as file:
        while True:
            entry = input("What happened today? " )
            file.write(entry + '\n')
            whatelse = input("Anything else to add? (yes/no) ")
            while whatelse.lower() == 'yes':
                entry = input("What else? " )
                file.write(entry + '\n')
                whatelse = input("Anything else to add? (yes/no) ")
            if whatelse.lower() == 'no':
                print("Your diary has been updated.")
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace=list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]} , Func.Name : {trace[2]} , Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
