# 중간 논술형.py
# 중간 논술형 ver1
f=open("20230991.txt", 'w')

coffee = int(input("Coffee count: "))
f.write("Coffee count:\n")
print("Coffee count is {0}".format(coffee))
f.write("Coffee count is {0}\n".format(coffee))

while(coffee):
    money=int(input("Insert money: "))
    f.write("Insert money:\n")

    if((money%1000)!=0):
        continue
    print("{0}won received".format(money))
    f.write("{0}won received\n".format(money))

    if(money==1000):
        coffee-=1

    elif(money>1000):
        print("Change is {}won".format(money-1000))
        f.write("Change is {}won".format(money-1000))
        coffee-=1

    else:
        pass
    if(coffee==0):
        print("sold out.")
        f.write("sold out.\n")
        break

f.close

#중간 논술 ver2
f=open("20230991.txt",'w')

coffee=int(input("coffee count:"))
print("coffee count is %d." %coffee)
f.write("coffee count is %d.\n" %coffee)

while True:
    money=int(input("insert money: "))
    print("%d won received. " %money)
    f.write("%d won received.\n" %money)

    if money == 1000:
        coffee-=1
    else:
        if money>1000:
            print("Change is %d won" %(money-1000))
            f.write("Change is %d won\n" %(money-1000))
            coffee-=1
    if coffee==0:
        print("Sold out.")
        f.write("Sold out.\n")
        break
    
f.close()