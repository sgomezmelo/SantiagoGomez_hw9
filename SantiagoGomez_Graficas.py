import numpy as np
import matplotlib.pyplot as plt

datos_python = np.loadtxt('times_python.csv', delimiter = ' ')
datos_cpp = np.loadtxt('times_cpp.csv', delimiter = ' ')

plt.figure()
plt.plot(datos_cpp[:,0],datos_cpp[:,1], label = 'c++')
plt.plot(datos_python[:,0],datos_python[:,1], label = 'python')
plt.xlabel('N')
plt.ylabel('Tiempo en s')
plt.legend()
#plt.savefig('cpp_vs_python.png')
