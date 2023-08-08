while True:
    print('-' * 30) #menu1
    print('Welcome to MMU MySejahtera Menu')
    print('-' * 30)
    print('1) Public User')
    print('2) Administrator')
    print('3) Exit MMU MySejahtera')
    print('')
    choice = int(input('Enter Your Choice: '))
    print('')
    if choice == 1:
        import LogInSignUpUser
    elif choice == 2:
        import LogInSignUpAdmin
    elif choice == 3:
        quit()
    else:
        print('Please Enter A Valid Option!')
