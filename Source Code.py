#TEO KAI YII TANG KAR LOK
#TP058618    TP060733
from datetime import datetime
#car
def ask_car_id (variable_name, instruction):
    while(True): 
        variable_name = input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction)

        file_car = open("car.txt", "r") #open car file to read

        if len(variable_name) == 0:
            print("==============================================\nCar ID is required !\n==============================================") 
        elif len(variable_name) != 3:
            print("==============================================\nCar ID should be in 3 character\n==============================================") 
        elif variable_name in file_car.read():
            print("==============================================\nCar ID unavailable ! \nPlease choose another ID\n==============================================") 
            file_car.close()
        else:
            break
    return variable_name

def ask_car_name (variable_name, instruction):
    while(True):
        variable_name = input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction)
        if len(variable_name) == 0:
            print("==============================================\nName required!\n==============================================") 
        else:
            break
    return variable_name

def ask_car_description (variable_name, instruction):
    while(True):
        variable_name = input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction)
        if len(variable_name) == 0:
            print("==============================================\nDescription required!\n==============================================")
        else:
            break  
    return variable_name

def ask_car_seat (variable_name, instruction):
    while(True):
        try:
            variable_name = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction))
            if variable_name not in range(2,11):
                print("==============================================\nPlease enter approriate number of seats\n==============================================")
            else:
                break
        except ValueError:
            print("==============================================\nOnly numbers allowed!\n==============================================")
            continue
    return variable_name

def ask_car_price (variable_name, instruction):
    while(True):
        try:
            variable_name = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction))
            if len(str(variable_name)) == 0:
                print("==============================================\nDaily Price required!\n==============================================")
            elif variable_name < 100:
                print("==============================================\nMinimum RM100\n==============================================")
            else:
                break
        except:
            print("==============================================\nOnly whole numbers allowed!\n==============================================")
            continue
 
    return variable_name

#snack
def ask_snack_name(variable_name, instruction):
    while (True):
        variable_name = input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction)
        if len(variable_name) == 0:
            print("==============================================\nSnack Name required!\n==============================================")
        else:
            break    
    return variable_name

def ask_snack_price(variable_name, instruction):
    while(True):
        try:
            variable_name = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction))
            if variable_name not in range(1, 10):
                print("==============================================\nPrice in RM 1 to RM9 !\n==============================================")    
            else:
                break 
        except:
            print("==============================================\nOnly whole numbers allowed!\n==============================================")    
            continue   
    return variable_name

#common
def view_mode(option, item):
    while(True):
        try:
            print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            option = int(input("Which mode would you like to view "+item+"?"+"\n1: All \n2: Price(Low-High)\n3: Price(High-Low)\n4: Latest\nOption: "))
            if option in range(1,5):
                break
            else:
                print("==============================================\nOnly option 1 to option 4 is available!\n==============================================") 
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================")    
            continue
    return option

def ask_quantity (variable_name, instruction):
    while(True):
        try:
            variable_name = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction))
            if variable_name < 1:
                print("==============================================\nMinimum one quantity\n==============================================")
            else:
                break
        except:
            print("==============================================\nOnly numbers allowed!\n==============================================")
            continue

    return variable_name

def update_file(file_name,list):
    with open(file_name, "w") as file_name:
        i = 0
        while (i< len(list)):
            detail = "\t".join(list[i])
            file_name.write(detail+"\n")
            i += 1 

def ask_index(index_num,limit,num):
    while(True):
        index_num = 0
        try:
            index_num = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter field number to be modify: "))
            if index_num not in range(1,limit):
                print("==============================================\nOnly option 1 to option "+num+" is available!\n==============================================") 
            else:
                break
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
            continue
    return index_num

def get_file_details(file,list):
    list = []
    with open(file,"r") as file_snack:
        for each in file_snack:
            each_details = each.strip().split("\t")
            list.append(each_details)
    return list

def user_exist():
    while (True):

        #get customer details
        user_details = []
        user_details = get_file_details("user.txt",user_details)

        #name input
        name = str(input("===================\nPlease enter name\nName:"))

        #check name existence
        for each_customer in user_details:
            customer_name = each_customer[0]
            if name == customer_name:
                name_check = True
                break
            else:
                name_check = False
            
        if len(name) == 0:
            print("==============================================\nPlease enter your name\n==============================================") 
        elif name_check:
            print("==============================================\nUser exist!\n==============================================") 
            break
        else:
            print("==============================================\nUser not found ! Please re-enter again !\n==============================================") 
    return name

def ascending(list,num):
    for j in range(0, len(list)-1):
        swapped = False #used to stop loop when all element are arranged
        for i in range(0, len(list)-1):
            if int(list[i][num]) > int(list[i+1][num]):
                swap = list[i] #store i in swap first
                list[i] = list[i+1] #store i+1 to i
                list[i+1]= swap #store swap(which is i previously) to i+1 
                swapped = True
        if not swapped:
            break
    return list

def descending(list,num):
    for j in range(0, len(list)-1): 
        swapped = False #used to stop loop when all element are arranged
        for i in range(0, len(list)-1):
            if int(list[i][num]) < int(list[i+1][num]):
                swap = list[i] #store i in swap first
                list[i] = list[i+1] #store i+1 to i
                list[i+1]= swap #store swap(which is i previously) to i+1 
                swapped = True
        if not swapped:
            break
    return list

def latest(list):
    i = 0
    length = len(list)
    for i in range(0, length//2):  #use // so no remainder
        swap = list[i]              #swap each item with the mirror position
        list[i] = list[length-i-1]  #first and last, second and the one before
        list[length-i-1] = swap     
    return list

def day_month():
    #day
    while (True):
        try:
            day = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nDay(DD): "))
            if day not in range(1,32):
                print("==============================================\nPlease enter an appropriate day\n==============================================") 
            else:
                break
        except:
            print("==============================================\nPlease enter according to the format given\n==============================================") 
            continue
    
    #month
    while (True):
        try:
            month = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nMonth(MM): "))
            if month not in range(1,13):
                print("==============================================\nPlease enter an appropriate month\n==============================================") 
            else:
                break
        except:
            print("==============================================\nPlease enter according to the format given\n==============================================") 
            continue

    return day, month

#booking
def ask_rental_date():
    isValidate = False
    while isValidate == False:
        
        day, month = day_month()

        #year
        while (True):
            try:
                year = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nYear(YYYY): "))
                if len(str(year)) != 4:
                    print("==============================================\nPlease enter an appropriate year\n==============================================") 
                elif year not in range(2021, 2025):
                    print("==============================================\nYou can only book a car 3 years before\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nPlease enter according to the format given\n==============================================") 
                continue
        
        #hour
        while (True):
            try:
                hour = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nHour(HH): "))
                if hour not in range(8,23):
                    print("==============================================\nPlease enter an appropriate time in 24-hr format\nOnly 8:00 to 22:59 is allowed\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nPlease enter according to the format given\n==============================================") 
                continue

        #minutes
        while (True):
            try:
                minutes = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nMinutes(MM): "))
                if minutes not in range(0,60):
                    print("==============================================\nPlease enter an appropriate time\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nPlease enter according to the format given\n==============================================") 
                continue

        #start date
        start_date = str(year)+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(minutes)

        #validate 
        rental_start_date = 0
        while(True):
            try:
                rental_start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
                isValidate = True
                break
            except ValueError:
                isValidate = False

            #flag
            if not isValidate:
                print("==============================================\nInvalid Date or Time ! Please re-enter\n==============================================") 
                break

    return rental_start_date

#payment
def payment(total):
    print(" -------------------- | PAYMENT SESSION STARTED | -------------------- \n")
    print("{ The total amount to be paid is RM",total,"}\n\nKindly fill up the following details:\n")
  
    payment_date = datetime.today().strftime('%Y-%m-%d')

    print("=================================\nPlease choose a payment method:")

    payment_method = ["Pay In Cash","Credit Card","Debit Card", "Online Banking"]

    #show payment method
    for i in range(0,4):
        i += 1
        str(i)
        print(i,"->",payment_method[i-1])
        if i == 4:
            break

    while(True):
        try:
            payment_method = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nPayment Method: "))
            #check valid  user input
            if len(str(payment_method)) == 0:
                print("==============================================\nPayment Method required!\n==============================================") 
            elif payment_method not in range(1,5):
                print("==============================================\nPlease choose an available option!\n==============================================") 
            elif payment_method in range(1, 5):
                break
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
            continue

    if payment_method == 1:
        payment_method = "Pay In Cash"
    elif payment_method == 2:
        payment_method = "Credit Card"
    elif payment_method == 3:
        payment_method = "Debit Card"
    elif payment_method == 4:
        payment_method = "Online Banking"
    payment_status = "Paid"

    return payment_status,payment_date,payment_method

#user
def ask_name(variable_name,instruction):
    while(True):
    #user input
        variable_name = input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction)
    
        file_user = open("user.txt","r") #open admin file to read

        if len(variable_name) == 0: #check if customer has enter name
            print("==============================================\nPlease enter your name! \nName is required!\n==============================================") 

        elif variable_name in file_user.read(): #check if name already exist in the file
            print("==============================================\nName unavailable ! Please choose another name\n==============================================") 
            file_user.close() #close the file
        else:
            break
    return variable_name  

