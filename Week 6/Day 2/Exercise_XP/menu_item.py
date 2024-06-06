import psycopg2
try:
        connection = psycopg2.connect(
        database='Menu2',
        user='postgres',
            password='',
            host='localhost',
            port=5432
            )
except Exception as e:
            print (f'Error: {e}')      
cursor = connection.cursor()

class MenuItem:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def connect():
        pass
        
    def save (table_name,menu_item,price):
        query=f'insert into {table_name} values {menu_item},{price}'
        #cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return query
 
    def delete(table_name,item_name):
        query=f'delete from {table_name} where item_name like {item_name}'
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def update(table_name, menu_item, price):
        query=f'update {table_name} set item_price={price} where item_name like {menu_item}'
        cursor.execute(query)
        connection.commit()
        cursor.close()
        

    if "name" == '__main__':
        
        table_name='Menu_items'

        user_input = input('Enter which function you want to perform: Save, update or delete.')
        if user_input == 'save':
            # table_name=input('Which table?\n')
            menu_item=input('Which menu item?\n')
            price=input('What price?\n')
            save(table_name,menu_item,price)
        elif user_input=='update':
            # table_name=input('Which table?\n')
            menu_item = input ("What menu item do you want to update?")
            price=input("What price do you want to set?")
            update(table_name,menu_item,price)
        elif user_input=='delete':
            # table_name=input('Which table?\n')
            menu_item = input ("What menu item do you want to delete?")
            delete(table_name,menu_item)
        else:
            user_input=input('Invalid input')

class MenuManager:

    def get_by_name(name):
        query=f'select * from Menu_items where item_name like {name}'
        cursor.execute(query)
        result=cursor.fetchall()
        if result: return result
        else: return None

    def all_items():
         query=f'select * from Menu_Items'
         cursor.execute(query)
         result=cursor.fetchall()
         return result

             
        
    
    
                    


