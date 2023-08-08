import csv
with open("TakSejahteraData.csv","a", newline="") as signup:
    fieldname =["FullName","Age","IDNumber","phoneNumber","postCode","Adress","password"]
    writeNewUser =csv.DictWriter(signup, fieldnames =fieldname)
    print("Please input your information:")
    FullName =input("Full Name: ")
    Age =input("Age: ")
    IDNumber =input("Your ID: ")
    phoneNumber =input("Phone Number: ")
    postCode =input("Postal Code: ")
    Adress =input("Full Adress: ")
    print('Do you work in one of these occupations catagories?')
    print('1- Health-care worker')
    print('2- Community services')
    print('3- Energy')
    print('4- Food and transportation workers')
    print('5- Students')
    occ = input('Answer: ')
    print("Enter a password for your account:")
    password =input("")

    writeNewUser.writeheader()
    writeNewUser.writerow({
        "FullName" : FullName,
        "Age" : Age,
        "IDNumber" : IDNumber,
        "phoneNumber" : phoneNumber,
        "postCode" : postCode,
        "Adress":Adress,
        "password" : password
    })

print("Registration complete.")
NewUserLogin=input("Would you like to exit, or log in? Y/N:")
if NewUserLogin =="Y":
    import UserLogIn
else:
    print("Thank you for signing up.Have a nice day," +FullName)

