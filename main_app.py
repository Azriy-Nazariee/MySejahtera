# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL2V & TL3V
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211104288 | MOHD AZRIY AKMALHAZIM BIN MOHD NAZARIEE | 1211104288@student.mmu.edu.my | 017-2071317
# Member_2: 1211103148 | MUHAMAD IZZUL IQBAL BIN ISMAIL | 1211103148@student.mmu.edu.my | 011-58861607
# Member_3: 1211103388 | VISHNU KARMEGAM | 1211103388@student.mmu.edu.my | 011-23041303
# Member_4: 1211104293 | NOOR HANNAN BIN NOOR HAMSURUDDIN | 1211104293@student.mmu.edu.my | 011-7294 1458
# *********************************************************
# Task Distribution
# Member_1: User's Medical Information Updates and Appointment Checking
# Member_2: Administrator Tasks
# Member_3: Menu and Display Result
# Member_4: Data Structure, Sign Up and Log In
# *********************************************************

# 🔽 Functions Definitions -----------------------------------------------------

def out():
    print('-' * 30)
    print('Do you want to exit / go to the menu?')
    print('-' * 30)
    print('1) Exit')
    print('2) Menu')
    choice = int(input("Answer: "))

    if choice == 1:
        print(bye())
        quit()
    else:
        pass

def bye():
    print('')
    print('-'*30)
    print('Thank you for using MMU Sejahtera')
    print('-'*30)
    print('')

# 🔽 Main App -------------------------------------------------------------------

