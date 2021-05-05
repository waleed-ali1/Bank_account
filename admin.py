from client import *
data = [
    {'ID' : 123, 'Password' : 'WalidAli1' , 'name':'Walid Ali' , 'AccountBalance': 1500},
    {'ID' : 200, 'Password' : 'ZiadAli1', 'name': 'Ziad Ali' , 'AccountBalance': 2000}
]

admin_data = [
    {'username' : 'admin_1', 'Password' : 'admin1' , 'name':'mhamad'},
    {'username' : 'admin_2', 'Password' : 'admin2', 'name': 'ahmad'}
]



def display_admin(userN , password):

    
    for info in admin_data:
        user_dic = {}
        if info['username'] == userN and info['Password']== password:
            print()
            print(str.format(' Welcome dear Admin {} ', info['name']))
            Running = True
            while Running:
                print()
                #print("0. List of clients")
                print("1. Add a client ")
                print("2. Remove a client ")                
                print("3. Exit your account ")
                print()
                print(" Please choose an operation ")
                decision = int(input())
                if decision == 1:
                    print(" Enter his ID")
                    id = int(input())
                    user_dic["ID"]=id
                    print(" Enter his name")
                    name_us = input()
                    user_dic["name"]= name_us
                    print(" Enter his password")
                    passw = input()
                    user_dic["password"]=passw
                    user = user_dic.copy()
                    data.append(user)
                    
                    print(' The new list of Clients is')
                    print()
                    for client in data:
                        print(client)
                        
                elif decision == 2:
                    print(" Enter the ID's Client you want to delete ")
                    del_id = int(input())
                    print(" Enter his password ")
                    passwd = input()
                    for i in range(len(data)):
                        if data[i]['ID'] == del_id and data[i]['Password'] == passwd:
                                del data[i]
                                print(' The new list of Clients is')
                                for client in data:
                                    print(client)                            
                                break
                        else:
                            print(" This client does not exist")
                            break     
                elif decision == 3:
                    program_is_running = False
                    break   
                else:
                    print()
                    print(('Please choose a valid option'))    
            break 
    
    if info['username']!= userN or info['Password']!= password:
        print()
        print(" Can't login Wrong informations ") 
    return True      


def Admin_login():
    print(' Enter  your username ', end=" ")
    username = input()
    print(" Enter your password ", end="")
    password = input()
    display_admin(username, password)



  