def ask_gender(variable_name,instruction):
    while(True):
        #user input
        variable_name = str(input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction))

        if len(variable_name) == 0: #check if customer has enter gender
            print("==============================================\nPlease provide your gender!\n==============================================") 
        elif variable_name != "M" and variable_name !="F":  #check format
            print("==============================================\nProvide gender with\n\"M\" as Male \n\"F\" as Female.\n==============================================") 
        else:
            break
    return variable_name

def ask_phone(variable_name,instruction):
    while(True):
        try:
            #user input
            variable_name = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction))
            if len(str(variable_name)) != 9: #restrict phone number to 9 digit
                print("==============================================\nPlease enter your phone number in 9 digit\n==============================================") 
            else:
                break
        except: #only allow number to be input
            print("==============================================\nPlease enter your phone number\n==============================================") 
            continue
        #End If
    #End of Loop
    return variable_name

def ask_email(variable_name,instruction):
    while(True):
        #user input
        variable_name = str(input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction))

        #check is it an email
        if "@" not in variable_name:
            print("==============================================\nPlease enter an appropriate email address\n==============================================") 
        elif "." not in variable_name:
            print("==============================================\nPlease enter an appropriate email address\n==============================================")    
        elif "mail" not in variable_name:
            print("==============================================\nPlease enter an appropriate email address\n==============================================")               
        else:
            break
        #End If
    #End of Loop
    return variable_name

def ask_password(instruction1, instruction2):
    while(True):
        #user input
        password = input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction1)
        
        if len(password) < 8: #check password length
            print("==============================================\nPassword should be at least 8 character\n==============================================") 
        else:
            #confirm password
            confirm_pwd = input(" >< >< >< >< >< >< >< >< >< >< >< >< \n"+instruction2)
            
            if confirm_pwd != password: #check if password match
                print("==============================================\nPassword does not match! \nPlease re-enter your password:") 
            else:
                break
            #End If
        #End If
    #End of Loop
    return confirm_pwd

def ask_birthday():
    isValidate = False
    while isValidate == False:
        
        day, month = day_month()

        #year
        while (True):
            try:
                year = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nYear(YYYY): "))
                if len(str(year)) != 4:
                    print("==============================================\nPlease enter an appropriate year\n==============================================") 
                elif year not in range(1956, 1999):
                    print("==============================================\nOnly 23 to 65 years old is allowed!\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nPlease enter according to the format given\n==============================================") 
                continue

        #start date
        dob = str(year)+"-"+str(month)+"-"+str(day)

        #validate 
        birthday = 0
        while(True):
            try:
                birthday = datetime.strptime(dob, "%Y-%m-%d")
                isValidate = True
                break
            except ValueError:
                isValidate = False

            #flag
            if not isValidate:
                print("==============================================\nInvalid Date ! Please re-enter\n==============================================") 
                break

    return birthday

#main functions
def log_out():
    print(" -------------------- | LOG OUT SESSION STARTED | -------------------- \n")


    while(True):
        option = 0
        try:
            print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            option = int(input("Do you wish to log out? Please choose an option\n1: Yes\n2: No\nOption: "))     
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 

        if option not in range(1,3):
            print("==============================================\nOnly option 1 and option 2 is available!\n==============================================") 
        else:
            break

    if option == 1:
        print("* * * * * * * * * * * * * * * * * * * * * Thank you for coming! Hope to see you soon ! * * * * * * * * * * * * * * * * * * * * * ")
    elif option == 2:
        print("=============================================\nApproaching to the welcome page ...")
        welcome()
        return

def who_register():
    who_register = 0
    while(True):
        try:
            #user input
            print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            who_register = int(input("What is your role? Please choose an option\n1: Customer\n2: Admin\n3: Exit\nOption: "))
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================")   
        #check valid  user input
        if who_register not in range(1,4):
            print("==============================================\nOnly option 1 to option 3 is available !\n==============================================") 
        else:
            break
    if who_register == 3:
        log_out()
    return who_register

