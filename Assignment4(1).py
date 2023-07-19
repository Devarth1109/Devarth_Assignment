# Write a Python program to append text to a file and display the text.
f = open("myfile1.txt",'r')
print(f.read())
f.close()
print("===================================================")

# Write a Python program to read first n lines of a file.
f = open("myfile1.txt",'r')
print(f.readline())
f.close()
print("===================================================")

# Write a Python program to read last n lines of a file.
f = open("myfile1.txt",'r')
print(f.readlines(1))
f.close()
print("===================================================")

# Write a Python program to read a file line by line and store it into a list
f = open("myfile1.txt",'r')
print(f.readlines())
f.close()
print("===================================================")

# Write a Python program to read a file line by line store it into a variable.
f = open("myfile1.txt",'r')
r1 = f.readlines()
print(r1)
f.close()


