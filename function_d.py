def max_value(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    
    return maximum

# this is here for testing

# let's add another line

<<<<<<< HEAD
# changing this line to something else

=======
# this is Steph's line
# this is also Steph's line
>>>>>>> 58e8795e6dc6917bb37ffe7ee1150a35daeb4182

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
# making a new change
