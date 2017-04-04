phonelist = {'Troy': {'name': 'Sara Troy', 'phone': '805-215-9908'}}

def add():
    name_a_1 = input('What is ther persons\' first name?: ')
    name_a_2 = input('What is their last name?: ')
    number_a = input('What is their number?: ')
    phonelist[name_a_2] = {'name': [name_a_1]+[name_a_2], 'phone': [number_a]}
    print(phonelist)

def remove():
    name_r_2 = input('Okay, what is the persons\' last name?: ')
    print(phonelist[name_r_2])
    q = input('Is this the entry you wish to edit?  y/n: ')
    if q == 'y':
        del(phonelist[name_r_2])
    elif q == 'n':
        print('okay, lets start over.')


def edit():
    name_e_2 = input('Okay, what is the persons\' last name?: ')
    print(phonelist[name_e_2])
    q = input('Is this the entry you wish to edit?  y/n: ')
    if q == 'y':
        del(phonelist[name_e_2])
        print('Okay, let\'s renenter {}\'s info'.format(name_e_2))
        add()
    elif q == 'n':
        print('okay, lets start over.')

def find():
    # name_f_1 = input('What is their first name?: ')
    name_f_2 = input('What is ther persons\'last name?: ')
    print(phonelist[name_f_2])

def start():
    something = input('Do you want to Add (a), Find (f), Edit (e), Remove (r) an entry?, or Quit (q): ')
    if something == 'a':
        add()
    if something == 'f':
        find()
    if something == 'e':
        edit()
    if something == 'r':
        remove()
    if something == 'q':
        print("Good Bye")
        quit()
while True:
    start()
