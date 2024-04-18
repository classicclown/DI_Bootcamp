def divide (num1,num2):
    try:
        (num1/num2)
    except ZeroDivisionError:
        print ("Cannot divide by 0")

divide(5,0)
    
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)