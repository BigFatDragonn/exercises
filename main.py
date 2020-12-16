str_1 = input()
# int in the beginning of the list comprehension and in the if otherwsie won't work at all and gives "typeerror: not all arguments converted ... in Python" error.
print([int(i) for i in str_1 if int(i) % 2 == 1])
