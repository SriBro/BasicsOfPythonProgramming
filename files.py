#Writing to file
file1 = open("sri.txt","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("Write this to my file","UTF-8"))
file1.close()

#Reading contents of a file
#r+ is used to read as well as write
file2 = open("sri.txt","r+")
text_to_read = file2.read()
print(text_to_read)