data = [
    {'ID' : 123, 'Password' : 'WalidAli1' , 'name':'Walid Ali' , 'AccountBalance': 1500},
    {'ID' : 200, 'Password' : 'ZiadAli1', 'name': 'Ziad Ali' , 'AccountBalance': 2000}
]


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
        Client_log()
    if decision ==2:
        Admin_log()    
    elif decision == 3:
        program_is_running = False
    else:
        print()
        print('please choose a valid option')    