Balance=50000
n=0
print('1.Deposit')
print('2.Withdraw')
print('3.Check')
print('4.Exit')
print('(Notice: It Will Run Until You Chosse To Exit)')
while True:
    command = int(input("Enter Number of the Choice You want to choose:"))
    if command == 1:
        Deposit=int(input("How Much Do You Want To Deposit: "))
        Balance=Deposit+Balance
        print("Deposit Successful. Balance",Balance)
      
    elif command == 2:
        Withdraw=int(input("How Much Do You Want To Withdraw: "))
        if Withdraw<Balance:
          Balance=Balance-Withdraw
          print("Withdraw Successful. Balance",Balance)

        else:
          print("Balance Insufficient")
      
    elif command == 3:
        print("Balance",Balance)
      
    elif command == 4:
        print('Exit')
        break

    else:
      print("Invalid Input")