
print("Welcome to Car Workshop Management System")   #Printing the name of system
def main():                                   #Defining the main function
    check="Y"                                 #Initializing the variable
    while check=="Y":                         #Applying while loop
        while True:                           #Applying while loop
            try:                              #Checking
                data=int(input("\n1)Workshop Record\n2)Customer Record\n3)Appointments\n4)Exit: ")) #Taking input from user  
                break                         #Loop ends
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if data==1:                           #If data is equal to 1
            Workshop_Record()                 #Call out the function of workshop records
            check="a"                         #changing the value of check
        elif data==2:                         #If data is equal to 2
            Customers_Record()                #Call out the function of Customer records
            check="a"                         #changing the value of check
        elif data==3:                         #If data is equal to 3
            Appointments()                    #Call out the function of Appointments
            check="a"                         #changing the value of check
        elif data==4:                         #If data is equal to 4
            print("Program Ends")             #Print this statement
            check="a"                         #changing the value of check
            break                             #Break the loop
        else:                                 #If data is equal to any number
            print("Invalid Input. Enter from the given choices")

def Workshop_Record():                        #Defining the Workshop record function
    check="Y"                                 #Initializing the variable
    while check=="Y":                         #Applying while loop
        while True:                           #Applying while loop
            try:                              #Checking
                data1=int(input("\n1)Add Records\n2)View Records\n3)Search Records\n4)Edit Records\n5)Delete Records\n6)Back: ")) #Taking input from user
                break                         #breaking the loop
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if data1==1:                          #If data1 is equal to 1
            Add_Workshop_records()            #Call out the function of add Workshop records
            break                             #breaks the loop
        elif data1==2:                        #If data1 is equal to 2
            View_Workshop_records()           #Call out the functio of view Workshop records
        elif data1==3:                        #If data1 is equal to 3
            Search_Workshop_records()         #Call out the function of search Workshop records
        elif data1==4:                        #If data1 is equal to 4
            Edit_Workshop_records()           #Call out the function of edit Workshop records
        elif data1==5:                        #If data1 is equal to 5
            Delete_Workshop_records()         #Call out the function of delete Workshop records
        elif data1==6:                        #If data1 is equal to 6
            main()                            #Call out the main function
            break                             #loop breaks
        else:                                 #If data1 is equal to any number
            print("Invalid Input. Enter from the given choices")

Workshop={}                                   #Creating empty dictionary
def Add_Workshop_records():                   #Defining add Workshop record function
    while True:                               #Applying while loop
        try:                                  #Checking
            ID =int(input("Enter phone number: " )) #Taking input from the user
            break                             #Loop braeks
        except:                               #Checking
            print("Enter Digits only")        #Print this statement
    if ID in Workshop.keys():                 #Cheking ID exist in keys of dictionary or not
        print("Already Exists. Please Enter another Phone Number") #If already exist print this statement
        Add_Workshop_records()                #Call out the funtion of add Workshop records
    else:                                     #If not exist
        while True:                           #Applying loop
            Name = input("Enter name: ")      #Taking input from user
            break                             #Loop breaks
        while True:                           #Applying loop
            Service=input("Enter the Type of Service: ") #Taking input from user
            break                             #Loop breaks
        while True:                           #Applying while loop
            Car_Number=input("Enter the car number(AAA-1111): ") #Taking input from the user
            break                             #Loop breaks
        while True:                           #Applying while loop
            Date=input("Enter the date(DD/MM/YYYY) on service been done: ") #Taking input from the user
            break                             #Loop breaks

        Workshop[ID]=[Name, Service, Car_Number, Date] #Appending attributes in dictionary
        option=input("Enter Yes to Add Further Record: ") #Taking input for entering further records or not
        if option=="Yes":                     #Applying condition                
            Add_Workshop_records()            #Calling out the function
        else:                                 #If option != Yes
            Workshop_Record()                   #Calling out the function
def View_Workshop_records():                     #Defining view Workshop record function
    if len(Workshop)>0:                          #Applying condition
        print("Phone number \tName    \tService    \tCar Number  \tDate") #Print this statement
        for k in Workshop.keys():                #Assigning ID's to k
            val=Workshop[k]                      #Assigning variable
            print(k,"\t", val[0],"\t", val[1],"\t", val[2],"\t", val[3]) #Print all records
    else:                                        #If condition id false
        print("Enter records first")             #Print this statement
