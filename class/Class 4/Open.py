My_File = ("D:/new text.txt", 'r+')
content = My_File.read()
My_File.close()
print(content)


My_file = open("D:/new text.txt", 'r+')
content = My_file.write("This text is added to the file it self")       # writing inside the file it self.
