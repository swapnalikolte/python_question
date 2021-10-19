print("welcome  to state bank of india")
print("please insert your card")
pin_inp =1234
pin = int(input("please enter your pin:"))
if pin==1234:
    print("1.blance enquiry")
    print("2.withdraw money")
    print("3.deposite money")
    print("4.transfer money")
    print("5.quit")
    transaction = input("which mode you prefer(please select the no)")
    if transaction=="1":
        slip=input("do you want to slip")
        if slip=="yes":
            print("collect your slip")
        else:
            print("thank you for visiting us")
    elif transaction=="2":
        amount=int(input("enter your amount for withdraw amount"))
        if amount<=100000:
            #print("please collect cash")
            #if transaction-amount
            print(100000-amount,"this is your bank balance")
        else:
            print("please enter valid ammount for withdraw")
    elif transaction=="3":
        deposite=int("enter ammount which you want to deposite")
        if deposite>0:
             print("your money is successfully deposite")
        else:
            print("please enter valid ammount for deposite your money")
    elif transaction=="4":
        trans=int(input("transfer money is"))
        if trans>0:
             print("your money is successfully transfer")
        else:
            print("please enter valid ammount for transfer")
    elif transaction=="5":
        print("quit")
    else:
          print("please choose any tranjaction")
else:
        print("please enter valid pin.....")