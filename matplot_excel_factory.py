import matplotlib.pyplot as plt
import csv

shake_force = []
shake_freq = []
fail_prob = []

with open('/home/rawin/data_set2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    plots.next()
    for row in plots:
        shake_force.append(int(row[2]))
        shake_freq.append(int(row[3]))
        fail_prob.append(float(row[4]))

'''
c = 0
with open('/home/rawin/data_set2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    plots.next()
    for row in plots:
        shake_force.append(int(row[2]))
        shake_freq.append(int(row[3]))
        fail_prob.append(float(row[4]))
        if c > 100:
            break
        c += 1
'''

'''
with open('/home/rawin/data_set2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    plots.next()
    for row in plots:
        if float(row[4]) > 0.7:
            shake_force.append(int(row[2]))
            shake_freq.append(int(row[3]))
            fail_prob.append(float(row[4]))
'''
'''
with open('/home/rawin/data_set2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    plots.next()
    for row in plots:
        if float(row[4]) > 0.7:
            #shake_force.append(int(row[2]))
            shake_freq.append(int(row[3]))
            fail_prob.append(float(row[4]))
'''
plt.plot(shake_force, marker = 'o')
plt.plot(shake_freq, marker = '*')
plt.plot(fail_prob, marker = 'x')
plt.show()
