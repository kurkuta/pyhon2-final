import pymongo
menu = {"lick":12, "tick":9, "crick":0}
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Restraunt"]
mycol = mydb["Menu"]
mycol.insert_one(menu)

def get_order():
    total = 0
    order = {}
    while True:
        x = input("What would you like?: ").lower()
        if x in menu:
            q = int(input("how much?: "))
            total = total+(q*menu[x])
            if x in order:
                order[x] += q
            else:
                order[x] = q
        else:
            print("sorry, we don't serve the item")
        l = int(input("Would you like to continue? 1.yes 2.no: "))
        if l == 2:
            print("order:",order)
            print("total:",total,"$")
            break
        else:
            continue
get_order()
