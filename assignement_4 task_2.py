a=input("Enter text to write to the file: ")

print("Data successfully written to the output.txt.")

file_1=open("output.txt","w")
file_writing=file_1.write(a+"\n")
file_1.close()

b=input("Enter additional text to append: ")
print("Data successfully appended.")

file_2=open("output.txt","a")
file_appending=file_2.write(b+"\n")
file_2.close()

c=open("output.txt","r")
print(c.read())
c.close()


