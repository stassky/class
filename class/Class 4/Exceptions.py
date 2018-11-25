from selenium import webdriver
try:
    My_File = open("D:/new text.tx", 'r+')
    content = My_File.read()
    content.close()
except IOError:
    print('content')


My_file = open("D:/new text.txt", 'r+')
content = My_file.write("This text is added to the file it self")       # writing inside the file it self.

finally:                                                                # נועד בשביל לסבר את העין
    print("FINALLY is for visual and code ORDER")