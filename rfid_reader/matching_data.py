import pandas as pd

serial_pasien = int(input("Tempelkan kartu rfid anda : "))

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1ja8NXuQgRO7XPEB9WxfFf48ESaRzjgI335N4687kWFA/export?format=csv")
a = df[(df.Id_rfid == serial_pasien)]

b = str(a)
print(b)
file = open("data.txt",'w')

file.write(b)
file.close