# #Ex. 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# combined = dict(zip(keys,values))
# print (combined)

# #Ex.2
# ticket_prices ={}
# total_cost=0
# family = {}
# fam = input("Please input a name and an age for each family member in this format name:age,name:age")
# pairs = fam.split(",")

# for pair in pairs:
#     key, value = pair.split(":")
#     family[key]=int(value)
    
# #family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# for name,age in family.items():
#     if age<3:
#         ticket_prices[name]=0
#     elif 3<age<12:
#         ticket_prices[name]=10
#     else:
#         ticket_prices[name]=15

# for name,price in ticket_prices.items():
#     print(f"{name} has to pay {price}")
#     total_cost+=price
# print(f"The total cost is {total_cost}")

#Ex.3
# brand = {
#     "name":"Zara",
#     "Creation date":1975,
#     "Creator name":"Amancio Ortega Gaona",
#     "Type of clothes":["men",'women','children','home'],
#     "International competitors":['Gap','H&M','Benetton'],
#     "Number stores":7000,
#     "Major colour":{"France":"blue","Spain":"red","US":"pink"}
# }

# brand ["number of stores"]=2
# print (f"Zara's clients are {brand['Type of clothes'][0:3]}")
# brand ['Country Creation']=["Spain"]
# if "international competitors" in brand:
#     brand["International competitors"].append("Desigual")
# del (brand ["Creation date"])
# print (brand["International competitors"][-1])
# print (brand["Major colour"]["US"])
# print (len(brand))
# print (brand.keys)
# more_on_zara = {"creation date":1975,"number_stores":10000}

# def add_to_dict (dictionary1,dictionary2):
#     for key,value in dictionary1.items():
#         dictionary2[key]=value

# add_to_dict(more_on_zara, brand)
# print (brand["number_stores"])

#Ex.4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A ={}
disney_users_B ={}
disney_users_C ={}
for name in enumerate(users):
    # disney_users_A[name[1]] = name[0]
    # disney_users_B[name[0]]=name[1]
    disney_users_A = {name:index for index,name in enumerate(users)}
    disney_users_B = {index:name for index,name in enumerate(users)}
def disney_users_sorted (dict):
    # sorted_dict=sorted(dict.keys())
    # for name in enumerate(sorted_dict):
    #     disney_users_C[name[1]] = name[0]
    disney_users_C = {name:index for index,name in enumerate(sorted(dict.keys()))}

    return disney_users_C


disney_users_A_if_i = {name:index for index,name in enumerate(users) if "i" in name}
disney_users_A_if_mp = {name:index for index,name in enumerate(users) if name[0].lower() in ("m","p")}


# print (disney_users_A)
# print (disney_users_B)
# print (disney_users_sorted(disney_users_A))
print (disney_users_A_if_i)
print (disney_users_A_if_mp)


