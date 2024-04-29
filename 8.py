# Create a Python script that copies the content of one file to another file.
#  copy from A.txt to B.txt
fileA = 'A.txt'
fileB = 'B.txt'

with open(fileA, 'r') as file:
    content = file.read()

with open(fileB, 'w') as file:
    file.write(content)

with open(fileB, 'r') as file:
    print(file.read())
