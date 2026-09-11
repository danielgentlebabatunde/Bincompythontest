from collections import Counter
import random

# Colours worn during the week
colours = [
    # Monday
    "green", "yellow", "green", "brown", "blue", "pink",
    "blue", "yellow", "orange", "cream", "orange", "red",
    "white", "blue", "white", "blue", "blue", "blue", "green",

    # Tuesday
    "brown", "green", "brown", "blue", "blue", "blue",
    "pink", "pink", "orange", "orange", "red", "white",
    "blue", "white", "white", "blue", "blue", "blue",

    # Wednesday
    "green", "yellow", "green", "brown", "blue", "pink",
    "red", "yellow", "orange", "red", "orange", "red",
    "blue", "blue", "white", "blue", "blue", "white", "white",

    # Thursday
    "blue", "blue", "green", "white", "blue", "brown",
    "pink", "yellow", "orange", "cream", "orange", "red",
    "white", "blue", "white", "blue", "blue", "blue", "green",

    # Friday
    "green", "white", "green", "brown", "blue", "blue",
    "black", "white", "orange", "red", "red", "red",
    "white", "blue", "white", "blue", "blue", "blue", "white"
]


# Count how many times each colour appears
frequency = Counter(colours)

print("Colour frequencies:")
for colour, number in frequency.items():
    print(colour, ":", number)


# 1. Mean
total = len(colours)
number_of_colours = len(frequency)

mean = total / number_of_colours

print("\nMean frequency:", mean)


# 2. Mostly worn colour (Mode)
most_worn = frequency.most_common(1)[0]

print("Colour mostly worn:", most_worn[0])
print("Number of times worn:", most_worn[1])


# 3. Median
values = sorted(frequency.values())

middle = len(values) // 2

if len(values) % 2 == 0:
    median = (values[middle - 1] + values[middle]) / 2
else:
    median = values[middle]

print("Median frequency:", median)


# 4. Variance
mean_frequency = sum(frequency.values()) / len(frequency)

variance = sum(
    (x - mean_frequency) ** 2 for x in frequency.values()
) / len(frequency)

print("Variance:", variance)


# 5. Probability of randomly selecting RED
red_count = frequency["red"]

probability_red = red_count / total

print("Probability of red:", probability_red)


# 7. Recursive search
def recursive_search(numbers, target, index=0):

    if index == len(numbers):
        return False

    if numbers[index] == target:
        return True

    return recursive_search(numbers, target, index + 1)


numbers = [2, 5, 8, 10, 15, 20]

number_to_find = int(input("\nEnter a number to search for: "))

if recursive_search(numbers, number_to_find):
    print("Number found")
else:
    print("Number not found")


# 8. Generate a random 4-digit binary number
binary_number = ""

for i in range(4):
    binary_number += str(random.randint(0, 1))

decimal_number = int(binary_number, 2)

print("\nRandom binary number:", binary_number)
print("Base 10:", decimal_number)


# 9. First 50 Fibonacci numbers
a = 0
b = 1
total_fibonacci = 0

for i in range(50):
    total_fibonacci += a
    a, b = b, a + b

print("Sum of first 50 Fibonacci numbers:", total_fibonacci)
