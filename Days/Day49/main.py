#file IO in Python


# Reading a File 
f = open('file.txt', 'r')
text = f.read()
print(text)

#Writing a file
f = open("file.txt", "w")
text = f.write("Mahfujar Rahman.")
f.close()   #Important


#Appending a file
f = open("file.txt", "a")
# for i in range(0,100):
text = f.write("\nMahfujar Rahman.")
f.close()   #Important

