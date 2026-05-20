# 1st remove kr diya kyuki hello world likhna toh aa he gaya hoga😜

# -------------------------------
# 2️⃣ VARIABLES & DATA TYPES
# -------------------------------


# Integer data type
age = 23


# Float data type
height = 5.8


# String data type
name = "Anirudh"


# Boolean data type
is_engineer = True


print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Engineer:", is_engineer)


# -------------------------------
# 3️⃣ TYPE CHECKING
# -------------------------------
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_engineer))  # <class 'bool'>


# -------------------------------
# 4️⃣ USER INPUT
# -------------------------------
# input() always takes input as STRING
user_name = input("Enter your name: ")


# Converting string input to integer
user_age = int(input("Enter your age: "))


print("Hello", user_name)
print("You are", user_age, "years old")


# -------------------------------
# 5️⃣ CONDITIONS (if / elif / else)
# -------------------------------
if user_age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# -------------------------------
# 6️⃣ LOOPS
# -------------------------------


# FOR LOOP
print("For loop example:")
for i in range(1, 6):
    print("Number:", i)


# WHILE LOOP
print("While loop example:")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1


# -------------------------------
# 7️⃣ LIST (Collection data type)
# -------------------------------
numbers = [10, 20, 30, 40]


print("Numbers list:", numbers)
print("First number:", numbers[0])


# Loop through list
for num in numbers:
    print("List value:", num)


# -------------------------------
# 8️⃣ FUNCTION
# -------------------------------


def add_numbers(a, b):
    """
    This function takes two numbers
    and returns their sum
    """
    return a + b


result = add_numbers(5, 7)
print("Sum is:", result)


# -------------------------------
# 9️⃣ FUNCTION WITH CONDITION
# -------------------------------


def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is", check_even_or_odd(10))
print("7 is", check_even_or_odd(7))


# ===============================
# END OF PROGRAM
# ===============================
