import matplotlib.pyplot as plt
import numpy as np

def metode_bolzano1(function,xL, xU, xtrue,iteration):

    def f(x): #Evaluating mathematical function into expression
        f = eval(function)
        return f

    def graphic(): #Draw the graphic of Bolzano Method
        x = np.linspace(-10, 10, 100)
        y = f(x)

        plt.plot(x, y)
        plt.title("Visualization of Bolzano Method with given function")
        plt.draw()
        plt.show()

    #First value for each xR,f(xL),f(xU),f(xR),Et, and Ea
    xR = float("{:.5f}".format((xL+xU)/2))
    yL = ("{:.5f}".format(f(xL)))
    yU = ("{:.5f}".format(f(xU)))
    yR = ("{:.5f}".format(f(xR)))
    Et = ("{:.5f}".format(abs(((xtrue - xR) / xtrue)*100)))
    Ea = "Not yet"

    i = 1
    while (abs(f(xR)) > 0 and i < iteration): #While loop for iteration
        print (f"Iterasi = {i} | xL = {xL} | xU = {xU} | xR = {xR} | f(xL) = {yL}| f(xU) = {yU} | f(xR) = {yR} | Et = {Et} | Ea = {Ea}")
        if f(xL)*f(xR) < 0:
            xU = xR

        elif f(xL)*f(xR) > 0:
            xL = xR

        else:
            print(xR)

        b = xR #xR value before updated into a new one (for Ea).

        #Update each value to the new one
        xR = float("{:.5f}".format((xL+xU)/2))
        yL = ("{:.5f}".format(f(xL)))
        yU = ("{:.5f}".format(f(xU)))
        yR = ("{:.5f}".format(f(xR)))
        Et = ("{:.5f}".format(abs(((xtrue - xR) / xtrue)*100)))
        Ea = ("{:.5f}".format(abs(((xR - b)/xR)*100)))
        i += 1

    print (f"Iterasi = {i} | xL = {xL} | xU = {xU} | xR = {xR} | f(xL) = {yL}| f(xU) = {yU} | f(xR) = {yR} | Et = {Et} | Ea = {Ea}")
    graphic()

def metode_bolzano2(function,xL , xU,iteration):

    def f(x): #Evaluating mathematical function into expression
        f = eval(function)
        return f

    def graphic(): #Draw the graphic of Bolzano Method
        x = np.linspace(-10, 10, 100)
        y = f(x)

        plt.plot(x, y)
        plt.title("Visualization of Bolzano Method with given function")
        plt.draw()
        plt.show()

    # First value for each xR,f(xL),f(xU),f(xR).
    xR = float("{:.5f}".format((xL+xU)/2))
    yL = ("{:.5f}".format(f(xL)))
    yU = ("{:.5f}".format(f(xU)))
    yR = ("{:.5f}".format(f(xR)))

    i = 1
    while (abs(f(xR)) > 0 and i < iteration): #While loop for iteration
        print (f"Iterasi = {i} | xL = {xL} | xU = {xU} | xR = {xR} | f(xL) = {yL}| f(xU) = {yU} | f(xR) = {yR} ")
        if f(xL)*f(xR) < 0:
            xU = xR

        elif f(xL)*f(xR) > 0:
            xL = xR

        else:
            print(xR)

        # Update each value to the new one
        xR = float("{:.5f}".format((xL+xU)/2))
        yL = ("{:.5f}".format(f(xL)))
        yU = ("{:.5f}".format(f(xU)))
        yR = ("{:.5f}".format(f(xR)))
        i += 1

    print (f"Iterasi = {i} | xL = {xL} | xU = {xU} | xR = {xR} | f(xL) = {yL} | f(xU) = {yU} | f(xR) = {yR}")
    graphic()


print("Bolzano Method Numeric Computing")
option = int(input("x true include (1) / x true not include (0): "))
#Choose if x true wanna be included or not

if option == 1:
    xL = float(input("Input x lower: "))
    xU = float(input("Input x upper: "))
    xtrue = float(input("Input x true: "))
    function = input("Input your function: ")
    iteration = int(input("How many iteration: "))

    metode_bolzano1(function, xL, xU, xtrue, iteration)
    #metode_bolzano1 is function with xtrue to find the Ea and Et

elif option == 0:
    xL = float(input("Input x lower: "))
    xU = float(input("Input x upper: "))
    function = input("Input your function: ")
    iteration = int(input("How many iteration: "))

    metode_bolzano2(function, xL, xU, iteration)
    # metode_bolzano2 is function without xtrue, Ea and Et
else:
    print("Wrong input")
