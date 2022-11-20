#ATM Machine Project using Python

print("Welcome to SR ATM!")
start = "Please insert your Card"
print(start)
act_pin = 2005
enter_pin = int(input("Please enter your 4-digit secret pin: "))
min = 5000
Amt = 50000

if enter_pin == act_pin:
     print("Hello Mr.John")
     print("Your current balance is:",Amt)
     print('''
               CHOOSE YOUR SERVICE
          
          \t\t\tPRESS 1 to DEPOSIT Money
          \t\t\tPRESS 2 to WITHDRAW Money
          \t\t\tPRESS 3 for Balance Enquiry
          \t\t\tPRESS 4 to Change your ATM pin
          \t\t\tPRESS 5 for Fund Transfer
          ''')
     
     option = int(input("Select an option: "))
     if option == 1:
          print("Deposit Money into your Account")
          Dep = int(input("Enter the Amount: Rs. "))
          Amt+=Dep
          print("Please wait while Transaction is being processed")
          print("Amount is successfully deposited into your Bank Account")
          print("Total Balance after the transaction: Rs.",Amt)                                                                                                                                                                                               
          print("Thank you!\nVisit Again")
     elif option == 2:
          print("WITHDRAW WISHED AMOUNT")
          Wtd = int(input("Enter Amount: Rs."))
          Amt-=Wtd
          if Amt<min:
               print("Amount can't be withdrawn due to exceeding of Minimum Limit")
          else:
               print("Please wait while Transaction is being processed")
               print("Amount is successfully withdrawn from the Account")
               print("Total Balance after the transaction: Rs.",Amt)
               print("Thank you!\nVisit Again")
     elif option == 3:
          print("Please wait while Transaction is being processed")
          print("Current Balance: Rs.",Amt) 
          print("Thank you!\nVisit Again")
     elif option == 4:
          print("Change your ATM pin")
          new_pin = int(input("Enter your new Secret Pin: "))
          aga_new = int(input("Enter your new Secret Pin again: "))
          a = str(new_pin)
          b = str(aga_new)
          if len(a)==4 and len(b)==4 and a == b:
               print("Please wait while Transaction is being processed")
               print("Pin changed successfully")
          elif len(a) == 4  and len(b)==4 and a!=b:
               print("Entered pins are not matching\nPlease try again")
          elif len(a)!= 4 or len(b) != 4:
               print("Pin should contain 4 digits only\nPlease try again")
     elif option == 5:
          print("Transfer Fund")
          acc_num=int(input("Enter Payee's Account Number: "))
          tra = int(input("Enter Amount: "))
          
          Amt-=tra
          if Amt < min:
               print("Please wait while transaction is being processed")
               print("Fund Transfer has breached Minimum limit\nTransaction not possible\nThank You!")
          else:
               print("Please wait while Transaction is being processed")
               print("Amount is successfully transfered")
               print("Current Balance:",Amt)
               print("Thank you\nVisit again!")
     else:
          print("Please choose valid Service\nFor choosing Valid Service,Please start a new session")   
else:
     print("Wrong pin entered by the user\nPlease check and enter valid pin")