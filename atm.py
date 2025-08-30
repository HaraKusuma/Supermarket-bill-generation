name="Ramya"
password="123"

user_name=input("Enter the Username:")
password_in=input("Enter the Password:")
s='''
    1.Credit
    2.Debit
    3.Mini Statement
    4.Exit
    '''
Amount=1000
if name.lower()==user_name.lower() and password==password_in:
    while True:
        print(s)
        option=int(input("Enter your choice:"))
        if option==1:
            credit_amt=float(input("Enter the amount to be credited:"))
            print("Amount after credit:",Amount+credit_amt)
        elif option==2:
            debit_amt=float(input("Enter the amount to be debited:"))
            print("Amount after debit:",Amount-debit_amt)
        elif option==3:
            print("Mini Statement Amount:",Amount)
        elif option==4:
            break
else:
    print("Invalid credentials")