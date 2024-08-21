# f "filename.txt"
fileX = open("/Users/brandontran/Documents/CECS 174/test") #'w' for write, 'r' for read, 'a' for append, 'r+' for read and write
content = fileX.read()
print(content)
fileX.close()

fileW = open("/Users/brandontran/Documents/CECS 174/test", 'w')
fileW.write("Hello World")
fileW.close()

# always close the file after opening it to prevent memory leaks

fileA = open("/Users/brandontran/Documents/CECS 174/test", 'a')
fileA.write("\nGoodbye World")
fileA.close()