sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]
total_sales={}
for sales in sales_data:
    product = sales["product"]
    price=sales["price"]*sales["quantity"]

    if product not in total_sales:
        total_sales[product] = price
    else:
        total_sales[product]+=price



customer_spend = {}

for customer in sales_data:
    user = customer["customer_id"]
    spend = customer["price"]*customer["quantity"]

    if user not in customer_spend:
        customer_spend[user]=spend
    else:
        customer_spend[user]+=spend


for data in sales_data:
    data["total price"]= data["quantity"]*data["price"]



#4
high_value=[]
for data in sales_data:
    if data["total price"]>500:
        high_value.append(data)

print (high_value)



