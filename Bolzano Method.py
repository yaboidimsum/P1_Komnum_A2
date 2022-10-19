import matplotlib.pyplot as plt
import numpy as np

def metode_bolzano(function,xL, xU, xtrue,iteration):

    def f(x):
        f = eval(function)
        return f

    def graphic():
        x = np.linspace(-10, 10, 100)
        y = f(x)

        plt.plot(x, y)
        plt.title("Visualization of Bolzano Method with given function")
        plt.draw()
        plt.show()

    xR = float("{:.5f}".format((xL+xU)/2))
    yL = ("{:.5f}".format(f(xL)))
    yU = ("{:.5f}".format(f(xU)))
    yR = ("{:.5f}".format(f(xR)))
    Et = ("{:.5f}".format(abs(((xtrue - xR) / xtrue)*100)))
    Ea = "Not yet"

    i = 1
    while (abs(f(xR)) > 0 and i < iteration):
        print (f"Iterasi = {i} | xL = {xL} | xU = {xU} | xR = {xR} | f(xL) = {yL}| f(xU) = {yU} | f(xR) = {yR} | Et = {Et} | Ea = {Ea}")
        if f(xL)*f(xR) < 0:
            xU = xR

        elif f(xL)*f(xR) > 0:
            xL = xR

        else:
            print(xR)

        b = xR
        xR = float("{:.5f}".format((xL+xU)/2))
        yL = ("{:.5f}".format(f(xL)))
        yU = ("{:.5f}".format(f(xU)))
        yR = ("{:.5f}".format(f(xR)))
        Et = ("{:.5f}".format(abs(((xtrue - xR) / xtrue)*100)))
        Ea = ("{:.5f}".format(abs(((xR - b)/xR)*100)))
        i += 1

    print (f"Iterasi = {i} | xL = {xL} | xU = {xU} | xR = {xR} | f(xL) = {yL}| f(xU) = {yU} | f(xR) = {yR} | Et = {Et} | Ea = {Ea}")
    graphic()

xL = float(input("Input x lower: "))
xU = float(input("Input x upper: "))
xtrue = float(input("Input x true: "))
function = input("Input your function: ")
iteration = int(input("How many iteration: "))

metode_bolzano(function,xL, xU, xtrue, iteration)


