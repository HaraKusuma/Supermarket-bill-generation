from datetime import datetime

name=input("Enter your Name:")
#LIST OF ITEMS

lists='''
LIST OF ITEMS

Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Panner  Rs 100/kg
Noodles Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 85/each

'''
#DECLARATION 

price=0
pricelist=[]
total_price=0
final_price=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,
       'sugar':30,
       'salt':20,
       'oil':80,
       'panner':100,
       'noodles':50,
       'boost':90,
       'colgate':85}
option=int(input("For list of items press 1 : "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("Press - 1 to Buy / 2 to Exit : "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items: ")
        # quantity=int(input("Enter quantity:"))
        if item in items.keys():
            quantity=int(input("Enter quantity: "))
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            total_price+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(total_price*5)/100
            #GST
            final_price=gst+total_price

        else:
            print("Sorry! Item you entered is not available")

    else:
        print("You have entered invalid , Please try again !")

    inp=input("Can i bill the items? Yes or No: ")
    if inp=='yes':
        pass
        if final_price!=0:
            print(" ")
            print(30*'=',"KH Supermarket",30*'=')
            print(33*' ',"Tirupati")
            print("Name: ",name,30*" ")
            print("Date:",datetime.now())
            print(75*"-")
            print("Sno",5*" ",'items',11*" ","Quantity:",8*" ",'Price:')
            
            for i in range(len(pricelist)):
                print(i+1,8*" ",ilist[i],14*" ",qlist[i],15*" ",plist[i])
            print(75*"-")
            print('Total Amount: ','Rs ',total_price)
            print("GST Amount: ",'Rs',gst)
            print(75*"-")
            print('Final Amount to be paid: ','Rs ',final_price)
            print(75*"-")
            print(25*" ",'Thanks for visiting!')
            print(75*"-")








