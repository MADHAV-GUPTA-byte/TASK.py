try:
    f= open("sample.txt","w")
    writing_file= f.write("This is a sample text file.\n")
    writing_file= f.write("It contains multiple lines.\n")
    f.close()

except FileNotFoundError:
    print("The file 'sample.txt' not found.")


f= open("sample.txt","r")
file_read= f.read()
print(file_read)
f.close()






