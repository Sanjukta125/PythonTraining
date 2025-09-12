import glob
import re
txt_files=glob.glob("C:/Users/hp/pythonWork/Glob&Remodule/*.txt")
print(txt_files)
for files in txt_files:
    with open(files,"r") as f:
        content=f.read()
        if re.search(r"Python",content):
            print(f"found python in:{files}")
        else:
            print("not found")