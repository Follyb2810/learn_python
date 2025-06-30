command =''
started=False
while True:
    print(command)
    command = input('> ').lower()
    if(command == 'start'):
        if(started):
            print('Car already started')
        else:
            started = True
            print('print cart started...')
    elif command == 'stop':
        if(not started):
            print('car is already stop')
        else:
            started = False
            print('car stop ...')
    elif command == 'help':
        print("""
start - to start cart
stop - to stop car
quit - to quit car
 """)
    elif command == 'quit':
        print('')
        break
    else:
        print('i dont understand you')
else:
    print('')