#data structure

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
    userdata = []

    if choice == 1:
        mainuserloop = True
        while mainuserloop == True:
            print('-' * 30) #menu2
            print('1) Sign Up For An Account')
            print('2) Log In')
            print('3) Return To Main Menu')
            print('-' * 30)
            print('')
            choice = int(input('Enter Your Choice: '))
            print('')

            if choice == 1:
                print('-' * 30)
                print('Sign Up To MMU MySejahtera')
                print('-' * 30)
                print('Please Enter Your Personal Information:')
                name = input('Name: ')
                age = input('Age: ')
                ic = input('ID: ')
                phone = input('Phone Number: ')
                post = input('Postcode: ')
                add = input('Address: ')
                pw = input('Password: ')
                user = [name, age, ic, phone, post, add, pw]
                userdata.append(user)
                print(user)
                print(userdata)
                print('')
                out()
                print('')

            elif choice == 2:
                #login process
                #login verification codes

                userloop = True
                while userloop == True:

                    hdata = []

                    print('-' * 30) #menu3
                    print('Welcome To MMU MySejahtera')
                    print('-' * 30)
                    print('1) Update Medical Information')
                    print('2) Check For Vaccination Appointment')
                    print('3) User Main Menu')
                    print('')
                    choice = int(input('Enter Your Choice:'))
                    print('')

                    if choice == 1: #update medical info
                        print('-'*20)
                        print('Health Information And Occupation Info')
                        print('-'*20)
                        print('')
                        print('Kindly Provide Your Medical History by typing "Y" or "N"') 
                        print('1) Do you have cardiovascular diseases?')
                        q1 = input('Answer: ') 
                        q1=q1.lower()
                        print('')
                        print('2) Do you have diabetes?')
                        q2 = input('Answer: ') 
                        q2=q2.lower()
                        print('')
                        print('3) Do you have chronic respiratory disease?')
                        q3 = input('Answer: ') 
                        q3=q3.lower()
                        print('')
                        print('4) Do you have chronic lung disease?')
                        q4 = input('Answer: ') 
                        q4=q4.lower()
                        print('')
                        print('5) Do you have chronic kidney disease?')
                        q5 = input('Answer: ') 
                        q5=q5.lower()
                        print('')
                        print('6) Do you have asthma?')
                        q6 = input('Answer: ') 
                        q6=q6.lower()
                        print('')
                        print('7) Do you have obesity?')
                        q7 = input('Answer: ') 
                        q7=q7.lower()
                        print('')
                        print('8) Do you have hyper-tension?')
                        q8 = input('Answer: ') 
                        q8=q8.lower()
                        print('')
                        print('9) Do you have cancer?')
                        q9 = input('Answer: ') 
                        q9=q9.lower()
                        print('')
                        print('10) Do you work in one of these occupations catagories?')
                        print('')
                        print('- Health-care worker')
                        print('- Community services')
                        print('- Energy')
                        print('- Food and transportation workers')
                        print('- Students')
                        occ = input('Answer: ')
                        occ=occ.lower()
                        print('')

                        hdata = [q1,q2,q3,q4,q5,q6,q7,q8,q9,occ] # list of health and occupation data info of the user.

                        status = 'Low Risk'

                        for i in hdata: #auto catagories status risk
                            if i == 'y':
                                status = 'High Risk'
                                break

                        hdata.append(status) # hdata = [q1,q2,q3,q4,q5,q6,q7,q8,q9,occ,status] (advanced feature q\1)
                        
                        print(f'You are {status} of contracting COVID-19.')
                        print('')
                        #print(hdata)
                        out()
                        print('')


                    elif choice == 2: #check appointment
                        print('-'*30)
                        print('COVID-19 Vaccine Appointment')
                        print('-'*30)
                        print('')
                        #print(f'Dear {userdata[i][0]}, your COVID-19 vaccine appointment details are as below:')
                        #print(f'Date: {}')
                        #print(f'Time: {}')
                        #print(f'Appointment Location: {}')
                        print('Would you be able to attend your appointment as scheduled? Kidly answer with "Y" for yes or "N" for no')
                        ans = (input('Enter Your Answer : '))
                        print('')
                        hdata.append(ans) #hdata = [q1,q2,q3,q4,q5,q6,q7,q8,q9,status,occ,ans]
                        out()
                        print('')

                    else:
                        userloop = False
            else:
                if choice == 3:
                    mainuserloop = False
                    print('')
                else:
                    print('Please Enter A Valid Choice.')


    elif choice == 2:
        mainadminloop = True
        while mainadminloop == True:
            print('-' * 30) #menu2
            print('1) Sign Up For An Account')
            print('2) Log In')
            print('3) Return To Main Menu')
            print('-' * 30)
            print('')
            choice = int(input('Enter Your Choice: '))
            print('')

            if choice == 1:
                print("Bruh.")
            elif choice == 2:
                #login process
                #login verification codes


                #important stuff
                vclistfull=[] #all vaccine center
                listappoinment=[]# list appoinment in specific vc
                appoinment=[]# all appoinment
                firstbatch=[]# this four is appoinment priorities
                secbatch=[]
                thirdbatch=[]
                fourtbatch=[]

                #start admin interface
                while True:
                    print("1. Continue")
                    print("2. Exit")

                    action=int(input("What do you want to do?"))
                    if action==1:
                        print("1. Create New Vaccination Center")
                        print("2. Check appoinment")
                        print("3. Sort users")
                        print("4. Assign appoinment")
                        print("5. Finished appoinment")
                        print("6. Check vaccine center appoinment")
                            
                        dowhat=int(input("What do you want to do? : "))




                        #Vaccine center creation2
                        #add vaccianation center


                        vclist=[]  #new vaccine center
                        if dowhat==1:                                                
                            name_vc=input("Vaccination Center Name : ")
                            locate_vc=  input(" Location : ")
                            capacity_vc= int(input(" Capacity per Hour : "))
                            vclist.append(name_vc)
                            vclist.append(locate_vc)
                            vclist.append(capacity_vc)
                            print(vclist)
                            vclistfull.append(vclist)
                            print(vclistfull)

                            
                        # check appoinment
                        elif dowhat==2:
                            checkapp=input("Please type in your name?")
                            for a in appoinment:
                                if [1] in a==checkapp:
                                    print(a)
                                else:
                                    print("Users not registered.")



                        #Sorting users
                        elif dowhat==3:
                            print(' 1. Postcode' )
                            print(' 2. Age ')
                            print(' 3. Covid-19 Status')
                            print(' 4. Group')
                            print(' 5. Priority')
                            dowhat2=int(input(" Sort by : "))
                            if dowhat2==1:
                                postuser=userdata.sort(key=[5])
                                print(postuser)
                                if dowhat2==2:
                                    ageuser=userdata.sort(key=[2])
                                    print(ageuser)
                                    if dowhat2==3:
                                        covuser=userdata.sort(key=[4])
                                        print(covuser)
                                        if dowhat==4:
                                            gruser=userdata.sort(key=[5])
                                            print(gruser)
                                            if dowhat2==5:
                                                pruser=userdata.sort(key=[6])
                                                print(pruser)  
                        

                        #assign appointmnet
                        elif dowhat==4:
                            vacp=firstbatch[1]
                            if firstbatch==[]:
                                vacp=secbatch[1]
                            elif secbatch==[]:
                                    vacp=thirdbatch[1]
                            elif thirdbatch==[]:
                                    vacp=fourtbatch[1]
                            else:
                                print("No user. All vaccinated ;).")
                                print(vacp)
                                vaccenter=input("Please input vaccination center : ")      
                                date= input("Please input date : ")
                                time= input("Please enter time : ") 
                            
                                appoinmentpersonal=[]

                                appoinmentpersonal.append(vacp)
                                appoinmentpersonal.append(vaccenter)
                                appoinmentpersonal.append(date)
                                appoinmentpersonal.append(time)

                                appoinment.append(appoinmentpersonal)


                        #delete appoinment
                        elif dowhat==5:  

                            print (appoinment)
                            deletevacp= input(" Delete first appoinment in list? :")
                            if deletevacp=="y" :
                                appoinment.remove(1)
                            elif deletevacp=="n":
                                pass
                            else:
                                print("invalid no.")


                        #List appoinmnet

                        elif dowhat==6:
                            checkvc=input(" Which vaccination center? : ")
                            for f in vclistfull:
                                if checkvc==f:
                                    for l in appoinment:
                                        for u in l:
                                            if u==checkvc:
                                                listappoinment.append(l)
                                                listappoinment.sort(key=[2])
                                                print (listappoinment)
                                            else:
                                                print('No one here :( ')
                                else:
                                    print('Vaccination center not registered.')

                            

                        #wrong no. for dowhat
                        else:
                            print("invalid no.")
                    
                    elif action==2:
                        break
                    else:
                        print("invalid no.")

            else:
                if choice == 3:
                    mainadminloop = False
                    print('')
                else:
                    print('Please Enter A Valid Choice.')                     
               
    else:
        bye()
        quit()







