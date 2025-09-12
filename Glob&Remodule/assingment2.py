import glob
import re
import os

all_files = glob.glob("C:/Users/hp/pythonWork/Glob&Remodule/*")
pattern = r"^data_.*\.csv$"

for file in all_files:
    filename = os.path.basename(file)  # get only the file name
    if re.match(pattern, filename):
        print(f"matched file: {filename}")
