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
    n=associations.find(m)
    k=input("key: ")
    l=associations.find(k)
    print(m)
elif t is 'd':
    m=input("message: ")
    n=associations.find(m)
    k=input("key: ")
    l=associations.find(k)
elif t is 'q':
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
