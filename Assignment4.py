""" Q:1 What is File function in python? What is keywords to create and write file.
--> A:1 File handling is an important part of any web application.
    Python has several functions for creating, reading, updating, and deleting files.
--> keyword to create and write file.
    x = create a file
    w = write into a file
"""
# Q:2 Write a Python program to read an entire text file.
f = open("myfile.txt", "r")
print(f.read())
f.close()
