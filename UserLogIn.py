import csv

print("Please enter your login details.")
loginID =input("Your ID:")
loginPassword =input("Your Password:")
with open("TakSejahteraData.csv","r") as login:
    UserData = csv.DictReader(login)
    for row in UserData:
            if((row["IDNumber"] == loginID) and (row["password"] == loginPassword)):
                print("Welcome," + row["FullName"] + "!")
                import UserMenu
            else:
                continue
        
    # i = 0
    # UserData =login.readlines()
    # while i < UserData:
    #     if loginID == Fullname
