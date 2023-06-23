'''file = open("student.txt","r")
#print(file.writable())
text=file.readlines()[3]
print(text)
size=len(text)
print(size)
file.close()'''
file=open("student.txt","r")
for line in file:
    print(line)
file.close()