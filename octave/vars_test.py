from oct2py import octave
import matplotlib.pyplot as plt
import numpy as np

[x, y, z, class_o, a, b, theta] = octave.vars(124.33, 'this')
print x, y, z, class_o

print len(theta)
plt.plot(np.array(theta), np.array(a), 'x-')
plt.ylabel('Sine Wave Values')
plt.show()
