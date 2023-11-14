a = int(input("Enter no of items purchased :"))
t = 0
for i in range(a):
    c = int(input("Enter item price : "))
    d = int(input("Enter quantity : "))
    t = t+(c*d)
t1 = t
if(t>200):
    print("Discount of 5%")
    t = t*0.05
print("Taxes of 6%")
t1 = t1-t
total = t1
t1 = t1*0.06
total = total-t1
print("Total :",total)
