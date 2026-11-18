def bankoper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updateBal = totalBal - withdraw

    return totalBal, updateBal

if __name__ == "__main__":
    initialBal = int(input("Enter amount as initial Bal"))
    deposit = int(input("Enter amount to deposit"))
    withdraw = int(input("Enter withdrawal amount"))

    totalBal, updatedBal = bankoper(initialBal, deposit, withdraw)

    print("Total Balance  :",totalBal)
    print("Updated Balance :",updatedBal)