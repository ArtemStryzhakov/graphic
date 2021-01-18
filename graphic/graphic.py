import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Зонтик
x1 = np.arange(-12,13)
y1 = -1/18*x1**2 + 12
x2 = np.arange(-4,5)
y2 = -1/8*x2**2 + 6
x3 = np.arange(-12,-3)
y3 = -1/8*(x3+8)**2 + 6
x4 = np.arange(4,13)
y4 = -1/8*(x4-8)**2 + 6
x5 = np.arange(-4,1)
y5 = 2*(x5+3)**2-9
x6 = np.arange(-4,1)
y6 = 1.5*(x6+3)**2-10

plt.subplots()
plt.title("Зонтик))")
plt.grid(True)

plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6, linewidth=3, color="blue")
plt.show()

#Очки
x1 = np.arange(-9,0,1)
y1 = -1/16*(x1+5)**2+2
x2 = np.arange(1,10,1)
y2 = -1/16*(x2-5)**2+2
x3 = np.arange(-9,0,1)
y3 = 1/4*(x3+5)**2-3
x4 = np.arange(1,10,1)
y4 = 1/4*(x4-5)**2-3
x5 = np.arange(-9,-5,1)
y5 = -(x5+7)**2+5
x6 = np.arange(6,10,1)
y6 = -(x6-7)**2+5
x7 = np.arange(-1,2,1)
y7 = -0.5*(x7**2)+1.5 

plt.subplots()
plt.title("Очки")
plt.grid(True)

plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7, linewidth=3, color="orange")
plt.show()

#График
with open(r"C:/python/Graphic/dannie.txt","r") as MyFile:
    mas1=[]
    mas2=[]
    for line in MyFile:
        n=line.find(",")
        mas1.append(line[0:n].strip())
        mas2.append(float(line[n+1:len(line)].strip()))

plt.grid(True)
plt.title("Данные о ИТ безопасности")

color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)

plt.show()
