class RangeError(Exception):
    pass
 
try:
    number1 = int(input("Enter a number: "))
   
    if number1 >50 and number1 <100:
        raise RangeError("number1 should be between 0 and 50")
   
    number2 = int(input("Enter asecond number: "))
 
    result = number1/number2
   
except ZeroDivisionError:
    print("exception caught:",e)
       
except ValueError as e:
    print("exception caught:",e)  
   
except RangeError as e:
    print("custom error caught:",e)  
 
else:
    print("The result is:", result)