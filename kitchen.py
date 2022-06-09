print("This is the store of Mugato Kitchen,it contains foodstuff for the list for this week")
Oils=[{"Kimbo":14},{"Elianto":12}]
Cereals=[{"Maize":34},{"Rice 4kgs":23}]
Flour=[{"Jembe":12},{"Ajab":24},{"Butterfly"}]
#find items
#using dictionaries inside lists
#Dictionary has keys of the name of items with value as the number
#Store each item
#if items needed  reduce value and update list.
def likes(names):
    x=0
    while x<len(names):
        if len(names)==0:
            print("no one likes this")
        elif len(names)>0:
                x+=1
                print(f"{names[x]}  likes this ")
                   
likes(["John","Jame","Eunice"])


