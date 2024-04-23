# my_functions.py
# Author: Eoghan Walsh


def fibonacci(number):
    a = 0
    b = 1
    fibonacci_sequence = [0]
    for i in range(1, number):
        fibonacci_sequence.append(b)
        a, b = b, a + b
    return [fibonacci_sequence]


print(fibonacci(10))

if __name__ == '__main__':
    return7 = [0, 1, 1, 2, 3, 5, 8]
    return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return value for 0'
    assert fibonacci(1) == [0], 'incorrect return value for 1'
    print("all good")