def Search_Workshop_records():                   #Defining search Workshop record function
    if len(Workshop)>0:                          #Applying condition
        while True:                               #Applying while loop
            try:                                  #Checking
                ID = int(input("Enter phone number: ")) #Taking input fron the user
                break                             #Loop breaks
            except:                               #Checking
                print("Enter only digits")        #Print this statement
        if ID in Workshop.keys():                 #If id exist in keys of dictionary
            print("Phone number \tName    \tService    \tCar Number  \tDate") #Print this statement
            val=Workshop[ID]                      #Assigning ID's to k
            print(ID,"\t", val[0],"\t", val[1],"\t", val[2],"\t", val[3]) #Print records
        else:                                     #If condition is false
            print("Phone number not Found. Please Enter Correct Phone number to Search Records") #Print this statement
            Search_Workshop_records()             #Call out the function
    else:                                         #If condition is false
        print("Enter record first")               #Print this statement
def Edit_Workshop_records():                      #Defining the funtion of edit Workshop records
    if len(Workshop)>0:                           #Applying condition
        while True:                               #Applying while loop
            try:                                  #Checking
                ID =int(input("Enter phone number: ")) #Taking input fron the user
                break                             #Loop braeks
            except:                               #Checking
                print("Enter only digits")        #Print this statement
        if ID in Workshop.keys():                 #If id exist in keys of Workshop
            while True:                           #Applying loop
                Name = input("Enter name: ")      #Taking input from user
                break                             #Loop breaks
            while True:                           #Applying loop
                Service=input("Enter the Type of Service: ") #Taking input from user
                break                             #Loop breaks
            while True:                           #Applying while loop
                Car_Number=input("Enter the car number(AAA-1111): ") #Taking input from the user
                break                             #Loop breaks
            while True:                           #Applying while loop
                Date=input("Enter the date(DD/MM/YYYY) on service been done: ") #Taking input from the user
                break
            Workshop[ID]=[Name, Service, Car_Number, Date]
        else:
            print("Please enter correct phone number to edit record")
            Edit_Workshop_records()               #Call out the function
    else:                                         #If coditions false  
        print("Enter Record first")               #Print this statement
def Delete_Workshop_records():                    #Defining the function of delete Workshop records
    if len(Workshop)>0:                           #Applying condition
        while True:                               #Applying while loop
            try:                                  #Checking
                ID =eval(input("Enter phone number: ")) #Taking input fron the user
                break                             #Loop braeks
            except:                               #Checking
                print("Enter only digits")        #Print this statement
        if ID in Workshop.keys():                 #Applying condition
            del Workshop[ID]                      #Deleting id
            print("Deleted Successfully")         #Print this statement
        else:                                     #If coditions false
            print("Phone number not Found. Please enter correct Phone number for Delete Record") #Print this statement
            Delete_Workshop_records()             #Call out the function
    else:                                         #If coditions false
        print("Enter Record first")               #Print this statement

def Customers_Record():                       #Defining the Workshop record function
    check="Y"                                 #Initializing the variable
    while check=="Y":                         #Applying while loop
        while True:                           #Applying while loop
            try:                              #Checking
                data2=eval(input("\n1)Add Records\n2)View Records\n3)Search Records\n4)Edit Records\n5)Delete Records\n6)Back: ")) #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if data2==1:                          #If data 2 is equal to 1
            Add_Customers_records()           #Call out he function of add Customers records
            break                             #loop breaks
        elif data2==2:                        #If data 2 is equal to 2
            View_Customers_records()          #Call out the function of view Customers records
        elif data2==3:                        #If data 2 is equal to 3
            Search_Customers_records()        #Call out the function of search Customers records
        elif data2==4:                        #If data 2 is equal to 4
            Edit_Customers_records()          #Call out the function of edit Customers          
        elif data2==5:                        #If data 2 is equal to 5
            Delete_Customers_records()        #Call out the function of delete Customers records
        elif data2==6:                        #If data 2 is equal to 6
            main()                            #Call out the main function
            break                             #Loop breaks
        else:                                 #If coditions false
            print("Invalid Input. Enter from the given choices") #Print this statement
