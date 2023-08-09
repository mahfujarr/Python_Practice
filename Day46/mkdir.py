#OS module in python

import os
# import shutil

if(not os.path.exists("Mahfujar")):
    os.mkdir("Mahfujar")

for i in range(0,20):
    os.mkdir(f"Mahfujar\Folder{i+1}")
    # shutil.rmtree("Mahfujar")