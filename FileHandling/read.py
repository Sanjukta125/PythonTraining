def read_first_n_lines(filename,n):   # read the specific first N lines of a file
    with open(filename,'r') as f:
        for i in range(n):
            line = f.readline()
            print(type(line))
            if not line:
                break
            print(line.strip())
           
read_first_n_lines('',15)