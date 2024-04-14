def divide (num1,num2):
    try:
        (num1/num2)
    except ZeroDivisionError:
        print ("Cannot divide by 0")

divide(5,0)
    