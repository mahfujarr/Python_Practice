# OS Module

import os
# import mkdir

folders = os.listdir("Mahfujar")

for folder in folders:
    print(f"{folder}")
    print(os.listdir(f"Mahfujar\{folder}"))

print(os.getcwd())
# os.chdir("C:\Users\mahfujarr\Desktop\py")
# print(os.getcwd())
# os.rmdir("Mahfujar\Folder20")