Customer={}                                   #Creating empty dictionary
def Add_Customers_records():                  #Defining function of add Customer records
    while True:                               #Applying while loop
        try:                                  #Checking
            PN =eval(input("Enter the Phone number of Customer: ")) #Taking input from the user
            break                             #Loop breaks
        except:                               #Checking
            print("Enter digits only")        #Print this statement
    if PN in Customer.keys():                 #If PN exist in keys of dictionary
        print("Already Exists. Please Enter another Phone number") #Print this statement
        Add_Customer_records()                #Call out the function of add Customer records
    else:                                     #If PN does not exist
        while True:                           #Applying while loop
            Name=input("Enter the name of Customer: ") #Taking input from the user
            break                             #Loop breaks
        while True:                           #Applying while loop
            Car_Number=input("Enter the car number(AAA-1111): ") #Taking input from the user
            break                             #Loop breaks
        while True:                           #Applying loop
            Service=input("Enter the Type of Service: ") #Taking input from user
            break                             #Loop breaks
        while True:                           #Applying loop
            Car_name=input("Enter the Car name: ") #Taking input from the user
            break                             #Loop breaks
        Customer[PN]=[Name,Car_Number,Service,Car_name]     #Append attributes in dictionary
        option=input("Enter Yes to Add Further Record: ")#Taking input from the user for futher records
        if option=="Yes":                     #Applying condition                    
            Add_Customers_records()           #Call out the function of add Customer records
        else:                                 #If coditions false
            Customers_Record()                #Call out the function of Customer records
def View_Customers_records():                 #Defining the function of view Customer records
    if len(Customer)>0:                       #Applying condition for printing records
        print("Phone Number\tName     \tCar Number    \tPast Service    \tCar Name")      #Print this statement
        for k in Customer.keys():             #Assigning ID's to k
            val=Customer[k]                   #Assigning variable
            print(k,"\t",val[0],"\t",val[1],"\t",val[2],"\t",val[3]) #Print all records
    else:                                     #If coditions false
        print("Enter the record first")       #Print this statement
def Search_Customers_records():               #Defining the function of search Customer records
    if len(Customer)>0:                       #Applying condition for printing records
        while True:                           #Applying while loop
            try:                              #Checking
                PN =eval(input("Enter Phone number for search records: ")) #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if PN in Customer.keys():             #Applying condition              
            print("Phone Number\tName     \tCar Number    \tPast Service    \tCar Name")  #Print this statement
            val=Customer[PN]                  #Assigning Variable
            print(PN  ,"\t",val[0],"\t",val[1],"\t",val[2],"\t",val[3]) #Print all records
        else:                                 #If coditions false
            print("Please Enter correct Phone number for search records") #Print this statement
            Search_Customers_records()         #Call out the function of search Customer records
    else:                                     #If coditions false
        print("Enter records first")          #Print this statement
def Edit_Customers_records():                 #Defining the function of edit Customer records
    if len(Customer)>0:                       #Applying condition
        while True:                           #Applying while loop
            try:                              #Checking
                PN=eval(input("Enter the Phone number: ")) #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if PN in Customer.keys():             #If PN exist in keys of dictionary
            while True:                       #Applying while loop
                Name=input("Enter the name of Customer: ") #Taking input from the user
                break                         #Loop breaks
            while True:                       #Applying while loop
                Car_Number=input("Enter the car number(AAA-1111): ") #Taking input from the user
                break                         #Loop breaks
            while True:                       #Applying loop
                Service=input("Enter the Type of Service: ") #Taking input from user
                break                         #Loop breaks
            while True:                       #Applying loop
                Car_name=input("Enter the Car name: ")
                break
            Customer[PN]=[Name,Car_Number,Service,Car_name]     #Append attributes in dictionary
        else:                                 #If coditions false
            print("Please Enter correct Phone number to edit records") #Print this statement
            Edit_Customers_records()          #Call out the function of edit Customer records
    else:                                     #If coditions false
        print("Enter Records first")          #Print this statement
