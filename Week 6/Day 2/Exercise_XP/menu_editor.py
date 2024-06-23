from menu_item import MenuItem
from menu_item import MenuManager
def show_user_menu():
    user_choice=input('''1.View an Item(V)\n2.Add an item(A)\n3.Delete an Item(D)
4.Update an Item(U)\n5.Show the Menu(S)\n6.Quit(Q)\n''')
    return user_choice

def view_item(manager):
    item=input("What item do you want to view?\n")
    result = manager.get_by_name(item)
    print(result)
    #manager.close_connection()
    
def add_item_to_menu():
    item=input("What item do you want to add?\n")
    price=input("What price?\n")
    menu=MenuItem(item,price)
    menu.save()
    

def remove_item_from_menu():
    item=input("What item do you want to remove?\n")
    menu=MenuItem(item)
    menu.delete()

def update_item_menu():
    item=input("What item do you want to update?\n")
    price=input("What price?\n")
    menu=MenuItem()
    menu.update(item,price)

def show_rest_menu(manager):
    items=manager.all_items()
    for item in items:
        print (item)

if __name__=='__main__':

    user = show_user_menu().lower()
    manager=MenuManager()
    menu=MenuItem()
    while user != 'q':
        if user == 'v':
            view_item(manager)
            break
        elif user == 'a':
            add_item_to_menu()
            break
        elif user=='d':
            remove_item_from_menu()
        elif user=='u':
            update_item_menu() 
            break
        elif user=='s':
            show_rest_menu(manager)
            break
        else:
            print('Invalid input')
    else:
        show_rest_menu()
        
    

    

