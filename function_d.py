def max_value(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    
    return maximum


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
