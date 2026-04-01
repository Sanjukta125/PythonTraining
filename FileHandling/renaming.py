import os
path = '/home/sanjukta/pythonTraining/FileHandling/back'
 
if os.path.exists(path):
    print(" the directory is present ")
    os.rename(path, '/home/sanjukta/pythonTraining/FileHandling/back')
    print(" the directory is renamed ")
else:
    print(" the directory is not present ")
    os.mkdir(path)
    print(" the directory is created ")