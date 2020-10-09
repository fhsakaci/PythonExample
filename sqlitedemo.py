import sqlite3

def listele():
    baglanti = sqlite3.connect("chinook/chinook.db")
    cursor = baglanti.execute("select CustomerId, FirstName, LastName from customers")

    for sutun in cursor:      
         
        print(sutun[0],sutun[1],sutun[2])
          
    baglanti.close()

listele()         