# Electricity Bill Calculator

RATE = 12.90

#validate customer's name
while True: 
    name = input("Enter customer name: ")
   
    if name.strip() != "":
        break
    else:
        print("Invalid name. Name can't be empty.")
    
#validate past readings
while True:
     previous = float(input("Enter previous meter reading: "))
    
    
     if previous >=0:
        break 
     else:
        print("Invalid reading. Please add a number that is atleast 0.")
   
#validate current readings   
while True:    
    current = float(input("Enter current meter reading: "))
    
    if current >= previous:
        break
    else:
        print("Invalid readin. Please add a number that is atleast your previous reading.")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
