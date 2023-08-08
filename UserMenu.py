import csv
print(f"Welcome!")
print("How can we help you today?")
print("1.Enter/Update Medical history and Covid-19 status")
print("2.Check vaccination appointment details")
print("3.RSVP for assigned appointment")
Options=input("")
if Options=="1":
    import CovidStatus
elif Options=="2":
    import VacAppointment
elif Options=="3":
    VacAppointmentAttendance=input("Will you be attending your vaccination appointment? Y/N :")
    print("Thank you for your response.")

