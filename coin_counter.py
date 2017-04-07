def coins(*args):
    list = []
    ammnt = int(input('How much money do you want to change?: '))
    for args in args:
        if ammnt < args:
            list.append(0)
        elif ammnt >= args:
            whole = ammnt // args
            list.append(whole)
            ammnt = ammnt % args

    print(list)


coins(25,10,5,1)
