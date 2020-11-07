#!/usr/bin/env python
# coding: utf-8

#     ATM_MACHINE USING PYTHON

# In[2]:


import time

print("Please insert Your CARD")

#Time taken for card processing in seconds

time.sleep(5)

password = 1234

#taking atm pin from user

pin = int(input("enter your atm pin "))

#user account balance

balance = 10000

#checking pin is valid or not 

if pin == password:
    
    #loop will run user get free
    
    while True:

        #Showing info to user

        print(""" 
   1 --> balance
   2 --> withdraw balance
   3 --> deposit balance
   4 --> exit
         """)

        try:    
             #taking an option from user
                
            option = int(input("Please enter your choice "))
        except:
            print("Please enter valid option")
        
        #for option 1  
        
        if option == 1:
            print(f"Your current balance is {balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount "))

            

            balance = balance - withdraw_amount

            print("{} is debited from your account".format(withdraw_amount))

            

            print("your current balance is {}".format(balance))

            

        if option == 3:

            deposit_amount = int(input("please enter deposit amount "))

            balance = balance + deposit_amount

            

            print("{} is credited to your account".format(deposit_amount))



            print(f"your current balance is {balance}")



        if option == 4:

            break


else:
    print("wrong pin, Please try again")


# In[ ]:




