import sqlite3
conn = sqlite3.connect('ShopCart.db')
c = conn.cursor()
c.execute("""CREATE TABLE Cartt (
            Product text,
            Price integer
            )""")

sc = [["carte",2],["asfet",5],["safdi",9]]
cs = sc[::-1]
for i in cs:
    c.execute("INSERT INTO Cartt VALUES (:Product, :Price)", {'Product': (i[0]), 'Price': (i[1])})
c.execute("SELECT * FROM Cartt")
print (c.fetchall())
conn.commit()
conn.close()
