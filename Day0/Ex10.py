import lxmls.readers.galton as galton

galton_data = galton.load()

print "Data:"
print galton_data

import numpy as np

data = np.array(galton_data)
print data

print "What are the mean height and standard deviation of all the people in the sample?"
print "-------------------"
print "Mean: %s" % (np.mean(data))
print "Std: %s" %(np.std(data))


print "What is the mean height of the fathers and of the sons?"
print "-------------------"
print "Fathers mean: %s" % (np.mean(data[:, 0]))
print "Sons mean: %s" % (np.mean(data[:, 1]))



import matplotlib.pyplot as plt
plt.interactive(False)
# hist = plt.hist(np.ravel(data))
# plt.show(hist)

#bar = plt.scatter(x=data[:,0], y=data[:, 1])
#plt.show(bar)

# Fathers vs sons
#plt.plot(range(len(data)), data)

fig, ax = plt.subplots()
ax.set_color_cycle(["blue", "pink"])
# plt.plot(range(len(data)), data[:, 0])
# plt.plot(data[:, 0], data[:, 1])
colors = np.random.rand(len(data))

plt.scatter(data[:,0]+np.random.randn(len(data)), data[:,1]+np.random.randn(len(data)), c = colors)


plt.show()