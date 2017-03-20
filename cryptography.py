"""
cryptography.py
Author: will laycock
Credit: me

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

t=input("Enter e to encrypt, d to decrypt, or q to quit: ")

if t is 'e':
    m=input("message: ")
    numbers=[]
    for c in m:
        n=associations.find(c)
        numbers.append(n)
    k=input("key: ")
    letters=[]
    for c in k:
        l=associations.find(c)
        letters.append(l)
    print(numbers)
    print(letters)
elif t is 'd':
    m=input("message: ")
    numbers=[]
    for c in m:
        n=associations.find(c)
        numbers.append(n)
    k=input("key: ")
    letters=[]
    for c in k:
        l=associations.find(c)
        letters.append(l)
    print(numbers)
    print(letters)
elif t is 'q':
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
