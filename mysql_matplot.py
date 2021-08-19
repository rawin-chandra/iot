import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abcdefghijk",
  database="sensors"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT mean_temp FROM temp_data")
temp_data = mycursor.fetchall()

mycursor.execute("SELECT growth_rate FROM temp_data")
growth_data = mycursor.fetchall()


'''
mycursor.execute("SELECT mean_temp,growth_rate FROM temp_data WHERE growth_rate > 25")
data = mycursor.fetchall()
t = []
g = []
for x in data:
    t.append(x[0])
    g.append(x[1])
'''


c = 0
t = []
for x in temp_data:
  t.append(x)
  c += 1
  if c > 100:
      break

c = 0
g = []
for x in growth_data:
  g.append(x)
  c += 1
  if c > 100:
      break


#plt.plot(temp_data, marker = 'o')
#plt.plot(growth_data, marker = 'x')

plt.plot(t, marker = 'o')
plt.plot(g, marker = 'x')

plt.show()
