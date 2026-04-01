try:
    f= open('/home/sanjukta/pythonTraining/FileHandling/Exception_handling/products.txt', 'r')
   
    try:
       data = f.read().split()
       product_name, stock, price = data[0], int(data[1]), float(data[2])
       
       if price <=0:
           raise ValueError('Price must be greater than zero')
       
       print(f'Product: {product_name}, Stock: {stock}, Price: {price}')
       
       qty = int(input('Enter the quantity to purchase: '))   # inbuilt ValurError will be thrown
       
       if qty <=0:
              raise ValueError('Quantity must be greater than zero')
       elif qty > stock:
              raise ValueError('Insufficient stock available')
         
       total = price * qty
       print(f'Total cost: {total}')
       
       discount = total / (qty-1)
       print(f'Discounted total: {discount}')
       
    except ValueError as ve:
        print('Value error:', ve)
       
    except ZeroDivisionError as zde:
        print('Qunaitity should be more than 1 to calcuate the discount', zde)
       
except FileNotFoundError:
    print('File not found, please check the path')
   
except Exception as e:
    print('An error occurred:', e)