PHONEBOOK = {}

def add_number(number, name):

    if len(PHONEBOOK[name]) > 0:
        PHONEBOOK[name].append(number)
        numbers = PHONEBOOK[name]
    else:
        numbers  = [number]
        
    
    new_number = {numbers: name}
    PHONEBOOK.update(new_number)


def delete_name(name):
    
    for phonebook_name in PHONEBOOK.keys():
        if name == phonebook_name:
            PHONEBOOK.pop(name)
            return
    print('Not found')
    

def find_name(name):
    
    for phonebook_name in PHONEBOOK.keys():
        if name == phonebook_name:
            print (str(PHONEBOOK[name]))
            return
        
    
    print('Not found')
    
while True:
    command = input("add/del/find?\n")
    com = command.split(" ")[0]

    if com == "add":
        x, name, num = command.split(" ")
        add_number(num, name)
    elif com == "del": 
        name = command.split(" ")[1]
        delete_name(name)
    elif com == "find":
        name = command.split(" ")[1]
        find_name(name)
    else:
        print("Invalid input")
    
    
