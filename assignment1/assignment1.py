# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return "Hello, " + name + "!"

#Task 3
def calc(num1, num2, operation="multiply"):
    try:
        if operation == "multiply":
            return num1 * num2
        elif operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "divide":
            if num2 == 0:
                return "You can't divide by 0!"
            return num1 / num2
        elif operation == "modulo":
            return num1 % num2
        elif operation == "power":
            return num1 ** num2
        elif operation == "int_divide":
            return num1 // num2
        else:
            return "Invalid operation."
    except TypeError:
        return "You can't " + operation + " those values!"
    
# Task 4

def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return "Invalid target type."
    except ValueError:
        return f"You can't convert {value} into a {target_type}."
    
#Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
#Task 6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result
# Task 7
def student_scores(best, **kwargs):
        if best == "mean":
            return sum(kwargs.values()) / len(kwargs)
        elif best == "best":
            return max(kwargs, key=kwargs.get)
        else:
            return "Invalid option."

# Task 8
def titleize(sentence):
    smallWords = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words=sentence.split()
    result = []

    for i, word in enumerate(sentence.split()):
        if i==0 or  i==len(words)-1 or word.lower() not in smallWords:
            word = word.capitalize()
        result.append(word)
    return ' '.join(result)

# Task 9
def hangman(secret, guess):
    guessed_letters = set(guess)
    result = ""
    for letter in secret:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result

# Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    def convertWord(word):
        if word[0] in vowels:
            return word + "ay"
            #building a consonant cluster to include words like quick square or others that have multiple consonants
       cluster_end=0
    while cluster_end < len(word) and word[cluster_end +1 < len(word) and word[cluster_end + 1] =="u"
        cluster_end+=2
        break
    cluster_end+=1
    return word[cluster_end:]+word[:cluster_end]+"ay"
    return ' '.join(convertWord(word) for word in sentence.split())


# call the functions
hello()
greet("Mike")
print(calc(5, 6, "add"))
print(data_type_conversion("124", "int"))
print(grade(75, 85, 95))
print(repeat("up,", 4))
print(student_scores("best", Tom=75, Mike=89, Angela=91))
print(titleize("war and peace"))
print(hangman("alphabet", "ab"))
print(pig_latin("the quick brown fox"))