def Delete_Customers_records():               #Defining the function of delete Customer records
    if len(Customer)>0:                       #Applying condition
        while True:                           #Applying while loop
            try:                              #Checking
                PN=eval(input("Enter Phone number for delete records: ")) #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if PN in Customer.keys():             #If PN exist in dictionary
            del Customer[PN]                  #Delete key and attributes
            print("Deleted Successfully")     #Print this statement
        else:                                 #If coditions false
            print("Enter the correct phone number for delete records") #Print this statement
            Delete_Customers_records()        #Call out the function of delete Customer records
    else:                                     #If coditions false
        print("Enter the record first")       #Print this statement
Available_slots = {1:"9:30 AM - 10:30 AM", 2:"10:30 AM - 11:00 AM", 3:"11:00 AM - 11:30 AM", 4:"11:30 AM - 12:00PM", 5:"12:00 PM - 12:30PM", 6:"1:00 PM - 1:30PM"}
Appointment={} 
def Appointments():                           #Defining the function of Appointments
    check="Y"                                 #Initializing the variable
    while check=="Y":                         #Applying while loop
        while True:                           #Applying while loop
            try:                              #Checking
                data3=int(input("\n1)Add Appointments\n2)View Appointments\n3)Back: ")) #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if data3==1:                          #If input is equal to 1
            Add_Appointments()                #Call out the function of add Appointments
        elif data3==2:                        #If input iss equal to 2
            View_Appointments()               #Call out the function of view Appointments
        elif data3==3:                        #If input is equal to 3
            main()                            #Call out the main function
            break                             #Loop breaks
        else:                                 #If input is equal to any value
            print("Invalid Input. Enter from given choices") #Print this statement
            Appointments()                    #Call out the function of Appointments
                                              #Creating empty dictionary
def Add_Appointments():                   #Defining function of add Appointmentss
    while True:                           #Applying while loop
        try:                              #Checking
            ID = int(input("Enter Phone number for Appointments: ")) #Taking input from the user
            break                         #Loop breaks
        except:                           #Checking
            print("Enter Digits only")    #Print this statement
  
    if len(Available_slots) == 0:
        print("No Time is available. Please come again later. Sorry fo the inconvenince") #Print this statement
    else:
        print("Slot number\tAvailable time")
        for k in Available_slots.keys():            #Assigning ID's to k
            val=Available_slots[k]                  #Assigning variable
            print(k,"\t","\t",Available_slots.get(k))
             
        x = int(input("Enter the slot number in which you want to book an appointment: "))
        
        while True:                           #Applying while loop
            try:                              #Checking
                Name=input("Enter the name of Customer: ") #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter alphabets only")
        while True:                           #Applying while loop
            try:                              #Checking
                Car_Number=input("Enter the car number(AAA-1111): ") #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter like this (AAA-1111)")
        while True:                           #Applying while loop
            Service=input("Enter the Type of Service: ") #Taking input from user
            break                             #Loop breaks
        while True:                           #Applying while loop
            try:                              #Checking
                Date=input("Enter the date(DD/MM/YYYY): ") #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter like this (DD/MM/YYYY)")
        while True:                           #Applying while loop
            Time_slot=Available_slots[x]
            break                             #Loop breaks
        print(Time_slot, "is your slot now please check appointments by your phone number")
        Appointment[ID]=[Name,Car_Number,Service,Date,Time_slot]
        del Available_slots[x]                #Deleting the selected slot from the dictionary
        option=input("Enter Yes to Add Further Record: ")#Taking input from the user for futher records
        if option=="Yes":                         #Applying condition                    
            Add_Appointments()                    #Call out the function of add appointments
        else:                                     #If coditions false
            main()                                #Call out the main function
def View_Appointments():                          #Defining funtion of view Appointmentss
    if len(Appointment)>0:                        #Applying condition for printing records
        print("Phone number\tName\tService \tCar number\tDate\tTime slot")#Print this statement
        for k in Appointment.keys():              #Applying loop for printing the records
            val=Appointment[k]                    #Determining the index of key
            print(k,"\t",val[0],"\t",val[1],"\t",val[2],"\t",val[3],"\t",val[4])#Print all records
    else:                                         #If coditions false
        print("No Record is Available")           #Print this statement


main()                                            #Call out the main funtion

