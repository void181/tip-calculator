print("welcome to the tip calculator")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
total_bill=input("what was the total bill")
#Format the result to 2 decimal places = 33.60
total_peoples=input("total numbr of peoples you want to split the bill")
tip=input("what percentage tip you would like to give?10,12,or 1?")
total_bill=float(total_bill)
total_peoples=int(total_peoples)
tip=int(tip)
tip=tip/100
tip=tip+1
total_bill=total_bill*tip
total_bill=total_bill/total_peoples
total_bill=round(total_bill,2)
print(f"each person should pay {total_bill}")
