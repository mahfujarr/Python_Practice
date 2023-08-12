#Seek & tell Functions


with open('sample.txt', 'w') as f:
    f.write("Mahfujar Rahman")
    # f.truncate(5)
    # print(type(f))


with open('sample.txt', 'r') as f:
    print(type(f))

    seek = f.seek(3)             #Move to the 10th bite of the file
    # print(f.tell())
    print(f"Seeked to : {f.tell()}")
    data = f.read(5)       #Read the next 5 bytes.
    print(data)

