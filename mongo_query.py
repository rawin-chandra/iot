import pymongo
import matplotlib.pyplot as plt
import numpy as np

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["temp_sensor"]

myquery = { "date": "29/7/2564" }

mydoc = mycol.find(myquery)
data = []     #list
for x in mydoc:
  data.append(x["temp"])

plt.plot(data, linestyle = 'dotted')
plt.show()

#print("mean = ", np.mean(data))
#print("std = " , np.std(data))
#print("percentile = " , np.percentile(data, 20))

#plt.hist(data)
#plt.show()


