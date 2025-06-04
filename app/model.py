import random
import string
import os
from datetime import datetime, timedelta
import json
import math
import matplotlib.pyplot as plt


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


def generate_random_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_random_people(n=10):
    return [Person(generate_random_name(), random.randint(10, 90)) for _ in range(n)]


def write_people_to_file(people, filename):
    data = [{'name': p.name, 'age': p.age} for p in people]
    with open(filename, 'w') as f:
        json.dump(data, f)


def read_people_from_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return [Person(p['name'], p['age']) for p in data]


def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def random_dates(start, end, n):
    delta = end - start
    return [start + timedelta(days=random.randint(0, delta.days)) for _ in range(n)]


def make_plot(data, title="Random Plot"):
    plt.plot(data)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.savefig("plot.png")
    plt.close()


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def write_random_text_file(filename, lines=10):
    with open(filename, 'w') as f:
        for _ in range(lines):
            line = ''.join(random.choices(string.ascii_letters + ' ', k=40))
            f.write(line + '\n')


def read_and_count_words(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    return len(words)


def create_random_matrix(rows, cols):
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]


def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)


def main():
    print("Generating random people...")
    people = generate_random_people(5)
    for p in people:
        print(f"{p.name} is {p.age} years old")

    filename = "people.json"
    print(f"\nWriting to file: {filename}")
    write_people_to_file(people, filename)

    print("Reading from file...")
    loaded_people = read_people_from_file(filename)
    for p in loaded_people:
        p.birthday()
        print(f"Happy Birthday {p.name}! Now {p.age}")

    print("\nFibonacci sequence (first 10):")
    print(fibonacci(10))

    print("\nChecking for primes from 1 to 20:")
    primes = [i for i in range(1, 21) if is_prime(i)]
    print(primes)

    print("\nGenerating random dates in 2023...")
    dates = random_dates(datetime(2023, 1, 1), datetime(2023, 12, 31), 5)
    for d in dates:
        print(d.strftime("%Y-%m-%d"))

    print("\nFactorials from 0 to 5:")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")

    print("\nGenerating and writing random text...")
    write_random_text_file("random_text.txt", 5)
    word_count = read_and_count_words("random_text.txt")
    print(f"Total words in file: {word_count}")

    print("\nCreating 3x3 random matrix and summing:")
    matrix = create_random_matrix(3, 3)
    for row in matrix:
        print(row)
    print(f"Sum of matrix: {matrix_sum(matrix)}")

    print("\nGenerating plot of 100 random numbers...")
    random_data = [random.randint(0, 50) for _ in range(100)]
    make_plot(random_data)
    print("Plot saved as 'plot.png'")


if __name__ == "__main__":
    main()