def welcome():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("-------------------- | WELCOME TO SUPER CAR RENTAL SERVICES (SCRS) ! | --------------------\n")
    print("\nWe are glad that you are here !\n")

    while(True): #ask user login/register
        option = 0
        try:
            print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
            option = int(input("Do you have an account? Please choose an option\n1: Yes\n2: No\n3: Exit\nOption: "))  
            if option not in range(1,4):
                print("==============================================\nOnly option 1 to option 3 is available!\n==============================================") 
            else:
                break
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
            continue

    if option == 1:
        
        while(True):
            option = 0
            try:
                print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                option = int(input("Do you want to login now? Please choose an option\n1: Login\n2: Exit\nOption: "))
                if option not in range(1,3):
                    print("==============================================\nOnly option 1 to option 3 is available!\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
                continue
        
        if option == 1:
            user_type = who_register()
            if user_type == 1:
                customer_login()
            elif user_type == 2:
                admin_login()
        else:
            log_out()

    elif option == 2:

        while(True):
            option = 0
            try:
                print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                option = int(input("Do you want to register an account now?\n1: Register now\n2: View all cars available for rent\n3: Exit\nOption: "))
                if option not in range(1,4):
                    print("==============================================\nOnly option 1 to option 3 is available!\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
                continue

        if option == 1:
            user_type = who_register()
            if user_type == 1:
                customer_register()
            elif user_type == 2:
                admin_register()

        elif option == 2:
            guest_available_car()

        elif option == 3:
            log_out()
    else:
        log_out()
    return

def menu_admin():
    print(" -------------------- | ADMIN FEATURES MENU | -------------------- \n\nWelcome to the Admin Features Menu !\n")
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("What would you like to do?\n")
    print(" 1. Modify Personal Details")
    print(" 2. Modify Car Details")
    print(" 3. Modify Snacks & Drinks Details")
    print(" 4. Add Cars To Be Rented Out")
    print(" 5. Add Snacks & Drinks To Be Sold")
    print(" 6. View Cars Rented Out")
    print(" 7. View Cars Available For Rent")
    print(" 8. View Customer Bookings")
    print(" 9. View Customer Payment")
    print("10. View Available Snacks & Drinks")
    print("11. Search Customer Booking")
    print("12. Search Customer Payment")
    print("13. Return Rented Car")
    print("14. Exit ")

    while(True):
        option = 0
        try:
            option = int(input("==============================================\nPlease choose an option\nOption:"))
            if option not in range(1,15):
                print("==============================================\nOnly option 1 to option 14 is available!\n==============================================") 
            else:
                break
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
            continue

    if option == 1:
        modify_admin_details()
    elif option == 2:
        modify_car()
    elif option == 3:
        modify_snacks()
    elif option == 4:
        insert_car()
    elif option ==5:
        insert_snacks()
    elif option ==6:
        admin_rented_car()
    elif option ==7:    
        admin_available_car()
    elif option ==8:
        view_booking()
    elif option ==9:
        view_payment()
    elif option ==10:
        admin_snacks()
    elif option ==11:
        admin_search_booking()
    elif option ==12:
        search_payment()
    elif option ==13:
        return_car()
    elif option ==14:
        log_out()
    return

def admin_continue():        
    answer = 1
    while(True):
            try:
                print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                #user input
                answer = int(input("Do you want to continue? Please choose an option\n1: Yes\n2: View Admin Features Menu\n3: Exit\nOption: "))
                #check valid  user input
                if answer not in range(1,4):
                    print("==============================================\nOnly option 1 to option 3 is available !\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nInvalid! Only number is allowed!\n==============================================")    
                continue

    if answer == 2:
        menu_admin()
    elif answer == 3:
        log_out()
    return answer

def menu_customer():
    print(" -------------------- | FEATURES MENU | -------------------- \n\nWelcome to the Features Menu !\n")
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("What would you like to do?\n1: Modify Personal Details\n2: View Personal Rental History\n3: View Details Of Available Car\n4: Place A Booking\n5: Exit\n")
    while(True):
        option = 0
        try:
            option = int(input("==============================================\nPlease choose an option\nOption:"))
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 

        if option not in range(1,6):
            print("==============================================\nOnly option 1 to option 5 is available!\n==============================================") 
        else:
            break
    if option == 1:
        modify_customer_details()
    elif option == 2:
        cus_search_booking()
    elif option == 3:
        cus_available_car()
    elif option == 4:
        place_booking()
    elif option ==5:
        log_out()
    return

def customer_continue():        

    answer = 1
    while(True):
            try:
                print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                #user input
                answer = int(input("Do you want to continue? Please choose an option\n1: Yes\n2: View Features Menu\n3: Exit\nOption: "))
                #check valid  user input
                if answer not in range(1,4):
                    print("==============================================\nOnly option 1 to option 3 is available !\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nInvalid! Only number is allowed!\n==============================================")    
                continue
    if answer == 2:
        menu_customer()
    elif answer == 3:
        log_out()
    return answer

#view snack
def show_snacks():
    print(" -------------------- |  VIEW SNACKS & DRINKS | -------------------- \n")

    option = 0
    option = view_mode(option,"snack and drinks") #call function
        
    snack_details = [] #define list
    snack_details = get_file_details("snack.txt", snack_details)

    snack_details  = [each_snack for each_snack in  snack_details if len(each_snack[1]) > 3] #take required snack from list without creating a new list
    
    if option == 1:#All
        print("======================== ` View mode: All ` =======================") 

        #Arrange ascending according to ID
        for j in range(0, len(snack_details)-1):
            swapped = False
            for i in range(0, len(snack_details)-1):
                if snack_details[i][0][1:3] > snack_details[i+1][0][1:3]:
                    swap = snack_details[i] #store i in swap first
                    snack_details[i] = snack_details[i+1] #store i+1 to i
                    snack_details[i+1]= swap #store swap(which is i previously) to i+1 
                    swapped = True
            if not swapped:
                break

    elif option == 2: #Low to high
        print("=========== ` View mode: Sort by Price (Low to High) ` ============") 
        #Arrange ascending according to price
        snack_details = ascending(snack_details,2)
    
    elif option == 3: #high to low
        print("=========== ` View mode: Sort by Price (High to Low) ` ============") 
        #Arrange desscending according to price
        snack_details = descending(snack_details,2)
    
    elif option == 4:#Latest
        print("======================= ` View mode: Latest ` =====================")
        #reverse
        snack_details = latest(snack_details)

    print("-------------------------------------------------------------------")
    print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` | DRINKS | ` $ ` $ ` $ ` $ ` $ ` $ ` $")
    print("-------------------------------------------------------------------")
    print("ID"+"\t"+"Price"+"\t"+"Quantity"+"\t"+"Drinks")
    print("-------------------------------------------------------------------")
    
    num = 0
    for each_snack in snack_details:
        if each_snack[0][0] == "D":
            print(each_snack[0]+"\t"+"  "+each_snack[2]+"\t"+"  "+each_snack[3]+"\t\t"+each_snack[1])
            num += 1
        elif num == len(snack_details):
            break

    print("-------------------------------------------------------------------")
    print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` | SNACKS | ` $ ` $ ` $ ` $ ` $ ` $ ` $")
    print("-------------------------------------------------------------------")
    print("ID"+"\t"+"Price"+"\t"+"Quantity"+"\t"+"Snacks")
    print("-------------------------------------------------------------------")

    num = 0
    for each_snack in snack_details:
        if each_snack[0][0] == "S":
            print(each_snack[0]+"\t"+"  "+each_snack[2]+"\t"+"  "+each_snack[3]+"\t\t"+each_snack[1])
            num += 1
        elif num == len(snack_details):
            break

    print("-------------------------------------------------------------------")
    return

def admin_snacks():
    answer = 1
    while answer == 1:
        show_snacks()
        answer = admin_continue()
    return

def customer_snacks():
    answer = 1
    while answer == 1:
        show_snacks()
        answer = customer_continue()
    return

#view booking
def order_snack():
    print(" -------------------- | SNACKS & DRINKS ORDER SESSION STARTED | -------------------- ")
    print("Snacks and Drinks will be provided in the car when you come to collect the car")
    print("~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ")

    answer = 1
    snack_total = 0
    snack_cost = 0
    while(True):
        try:
            answer = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nDo you need any snacks and drinks? Please choose an option\n1. Yes\n2. No\nOption:"))
            if answer not in range(1,3):
                print("==============================================\nOnly option 1 and 2 is allowed\n==============================================") 
            else: 
                break
        except:
            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
            continue

    while answer == 1:

        #define variables
        booking_name = ""
        order_snack_id = ""
        order_quantity = ""
        rental_start_date = ""
        index = 0

        # customer name
        booking_name = user_exist()

        #call function
        show_snacks()

        #get snack details
        snack_details = []
        snack_details = get_file_details("snack.txt",snack_details)

        print("~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ")
        print("Which snack or drink would you like to order?")

        while(True):#search car by ID
            #get user input
            order_snack_id = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter Snack ID to order:")

            #check and display car details
            not_found = True
            for all_snack in snack_details:
                #split information with a space into list
                index += 1
                if order_snack_id == all_snack[0]:
                    print("========================== ` Snacks Details ` ==========================") 
                    print("Snack ID: ", all_snack[0])
                    print("1: Name:",all_snack[1])
                    print("2: Price:",all_snack[2])
                    print("3: Quantity:",all_snack[3])
                    print("========================================================================") 
                    not_found = False
                    break
            index = index - 1
            if not_found:
                print("==============================================\nSnack or Drink is not found !\n==============================================") 
            else:
                break

        #quantity
        print("~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ `")
        print("How many would you like to order ? ")
        order_quantity = ask_quantity(order_quantity,"Quantity: ")

        #total price
        for i in range(index, index+ 1):
            snack_cost = 0
            snack_cost = int(all_snack[2])*int(order_quantity)
            snack_total += snack_cost

        print("~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~")
        print("When is your car rental start date and time ? ")
        rental_start_date = ask_rental_date()
        rental_start_date = str(rental_start_date)
        rental_start_date = rental_start_date[:16]

        #store snack order
        file_snack = open("snack.txt", "a")
        file_snack.write(booking_name+"\t"+order_snack_id+"\t"+str(order_quantity)+"\t"+str(rental_start_date)+"\n") 
        file_snack.close()

        #decrease quantity
        updated_list = []
        with open("snack.txt","r") as file_snack:
            for each_snack in file_snack: 
                all_snack = each_snack.strip().split("\t") #split info into list
                if order_snack_id == all_snack[0]: 
                    while(True):
                        all_snack[3] = int(all_snack[3])-order_quantity  # minus quantity
                        all_snack[3] = str(all_snack[3])
                        break
                updated_list.append(all_snack) #append all info to list

        #update the file
        update_file("snack.txt",updated_list)

        print("~ ` ~ ` ~ ` ~ ` ~ Snacks ordered successfully! ~ ` ~ ` ~ ` ~ ` ~")


        while(True):
            try:
                #user input
                print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                answer = int(input("Do you want to continue? Please choose an option\n1: Yes\n2: No\nOption: "))
                #check valid  user input
                if answer not in range(1,3):
                    print("==============================================\nOnly option 1 and option 2 is available !\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nInvalid! Only number is allowed!\n==============================================")     
                continue

        if answer == 2:
            break

    return snack_total

def view_booking():
    print(" -------------------- | BOOKINGS | -------------------- \n")
    answer = 1
    while answer == 1:

        option = 0
        option = view_mode(option, "bookings")
        
        booking_details = [] #define list
        booking_details = get_file_details("booking.txt",booking_details)

        #get snack
        snack_details = []
        snack_details = get_file_details("snack.txt",snack_details)

        snack_details  = [each_snack for each_snack in  snack_details if len(each_snack[0]) > 3] #take required value from list without creating a new list

        if option == 1:#All
            print("======================================== ` View mode: All ` ========================================") 

        elif option == 2: #Low to high
            print("======================== ` View mode: Sort by Total Amount (Low to High) ` =========================") 

            #Arrange ascending according to price
            booking_details = ascending(booking_details,7)

            #Arrange ascending according to quantity
            snack_details = ascending(snack_details,2)
        
        elif option == 3: #high to low
            print("======================== ` View mode: Sort by Total Amount (High to Low) ` =========================") 

            #Arrange ascending according to price
            booking_details = descending(booking_details,7)

            #Arrange ascending according to quantity
            snack_details = descending(snack_details,2)
        
        elif option == 4:#Latest
            print("================================ ` View mode: Show Latest Bookings ` ===============================") 

            booking_details = latest(booking_details)

            snack_details = latest(snack_details)

        print("----------------------------------------------------------------------------------------------------")
        print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` | BOOKINGS | ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $")
        print("----------------------------------------------------------------------------------------------------")
        print("Car ID"+"\t"+"Days"+"\t"+"Rental Start Date"+"\t"+"Payment Status"+"\t"+"Total Amount(RM)"+"\t"+"Name")
        print("----------------------------------------------------------------------------------------------------")

        num = 0
        for each_booking in booking_details:
            print(each_booking[1]+"\t"+" "+each_booking[2]+"\t"+each_booking[3]+"\t"+" "+each_booking[5]+"\t"+"   "+each_booking[7]+"\t\t\t"+each_booking[0])
            num += 1
            if num == len(booking_details):
                break

        print("\n----------------------------------------------------------------------------------------------------")
        print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` | SNACKS & DRINKS | ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $")
        print("----------------------------------------------------------------------------------------------------")
        print("ID"+"\t"+" "+"Quantity"+"\t"+"Rental Start Date"+"\t"+"Name")
        print("----------------------------------------------------------------------------------------------------")

        num = 0
        for each_snack in snack_details:
            print(each_snack[1]+"\t"+"    "+each_snack[2]+"\t\t"+each_snack[3]+"\t"+each_snack[0])
            num += 1
            if num == len(snack_details):
                break
        print("----------------------------------------------------------------------------------------------------\n")
        answer = admin_continue()
    return

def view_payment():
    print(" -------------------- | PAYMENT | -------------------- \n")

    answer = 1
    while answer == 1:
        option = 0
        option = view_mode(option, "payments")

        booking_details = []  #define list
        booking_details = get_file_details("booking.txt",booking_details)

        if option == 1:#All
            print("======================================== ` View mode: All ` ========================================") 


        elif option == 2: #Low to high
            print("======================== ` View mode: Sort by Payment Amount (Low to High) ` =========================") 

            #Arrange ascending according to price
            booking_details = ascending(booking_details,7)

        elif option == 3: #high to low
            print("======================== ` View mode: Sort by Payment Amount (High to Low) ` =========================") 

            #Arrange descending according to price
            booking_details = descending(booking_details,7)
        

        elif option == 4:#Latest
            print("================================ ` View mode: Show Latest Payment ` ===============================") 

            #reverse list
            booking_details = latest(booking_details)

        num = 0
        print("----------------------------------------------------------------------------------------------------")
        print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` | PAYMENT | ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $")
        print("----------------------------------------------------------------------------------------------------")
        print("Payment Status"+"\t"+"Payment Date"+"\t"+"Payment Amount(RM)"+"\t"+"Payment Method"+"\t\t"+"Name")
        print("----------------------------------------------------------------------------------------------------")

        num = 0
        for each_booking in booking_details:
            print("    "+each_booking[4]+"\t"+" "+each_booking[5]+"\t\t"+each_booking[7]+"\t\t"+each_booking[6]+"\t\t"+each_booking[0])
            num += 1
            if num == len(booking_details):
                break
        print("----------------------------------------------------------------------------------------------------")
        answer = admin_continue()
    return

#view car
def available_car():
    print("--------------------- | VIEW AVAILABLE CARS | ---------------------\n")

    option = 0
    option = view_mode(option,"available cars for rent")

    car_details = [] #define list
    car_details = get_file_details("car.txt",car_details)
    
    #remove car from list without creating a new list
    car_details  = [each_car for each_car in  car_details if int(each_car[5]) > 0]

    if option == 1: #All
        print("======================== ` View mode: All ` =======================") 

    elif option == 2: #Low to high
        print("============ ` View mode: Sort by Price (Low to High) ` ===========") 

        #Arrange ascending according to price
        car_details = ascending(car_details,4)    

    elif option == 3: #high to low
        print("============ ` View mode: Sort by Price (High to Low) ` ===========")  

        #Arrange descending according to price
        car_details = descending(car_details,4) 
    
    elif option == 4:#Latest
        print("================== ` View Mode: Show Latest Cars ` ================")  

        #reverse the list
        car_details = latest(car_details) 

    num = 0 #define variable
    print("-------------------------------------------------------------------")
    print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` | CARS | ` $ ` $ ` $ ` $ ` $ ` $ ` $")
    print("-------------------------------------------------------------------")
    print("Car ID"+"\t"+"Seats"+"\t"+"Price"+"\t"+"Name"+"\t\t"+"Description")
    print("-------------------------------------------------------------------")

    for each_car in car_details:
        print(each_car[0]+"\t"+" "+each_car[3]+"\t"+each_car[4]+"\t"+each_car[1]+"\t"+each_car[2])
        num += 1
        if num == len(car_details):
            break

    print("-------------------------------------------------------------------")
    return

def cus_available_car():
    answer = 1
    while answer == 1:
        available_car()
        answer = customer_continue()
    return

def admin_available_car():
    answer = 1
    while answer == 1:
        available_car()
        answer = admin_continue()
    return

def rented_car():
    print(" --------------------------------- |  VIEW RENTED CARS | --------------------------------- \n")
    
    option = 0
    option = view_mode(option, "rented cars")

    car_details = [] #define list
    car_details = get_file_details("car.txt",car_details)
    
    #remove not rented cars
    car_details  = [each_car for each_car in  car_details if int(each_car[6]) > 0] #remove car from list without creating a new list

    if option == 1:#All
        print("===================================== ` View mode: All ` ====================================") 

    elif option == 2: #Low to high
        print("========================= ` View mode: Sort by Price (Low to High) ` ========================") 

        #Arrange ascending according to price
        car_details = ascending(car_details,4)

    elif option == 3: #high to low
        print("========================= ` View mode: Sort by Price (High to Low) ` ========================") 

        #Arrange descending according to price
        car_details = descending(car_details,4)

    elif option == 4:#Latest
        print("============================== ` View Mode: Show Latest Cars ` ==============================") 
        
        #reverse list
        car_details = latest(car_details)

    num = 0
    print("----------------------------------------------------------------------------------------------")
    print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` | CARS | ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ")
    print("----------------------------------------------------------------------------------------------")
    print("Car ID"+"\t"+"Seats"+"\t"+"Price"+"\t"+"Name"+"\t\t"+"Description"+"\t"+"Quantity Available"+"\t"+"Quantity Rented")
    print("----------------------------------------------------------------------------------------------")

    for each_car in car_details:
        print(each_car[0]+"\t"+" "+each_car[3]+"\t"+each_car[4]+"\t"+each_car[1]+"\t"+each_car[2]+"\t\t"+each_car[5]+"\t\t"+"    "+each_car[6])
        num += 1
        if num == len(car_details):
            break

    print("----------------------------------------------------------------------------------------------")
    return

def admin_rented_car():
    answer = 1
    while answer == 1:
        rented_car()
        answer = admin_continue()
    return

def return_car():
    print(" -------------------- | RETURN RENTED CAR SESSION STARTED | -------------------- \n\nKindly fill up the following details:\n")

    answer = 1
    while answer == 1:

        rented_car() #call function

        updated_list = []
        car_details = []
        car_details = get_file_details("car.txt",car_details)

        #get user input
        search_car = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter Car ID to return a rented car:")

        #check and display car details
        not_found = True
        for all_car in car_details:
            if search_car == all_car[0]:
                print("Car ID: ", all_car[0])
                print("1: Name:",all_car[1])
                print("2: Description:",all_car[2])
                print("3: Number Of Seats:",all_car[3],"seater")
                print("4: Daily Price: RM",all_car[4])
                print("5: Quantity:",all_car[5])
                all_car[5] = int(all_car[5])+1  #add quantity
                all_car[6] = int(all_car[6])-1  #minus rented quantity
                all_car[5] = str(all_car[5])
                all_car[6] = str(all_car[6])
                not_found = False
            updated_list.append(all_car) #append all car details 
        
        #if car not found
        if not_found:
            print("==============================================\nCar is not found !\n==============================================")
            continue
        else:
            update_file("car.txt",updated_list)
        print("~ ` ~ ` ~ ` ~ ` ~ Rented Car Return successfully! ~ ` ~ ` ~ ` ~ ` ~")
        answer = admin_continue()
    return

#user features
def modify_customer_details():
    print(" -------------------- | MODIFY PERSONAL DETAILS SESSION STARTED | -------------------- \nKindly fill up the following details:")

    answer = 1 
    while answer == 1:
        modified_list = []
        with open("user.txt","r") as file_user:
            #get user input
            search_name = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter your name to modify personal details:")

            #check and display customer_details
            not_found = True
            for each_customer in file_user:
                #split information with a space into list
                all_customer = each_customer.strip().split("\t")
                if all_customer[2] != "Admin" and search_name == all_customer[0]:
                    print("========================== ` Personal Details ` ==========================") 
                    print("Name:",all_customer[0])
                    print("1: Gender:",all_customer[1])
                    print("2: Date Of Birthday:",all_customer[2])
                    print("3: Phone number: (+60)",all_customer[3])
                    print("4: Email Address:",all_customer[4])
                    print("5: Password:",all_customer[5])
                    print("==========================================================================") 
                    not_found = False

                    #user input
                    while(True):
                        index_num = 0
                        index_num = ask_index(index_num,6,5)
                        break

                    while(True):
                        print("Existing information in field is: ", all_customer[index_num])
                        #gender
                        if index_num == 1:
                            all_customer[index_num] = ask_gender(all_customer[index_num], "Enter new gender:")
                            break
                            
                        #DOB
                        elif index_num == 2:
                            all_customer[index_num] = ask_birthday()
                            all_customer[index_num] = str(all_customer[index_num])
                            all_customer[index_num] = all_customer[index_num][:10]
                            break

                        #phone
                        elif index_num == 3:
                            all_customer[index_num] = ask_phone(all_customer[index_num], "Enter new phone number (+60):")
                            all_customer[index_num] = str(all_customer[index_num])
                            break

                        #email
                        elif index_num == 4:
                            all_customer[index_num] = ask_email (all_customer[index_num], "Enter new email address:")
                            break

                        #password
                        elif index_num == 5:
                            all_customer[index_num]  = ask_password("Enter new password:", "Confirm password: ")
                            all_customer[index_num]  = str(all_customer[index_num])
                            break

                modified_list.append(all_customer) #append all customer details
                
            #if name not found
            if not_found:
                print("==============================================\nName is not found !\n==============================================")
                continue 
            else:
                update_file("user.txt",modified_list)

        print("~ ` ~ ` ~ ` ~ ` ~ Personal details successfully updated ! ~ ` ~ ` ~ ` ~ ` ~")
        answer = customer_continue()
    return

def modify_admin_details():
    print(" -------------------- | MODIFY PERSONAL DETAILS SESSION STARTED | -------------------- \nKindly fill up the following details:")

    answer = 1 
    while answer == 1:
        modified_list = []
        with open("user.txt","r") as file_user:
            #get user input
            search_name = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter your name to modify personal details:")

            #check and display customer_details
            not_found = True
            for each_admin in file_user:
                #split information with a space into list
                all_admin = each_admin.strip().split("\t")
                if all_admin[2] == "Admin" and search_name == all_admin[0]:
                    print("========================== ` Personal Details ` ==========================") 
                    print("Name:",all_admin[0])
                    print("1: Gender:",all_admin[1])
                    print("2: Phone number: (+60)",all_admin[3])
                    print("3: Email Address:",all_admin[4])
                    print("4: Password:",all_admin[5])
                    print("==========================================================================") 
                    not_found = False

                    #user input
                    while(True):
                        index_num = 0
                        try:
                            index_num = int(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter field number to be modify: "))
                            if index_num not in range(1,5):
                                print("==============================================\nOnly option 1 to option 4 is available!\n==============================================") 
                            else:
                                if index_num in range(2,5):
                                    index_num = index_num + 1
                                break
                        except:
                            print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
                            continue

                    while(True):
                        print("Existing information in field is: ", all_admin[index_num])
                        #gender
                        if index_num == 1:
                            all_admin[index_num] = ask_gender(all_admin[index_num], "Enter new gender:")
                            break

                        #phone
                        elif index_num == 3:
                            all_admin[index_num] = ask_phone(all_admin[index_num], "Enter new phone number (+60):")
                            all_admin[index_num] = str(all_admin[index_num])
                            break

                        #email
                        elif index_num == 4:
                            all_admin[index_num] = ask_email (all_admin[index_num], "Enter new email address:")
                            break

                        #password
                        elif index_num == 5:
                            all_admin[index_num]  = ask_password("Enter new password:", "Confirm password: ")
                            all_admin[index_num]  = str(all_admin[index_num])
                            break

                modified_list.append(all_admin) #append all admin details

        #if name not found
        if not_found:
            print("==============================================\nName is not found !\n==============================================")
            continue 
        else:
            update_file("user.txt",modified_list)

        print("~ ` ~ ` ~ ` ~ ` ~ Personal details successfully updated ! ~ ` ~ ` ~ ` ~ ` ~")
        answer = admin_continue()
    return

def login():
    print("-------------------- |LOGIN SESSION STARTED !|--------------------\nKindly fill up the following details:")

    #get admin details
    user_details = []
    user_details = get_file_details("user.txt",user_details)

    #admin name
    user_exist()   
    return user_details

def customer_login():
    user_details = login()

    # customer password
    while (True):

        #password input
        login_password = str(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nPassword:"))

        #check password existence
        for each_customer in user_details:
            customer_password = each_customer[5]
            if login_password == customer_password:
                password_check = True
                break
            else:
                password_check = False   
        #validation     
        if len(login_password) == 0:
            print("==============================================\nPlease enter your password\n==============================================") 
        elif password_check:
            print("~ ` ~ ` ~ ` ~ ` ~ Succesfully Logged in! Welcome back! ~ ` ~ ` ~ ` ~ ` ~")
            print("======================================\nApproaching Features Menu")
            menu_customer()
            break
        else:
            print("==============================================\nPassword wrong! \nPlease re-enter your password again\n==============================================") 
    return    
                
def admin_login():
    user_details = login()
    # admin password
    while (True):

        #password input
        login_password = str(input(" >< >< >< >< >< >< >< >< >< >< >< >< \nPassword:"))

        #check password existence
        for each_admin in user_details:
            admin_password = each_admin[5]
            if login_password == admin_password:
                password_check = True
                break
            else:
                password_check = False
        #validation
        if len(login_password) == 0:
            print("==============================================\nPlease enter your password\n==============================================") 
        elif password_check:
            print("~ ` ~ ` ~ ` ~ ` ~ Succesfully Logged in! Welcome back! ~ ` ~ ` ~ ` ~ ` ~")
            print("======================================\nApproaching Admin Features Menu")
            menu_admin()
            break
        else:
            print("==============================================\nPassword wrong! \nPlease re-enter your password again\n==============================================") 
    return 

def admin_register():
    print(" -------------------- | REGISTER SESSION STARTED | -------------------- \nKindly fill up the following details:")
    admin = "Admin"

    while(True):#while loop for the file

        #define variables
        name = 0
        gender = 0
        phone = 0
        email = 0
        confirm_pwd = 0

        file_user = open("user.txt","a")  #open new file when no file
        file_user.close

        #get admin input

        #name
        name = ask_name(name,"Name: ")

        #gender
        gender = ask_gender( gender,"Gender(M/F): ")

        #phone
        phone = ask_phone(phone,"Phone number: (+60)")

        #email
        email = ask_email(email,"Email Address:")

        #password & confirm password
        confirm_pwd = ask_password("Password: ","Confirm Password: ")
        
        file_user = open("user.txt","a") #open user file in append mode
        file_user.write(str(name)+"\t"+gender+"\t"+admin+"\t"+str(phone)+"\t"+email+"\t"+str(confirm_pwd)+"\n")  #insert admin details
        file_user.close() #close the file

        print("~ ` ~ ` ~ ` ~ ` ~ Registration successfully completed! ~ ` ~ ` ~ ` ~ ` ~") #user registered sucessfully
        print("==============================================\nApproaching login session ...")
        admin_login()
        break
    return

def customer_register():
    print(" -------------------- | REGISTER SESSION STARTED | -------------------- \nKindly fill up the following details:")
    
    while(True):

        #define variables
        name = 0
        gender = 0
        birthday = 0
        phone = 0
        email = 0
        confirm_pwd = 0

        file_user = open("user.txt","a") #open new file when no file
        file_user.close

        #get customer input

        #name
        name = ask_name(name,"Name: ")

        #gender
        gender = ask_gender( gender,"Gender(M/F): ")

        #birthday
        print("Date Of Birth: ")
        birthday = ask_birthday()
        birthday = str(birthday)
        birthday = birthday[:10]

        #phone
        phone = ask_phone(phone,"Phone number: (+60)")

        #email
        email = ask_email(email,"Email Address:")

        #password & confirm password
        confirm_pwd = ask_password("Password: ","Confirm Password: ")

        file_user = open("user.txt", "a") #open user file in appennd mode
        file_user.write(str(name)+"\t"+gender+"\t"+str(birthday)+"\t"+str(phone)+"\t"+email+"\t"+str(confirm_pwd)+"\n") #insert customer details
        file_user.close() #close the file

        print("~ ` ~ ` ~ ` ~ ` ~ Registration successfully completed! ~ ` ~ ` ~ ` ~ ` ~") #user registered sucessfully
        print("==============================================\nApproaching login session ...")
        customer_login()
        break
    return #End function

def guest_available_car():
    answer = 1
    while answer == 1:
        available_car()

        #user input
        while(True):
            answer = 0
            try:
                print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                answer = int(input("Do you want to register an account to place booking ?\n1: Continue to view all cars available for rent\n2: Register now\n3: Exit\nOption: "))
                if answer not in range(1,4):
                    print("==============================================\nOnly option 1 to option 3 is available!\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nInvalid! Only number is allowed!\n==============================================") 
                continue
        if answer == 2:
            customer_register()
        elif answer ==3:
            log_out()
    return

#customer features
def place_booking():
    print(" -------------------- | BOOKING SESSION STARTED | -------------------- \nKindly fill up the following details:")

    answer = 1
    while answer == 1:

        #define variables
        booking_name = 0
        booking_car = ""
        booking_day = ""
        rental_start_date = ""
        index = 0

        # customer name
        booking_name = user_exist()

        #call function
        available_car()

        #get car details
        car_details = []
        car_details = get_file_details("car.txt",car_details)

        print("~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~")
        print("Which car would you like to book?")
        while(True):#search car by CarID
            #get user input
            booking_car = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter Car ID to book:")

            #check and display car details
            not_found = True
            for all_car in car_details:
                if booking_car == all_car[0]:
                    print("========================== ` Car Details ` ==========================") 
                    print("Car ID: ", all_car[0])
                    print("1: Name:",all_car[1])
                    print("2: Description:",all_car[2])
                    print("3: Number Of Seats:",all_car[3],"seater")
                    print("4: Daily Price: RM",all_car[4])
                    print("5: Quantity:",all_car[5])
                    print("=====================================================================") 
                    not_found = False
                    break
            #if car not found
            if not_found:
                print("==============================================\nCar is not found !\n==============================================") 
            else:
                break

        print("~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~")
        print("How many days would you like to book ?")

        while(True):#no of day
            try:
                booking_day = int(input("Day: "))
                if len(str(booking_day)) == 0:
                    print("==============================================\nPlease enter how many days would you like to book\n==============================================") 
                elif booking_day not in range(1, 29):
                    print("==============================================\nMaximum 28 days are allowed!\n==============================================") 
                else:
                    break
            except:
                print("==============================================\nOnly numbers allowed!\n==============================================") 
                continue

        #total price
        for i in range(index, index+ 1):
            car_total = int(all_car[4])*int(booking_day)

        print("~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ ` ~ `  ~ ` ~ ` ~ ` ~")
        print("When do you want to start you car rental ?\nPlease provide date and time ")
        rental_start_date = ask_rental_date()
        rental_start_date = str(rental_start_date)
        rental_start_date = rental_start_date[:16]
        
        snack_total = order_snack() #call function to order snack
        payment_amount = car_total + snack_total
        payment_status , payment_date, payment_method = payment(car_total) #call function to make payment

        #store booking info
        file_booking = open("booking.txt", "a") #open file to insert values
        file_booking.write(booking_name+"\t"+booking_car+"\t"+str(booking_day)+"\t"+str(rental_start_date)+"\t"+payment_status+"\t"+payment_date+"\t"+payment_method+"\t"+str(payment_amount)+"\n")
        file_booking.close()#close booking file
        
        #increase rented quantity
        updated_list = [] #define list
        for all_car in car_details: 
            if booking_car == all_car[0]: 
                while(True):
                    all_car[5] = int(all_car[5])-1  #quantity - 1
                    all_car[6] = int(all_car[6])+1  #rented + 1
                    all_car[5] = str(all_car[5])
                    all_car[6] = str(all_car[6])
                    break
            updated_list.append(all_car) #append all info to list

        #update the file
        update_file("car.txt",updated_list)

        print("~ ` ~ ` ~ ` ~ ` ~ Booking placed successfully! ~ ` ~ ` ~ ` ~ ` ~")
        answer = customer_continue()
    return

def search_personal_history(name):
    print(" -------------------- | "+name+" | -------------------- \nKindly fill up the following details:")
    # customer name
    search_name = user_exist()
    
    #booking details
    booking_details = [] #open booking file
    booking_details = get_file_details("booking.txt",booking_details)

    booking_details  = [each_booking for each_booking in  booking_details if each_booking[0] == search_name] #take required booking from list without creating a new list

    view_car = []
    for each_booking in booking_details:
        view_car.append(each_booking[1]) #store rental car history in a list

    print("--------------------------------------------------------------------")
    print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` | BOOKINGS | ` $ ` $ ` $ ` $ ` $ ` $ ` $")
    print("--------------------------------------------------------------------")
    print("Car ID"+"\t"+"Days"+"\t"+"Rental Date"+"\t\t"+"Amount(RM)"+"\t"+"Payment Date")
    print("--------------------------------------------------------------------")

    num = 0
    for each_booking in booking_details:
        if each_booking[0] == search_name:
            print(each_booking[1]+"\t"+" "+each_booking[2]+"\t"+each_booking[3]+"\t"+" "+each_booking[7]+"\t\t"+each_booking[5])
            num += 1
        elif num == len(booking_details):
            break

    #car details
    car_details = []
    car_details = get_file_details("car.txt",car_details)

    print("\n-------------------------------------------------------------------")
    print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` | CARS | ` $ ` $ ` $ ` $ ` $ ` $ ` $` $")
    print("-------------------------------------------------------------------")
    print("Car ID"+"\t"+"Seats"+"\t"+"Price"+"\t"+"Name"+"\t\t\t"+"Description")
    print("-------------------------------------------------------------------")

    num , i= 0 , 0
    for each_car in car_details:  
        for i in range(len(view_car)):
            if view_car[i] == each_car[0]:
                print(each_car[0]+"\t"+" "+each_car[3]+"\t"+each_car[4]+"\t"+each_car[1]+"\t\t"+each_car[2])
                i += 1
        num += 1
        if num == len(car_details):
            break

    #get snack
    snack_details = []
    snack_details = get_file_details("snack.txt",snack_details)

    snack_details  = [each_snack for each_snack in  snack_details if each_snack[0] == search_name] #take required snack from list without creating a new list
    
    view_snack = []
    view_quantity = []
    for each_snack in snack_details:
        view_snack.append(each_snack[1]) #store snack in a list
        view_quantity.append(each_snack[2])

    #snack details
    snack_details = []
    snack_details = get_file_details("snack.txt",snack_details)

    print("\n-------------------------------------------------------------------")
    print("$ ` $ ` $ ` $ ` $ ` $ ` | SNACKS & DRINKS | ` $ ` $ ` $ ` $ ` $ ` $")
    print("-------------------------------------------------------------------")
    print("ID"+"\t"+"Price"+"\t"+" "+"Quantity"+"\t"+"Item")
    print("-------------------------------------------------------------------")

    num, i = 0, 0
    for each_snack in snack_details:
        for i in range(len(view_snack)):
            if view_snack[i] == each_snack[0]:
                print(each_snack[0]+"\t"+"  "+each_snack[2]+"\t"+"   "+view_quantity[i]+"\t\t"+each_snack[1])
                i += 1
        num += 1
        if num == len(snack_details):
            break
    print("-------------------------------------------------------------------\n")
    return

def cus_search_booking():
    answer = 1
    while answer == 1:
        search_personal_history("PERSONAL RENTAL HISTORY SESSION STARTED")
        answer = customer_continue()
    return

#admin features
def insert_car():
    print(" -------------------- | INSERT CAR SESSION STARTED | -------------------- \nKindly fill up the following details:")    
    answer = 1
    while answer == 1:

        #define variables
        car_id = ""
        name = ""
        description = ""
        seat = ""
        daily_price = ""
        quantity = ""
        rented = 0
        
        file_car = open("car.txt","a") #create new file when no file
        file_car.close #close file

    #admin insert details
        #car id
        car_id = ask_car_id(car_id,"Car ID: ")
        
        #name
        name = ask_car_name(name, "Name: ")
        
        #description
        description = ask_car_description(description,"Description: ")    

        #number of seats
        seat = ask_car_seat(seat, "Number Of Seats:")    

        #daily price
        daily_price = ask_car_price(daily_price, "Daily Price: RM")         

        #quantity
        quantity = ask_quantity(quantity, "Quantity: ")         
            
        
        file_car = open("car.txt", "a") #open car file to append
        file_car.write(car_id+"\t"+name+"\t"+description+"\t"+str(seat)+"\t"+str(daily_price)+"\t"+str(quantity)+"\t"+str(rented)+"\n") #insert values
        file_car.close() #close car file
        print("Car information successfully updated! ") 
        answer = admin_continue()
    return

def modify_car():
    print(" -------------------- | MODIFY CAR SESSION STARTED | -------------------- \n")
    
    answer = 1
    while answer == 1:
        modified_list = []
        with open("car.txt","r") as file_car:
            available_car()  #View cars
            #get user input
            search_car = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter Car ID to modify car details:")

            #check and display car details
            not_found = True
            for each_car in file_car:
                #split information with a space into list
                all_car = each_car.strip().split("\t")
                if search_car == all_car[0]:
                    print("============================ ` Car Details ` ============================") 
                    print("Car ID: ", all_car[0])
                    print("1: Name:",all_car[1])
                    print("2: Description:",all_car[2])
                    print("3: Number Of Seats:",all_car[3],"seater")
                    print("4: Daily Price: RM",all_car[4])
                    print("5: Quantity:",all_car[5])
                    print("=========================================================================") 
                    not_found = False

                    #user input
                    while(True):
                        index_num = 0
                        index_num = ask_index(index_num,6,5)
                        break

                    #get new value
                    while(True):
                        print("Existing information in field is:",all_car[index_num])

                        #name
                        if index_num == 1:
                            all_car[index_num] = ask_car_name(all_car[index_num], "Enter new name: ")
                            break

                        #description
                        elif index_num == 2:
                            all_car[index_num] = ask_car_description(all_car[index_num],"Enter new description: ")
                            break

                        #number of seats
                        elif index_num == 3:
                            all_car[index_num] = ask_car_seat(int(all_car[index_num]),"Enter new number of seats:" )
                            all_car[index_num] = str(all_car[index_num])
                            break

                        #daily price
                        elif index_num == 4:
                            all_car[index_num] = ask_car_price(all_car[index_num], "Enter new daily price: RM")
                            all_car[index_num] = str(all_car[index_num])
                            break

                        #quantity
                        elif index_num == 5:
                            all_car[index_num] = ask_quantity(all_car[index_num], "Enter new quantity: ")
                            all_car[index_num] = str(all_car[index_num])
                            break
                
                modified_list.append(all_car) #append all car details to list
            
            #if car not found
            if not_found:
                print("==============================================\nCar is not found !\n==============================================") 
                continue 
            else:
                update_file("car.txt",modified_list)

        print("~ ` ~ ` ~ ` ~ ` ~ Car details successfully updated !!! ~ ` ~ ` ~ ` ~ ` ~")
        answer = admin_continue()
    return

def admin_search_booking():
    answer = 1
    while answer == 1:
        search_personal_history("SEARCH BOOKINGS SESSION STARTED")
        answer = admin_continue()
    return

def search_payment(): 
    print(" -------------------- | SEARCH PAYMENT SESSION STARTED | -------------------- \nKindly fill up the following details: ")

    answer = 1
    while answer == 1:

        while(True): #search by which item
            option = 0
            try:
                print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                option = int(input("How would you like to search? Please choose an option \n1: Search by Name\n2: Search by Date\nOption: "))
                if option not in range(1,3):
                    print("Only option 1 and option 2 is available!")
                else:
                    break
            except:
                print("Invalid! Only number is allowed!")
                continue

        #get customer details
        user_details = []
        user_details = get_file_details("user.txt",user_details)

        #booking details
        booking_details = [] #open booking file
        booking_details = get_file_details("booking.txt",booking_details)

        if option == 1:
            # customer name
            search_name = user_exist()

            #get specific booking from list without creating a new list
            booking_details  = [each_booking for each_booking in  booking_details if each_booking[0] == search_name] 
        
        elif option ==2: #search by date

            while (True):
                search_date = 0 #define variable
                search_date = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter a date to search(YYYY-MM-DD):") #date input
          
                for each_booking in booking_details:
                    payment_date = each_booking[5] #check date existence
                    if search_date == payment_date: 
                        date_check = True
                        break
                    else:
                        date_check = False
                if len(search_date) == 0:
                    print("==============================================\nPlease enter a date\n==============================================") 
                elif date_check:
                    print("==============================================\nDate exist!\n==============================================") 
                    break
                else:
                    print("==============================================\nDate not found ! Please follow the format\nYYYY-MM-DD\n=============================================")
            #get specific booking from list without creating a new list
            booking_details  = [each_booking for each_booking in  booking_details if each_booking[5] == search_date] 

        print("---------------------------------------------------------------------------------------------------")
        print("$ ` $ ` $ ` $ ` $ ` $ ` $ ` $  ` $ ` $ ` $ ` | PAYMENT | ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ` $ ")
        print("---------------------------------------------------------------------------------------------------")
        print("Status"+"\t"+"Date"+"\t\t"+"Method"+"\t\t"+"Amount(RM)"+"\t"+"Name")
        print("---------------------------------------------------------------------------------------------------")

        num = 0
        for each_booking in booking_details:
            print(each_booking[4]+"\t"+each_booking[5]+"\t"+each_booking[6]+"\t"+"  "+each_booking[7]+"\t\t"+each_booking[0])
            num += 1
            if num == len(booking_details):
                break
        print("---------------------------------------------------------------------------------------------------")
        answer = admin_continue()
    return

def insert_snacks():
    print(" -------------------- | INSERT SNACKS & DRINKS SESSION STARTED | -------------------- \nKindly fill up the following details:")

    answer = 1
    while answer == 1:

        #define variables
        snack_id = ""
        snack = ""
        price = ""
        quantity = ""

        file_snack = open("snack.txt","a") #open new file when no file
        file_snack.close

        # snack id
        while (True):

            #get snack details
            snack_details = []
            snack_details = get_file_details("snack.txt",snack_details)

            #id input
            snack_id = str(input("Snack ID:"))

            id_check = False
            for each_snack in snack_details:
                id_snack = each_snack[0] #check id existence
                if snack_id == id_snack: 
                    id_check = True
                    break
                else:
                    id_check = False
            if len(snack_id) == 0:
                print("==============================================\nSnack ID required !\n==============================================") 
            elif len(snack_id) != 3:
                print("==============================================\nSnack ID should be in 3 characters\n==============================================") 
            elif not id_check:
                break
            elif id_check:
                print("==============================================\nSnack ID already exist!\n==============================================") 

        #snack
        snack = ask_snack_name(snack, "Snack: ")

        #price
        price = ask_snack_price(price,"Price: RM")

        #quantity
        quantity = ask_quantity(quantity,"Quantity: " )                 
        
        file_snack = open("snack.txt", "a") #open snack file      
        file_snack.write(str(snack_id)+"\t"+snack+"\t"+str(price)+"\t"+str(quantity)+"\n") #insert values
        file_snack.close() #close snack file
        print("~ ` ~ ` ~ ` ~ ` ~ Information successfully updated!  ~ ` ~ ` ~ ` ~ ` ~")
        answer = admin_continue()
    return

def modify_snacks():
    print(" -------------------- | MODIFY SNACKS & DRINKS SESSION STARTED | -------------------- \n")

    answer = 1
    while answer == 1:
        modified_list = []
        with open("snack.txt","r") as file_snack:
            show_snacks() #view snacks and drinks

            #user input
            search_snack = input(" >< >< >< >< >< >< >< >< >< >< >< >< \nEnter Snack ID to modify details:")

            #check and display car details
            not_found = True
            for each_snack in file_snack:
                #split information with a space into list
                all_snack = each_snack.strip().split("\t")
                if search_snack == all_snack[0]:
                    print("========================== ` Snacks Details ` ==========================") 
                    print("Snack ID: ", all_snack[0])
                    print("1: Name:",all_snack[1])
                    print("2: Price:",all_snack[2])
                    print("3: Quantity:",all_snack[3])
                    print("========================================================================") 
                    not_found = False

                    #user input
                    while(True):
                        index_num = 0
                        index_num = ask_index(index_num,4,3)
                        break

                    #get new value
                    while(True):
                        print("Existing information in field is:",all_snack[index_num])

                        #name
                        if index_num == 1:
                            all_snack[index_num] = ask_snack_name(all_snack[index_num], "Enter new name: ")
                            break

                        #price
                        elif index_num == 2:
                            all_snack[index_num] = ask_snack_price(all_snack[index_num],"Enter new price: ")
                            all_snack[index_num] = str(all_snack[index_num])
                            break

                        #quantity
                        elif index_num == 3:
                            all_snack[index_num] = ask_quantity(all_snack[index_num],"Enter new quantity:")
                            all_snack[index_num] = str(all_snack[index_num])
                            break
    
                modified_list.append(all_snack)
            
            #if car not found
            if not_found:
                print("==============================================\nSnack or Drink is not found !\n==============================================")
                continue 
            else:
                update_file("snack.txt",modified_list)
        
        print("~ ` ~ ` ~ ` ~ ` ~ Snacks & Drinks details successfully updated ! ~ ` ~ ` ~ ` ~ ` ~")
        answer = admin_continue()
    return

welcome()