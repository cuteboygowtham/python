#Writing content to file
file = open("demo.txt", 'w')
file.write("This is the New Line Lavade\n")
file.close()
#Reading the content in the file
file = open("demo.txt",'r')
content = file.read()
print(content)
file.close()
#Adding the content to the existing file using append
file = open("demo.txt",'a')
file.write("This is the second line ra lavade")
file.close()

