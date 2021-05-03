data = [
    {'ID' : 123, 'Password' : 'WalidAli1' , 'name':'Walid Ali' , 'AccountBalance': 1500},
    {'ID' : 200, 'Password' : 'ZiadAli1', 'name': 'Ziad Ali' , 'AccountBalance': 2000}
]


def display(id_c , password):

    
    for info in data:
        if info['ID'] == id_c and info['Password']== password:
            print()
            print(str.format(' Welome dear Client {} your Current Balance Accnount is {}', info['name'],info['AccountBalance']))
            Running = True
            while Running:
                print()
                print("1. Add Money to your Balance Account")
                print("2. Take Money from your Balance Account")                
                print("3. Exit your account ")
                print()
                print(" Please choose a task ")
                decision = int(input())
                if decision == 1:
                    print(" Enter the amount of money you want to add")
                    add = int(input())
                    info['AccountBalance'] = add + info['AccountBalance']
                    print(str.format(' Your new Balance is {}',info['AccountBalance']))
                    print()
                elif decision == 2:
                    print(" Enter the amount of money you want to Take ")
                    sub = int(input())
                    new_balance = info['AccountBalance'] - sub
                    if new_balance >=0 :
                        info['AccountBalance']= new_balance
                        print(str.format(' Your new Balance is {}',info['AccountBalance']))
                    else: 
                        print(" You don't have this much to take ")
                elif decision == 3:
                    program_is_running = False
                    break   
                else:
                    print()
                    print(('Please choose a valid option'))    
            break 
    
    if info['ID']!= id_c or info['Password'] != password:
        print()
        print(" Can't login Wrong informations ") 
    return True      


def Client_login():
    print(' Enter  your ID ', end=" ")
    id = int(input())
    print(" Enter your password ", end="")
    password = input()
    display(id,password)






menu_option = """
====================
1. Login as Client
2. Login as Admin
3. Quit

What would you like to do? """

program_is_running = True

while program_is_running:
    decision = int(input(menu_option))
    if decision == 1:
        Client_login()
    elif decision == 2:
        Admin_login()
    elif decision == 3:
        program_is_running = False
    else:
        print()
        print('please choose a valid option')    