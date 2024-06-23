import psycopg2

class MenuItem:
    conn = psycopg2.connect(
            database='Menu',
            user='postgres',
            password='password',
            host='localhost',
            port=5432)
              
    cursor=conn.cursor()
    


    def __init__(self,name="",price=0):
        self.name=name
        self.price=price

    def save (self):
        query = f"INSERT INTO Menu_Items (item_name, item_price) VALUES (%s,%s)"
        self.cursor.execute(query,(self.name,self.price))
        self.conn.commit()
        print ("Saved")
 
    def delete(self):
        query=f"delete from Menu_Items where item_name = %s"
        self.cursor.execute(query,(self.name,))
        self.conn.commit()
        print("Deleted")
 
    def update(self, menu_item,price):
        query=f"update Menu_Items set item_price=%s where item_name =%s"
        self.cursor.execute(query,(price,menu_item))
        self.conn.commit()
        print("Updated")
    
class MenuManager(MenuItem):

    def __init__ (self,name="",price=0):
        super().__init__(name,price)

    def get_by_name(self,name):
        query=f"select * from Menu_items where item_name like %s"
        self.cursor.execute(query,(name,))
        result=self.cursor.fetchone()
        return result

    def all_items(self):
         query=f"select * from Menu_Items"
         self.cursor.execute(query)
         result=self.cursor.fetchall()
         return result
    
if __name__ == "__main__":
        
        try:
           
            MenuItem.cursor.close()
            MenuItem.conn.close()

        except Exception as e:
            print (e)
            




             
        


    
                    


