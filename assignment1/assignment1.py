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
        elif operation == "exponent":
            return num1 ** num2
        elif operation == "int_divide":
            return num1 // num2
        else:
            return "Invalid operation."
    except TypeError:
        return "You can't " + operation + " those values!"
    
# Task 4

def dataTypeConversion(value, target_type):
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
        return "You can't convert " + str(value) + " into a " + target_type + "."
    
#Task 5
def gradingSystem(*args):
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
    for _ in range(count):
        string += string
    return string
# Task 7
def studentScores(best, **kwargs):
    for key, value in kwargs.items():
        if best == "mean":
            return sum(kwargs.values()) / len(kwargs)
        elif best == "best":
            return max(kwargs, key=kwargs.get)

# Task 8
def titleize(sentence):
    smallWords = ["a", "on", "an", "the", "of", "and", "is", "in"]
    result = []

    for i, word in enumerate(sentence.split()):
        if i==0 or word.lower() not in smallWords:
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
def pigLatin(sentence):
    vowels = "aeiou"
    def convertWord(word):
        if word.startswith("qu"):
            newWord=word[:2] + "ay" #Keeps the first two letters together for a qu start
        elif word[0] in vowels:
            return word + "ay"
        else:
            for i, letter in enumerate(word):
                if letter in vowels or (letter=='q' and i+1 <len(word) and word[i+1]=='u'):
                    newWord=word[i:] + word[:i] + "ay"
                    return newWord
            return word + "ay"  # for words without vowels
    return ' '.join(convertWord(word) for word in sentence.split())


# call the functions
hello()
greet("Mike")
print(calc(5, 6, "add"))
print(dataTypeConversion("124", "int"))
print(gradingSystem(75, 85, 95))
print(repeat("up,", 4))
print(studentScores("best", Tom=75, Mike=89, Angela=91))
print(titleize("war and peace"))
print(hangman("alphabet", "ab"))
print(pigLatin("the quick brown fox"))
