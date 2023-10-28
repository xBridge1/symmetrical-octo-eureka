import random

print('Password Generator')

chars = ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!##$%¨&*().,?')

numbers = input('Choose the amount of passwords to generate:')
numbers = int(numbers)

length = input('Choose password length:')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(numbers):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print (passwords)