print('-' * 30)
print('1) Sign Up For An Account')
print('2) Log In')
print('3) Return To Main Menu')
print('-' * 30)
print('')
SignUpOrLogIn =input("")
if SignUpOrLogIn =="1":
    import UserSignUp
elif SignUpOrLogIn =="2":
    import UserLogIn
elif SignUpOrLogIn == "3":
    import Mainmenu
else:
    print('Please Enter A Valid Option!')
