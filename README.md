# P1_Komnum_A2
Praktikum 1 Komputasi Numerik

Anggota Kelompok:

- Christian Kevin Emor    (5025211153)

- Nayya Kamila Putri      (5025211183)

- Dimas Prihady Setyawan  (5025211184)

- Layyinatul Fuadah       (5025211207)

- Shahnaaz A. Firdaus     (05111940000158)

--------------------------------------------

**Contoh Soal Bolzano**

f(x)= x^3 + 10x^2 - 7x - 196

xLower       = -5

xUpper       = 8

x sebenarnya = 4

Iterasi = 1 | xL = -5.0 | xU = 8.0 | xR = 1.5 | f(xL) = -36.00000| f(xU) = 900.00000 | f(xR) = -180.62500 | Et = 62.50000 | Ea = Not yet

Iterasi = 2 | xL = 1.5 | xU = 8.0 | xR = 4.75 | f(xL) = -180.62500| f(xU) = 900.00000 | f(xR) = 103.54688 | Et = 18.75000 | Ea = 68.42105

Iterasi = 3 | xL = 1.5 | xU = 4.75 | xR = 3.125 | f(xL) = -180.62500| f(xU) = 103.54688 | f(xR) = -89.70117 | Et = 21.87500 | Ea = 52.00000

Iterasi = 4 | xL = 3.125 | xU = 4.75 | xR = 3.9375 | f(xL) = -89.70117| f(xU) = 103.54688 | f(xR) = -7.47681 | Et = 1.56250 | Ea = 20.63492

Iterasi = 5 | xL = 3.9375 | xU = 4.75 | xR = 4.34375 | f(xL) = -7.47681| f(xU) = 103.54688 | f(xR) = 44.23398 | Et = 8.59375 | Ea = 9.35252

Iterasi = 6 | xL = 3.9375 | xU = 4.34375 | xR = 4.14062 | f(xL) = -7.47681| f(xU) = 44.23398 | f(xR) = 17.45283 | Et = 3.51550 | Ea = 4.90579

Iterasi = 7 | xL = 3.9375 | xU = 4.14062 | xR = 4.03906 | f(xL) = -7.47681| f(xU) = 17.45283 | f(xR) = 4.75988 | Et = 0.97650 | Ea = 2.51445

Iterasi = 8 | xL = 3.9375 | xU = 4.03906 | xR = 3.98828 | f(xL) = -7.47681| f(xU) = 4.75988 | f(xR) = -1.41510 | Et = 0.29300 | Ea = 1.27323

Iterasi = 9 | xL = 3.98828 | xU = 4.03906 | xR = 4.01367 | f(xL) = -1.41510| f(xU) = 4.75988 | f(xR) = 1.65818 | Et = 0.34175 | Ea = 0.63259

Iterasi = 10 | xL = 3.98828 | xU = 4.01367 | xR = 4.00098 | f(xL) = -1.41510| f(xU) = 1.65818 | f(xR) = 0.11860 | Et = 0.02450 | Ea = 0.31717

Iterasi = 11 | xL = 3.98828 | xU = 4.00098 | xR = 3.99463 | f(xL) = -1.41510| f(xU) = 0.11860 | f(xR) = -0.64914 | Et = 0.13425 | Ea = 0.15896

Iterasi = 12 | xL = 3.99463 | xU = 4.00098 | xR = 3.99781 | f(xL) = -0.64914| f(xU) = 0.11860 | f(xR) = -0.26488 | Et = 0.05475 | Ea = 0.07954

Iterasi = 13 | xL = 3.99781 | xU = 4.00098 | xR = 3.99939 | f(xL) = -0.26488| f(xU) = 0.11860 | f(xR) = -0.07380 | Et = 0.01525 | Ea = 0.03951

Iterasi = 14 | xL = 3.99939 | xU = 4.00098 | xR = 4.00019 | f(xL) = -0.07380| f(xU) = 0.11860 | f(xR) = 0.02299 | Et = 0.00475 | Ea = 0.02000

Iterasi = 15 | xL = 3.99939 | xU = 4.00019 | xR = 3.99979 | f(xL) = -0.07380| f(xU) = 0.02299 | f(xR) = -0.02541 | Et = 0.00525 | Ea = 0.01000

Iterasi = 16 | xL = 3.99979 | xU = 4.00019 | xR = 3.99999 | f(xL) = -0.02541| f(xU) = 0.02299 | f(xR) = -0.00121 | Et = 0.00025 | Ea = 0.00500

Iterasi = 17 | xL = 3.99999 | xU = 4.00019 | xR = 4.00009 | f(xL) = -0.00121| f(xU) = 0.02299 | f(xR) = 0.01089 | Et = 0.00225 | Ea = 0.00250

Iterasi = 18 | xL = 3.99999 | xU = 4.00009 | xR = 4.00004 | f(xL) = -0.00121| f(xU) = 0.01089 | f(xR) = 0.00484 | Et = 0.00100 | Ea = 0.00125

Iterasi = 19 | xL = 3.99999 | xU = 4.00004 | xR = 4.00002 | f(xL) = -0.00121| f(xU) = 0.00484 | f(xR) = 0.00242 | Et = 0.00050 | Ea = 0.00050

Iterasi = 20 | xL = 3.99999 | xU = 4.00002 | xR = 4.0 | f(xL) = -0.00121| f(xU) = 0.00242 | f(xR) = 0.00000 | Et = 0.00000 | Ea = 0.00050


![Figure_1](https://user-images.githubusercontent.com/101172637/196720793-72fc590c-63b2-47c2-9c60-7b2eebd2c1fc.png)

--------------------------------------------

**Penjelasan Program**

**1. Import Libraries**

  ```python
  import matplotlib.pyplot as plt
  import numpy as np
  ```
Menggunakan dua library Python yaitu *Matplotlib.pyplot* dan *NumPy* yang berfungsi untuk gambar grafik


**2. Menentukan pilihan metode**

```python
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
```

Tersedia dua metode bolzano berbeda

- Pertama (metode_bolzano1), xtrue diketahui jadi Error True dan Error Approximate dapat dicari
- Kedua (metode_bolzano2), xtrue tidak diketahui jadi Error True dan Error Approximate tidak dapat dicari

**3. Meminta user-input**

```python
xL = float(input("Input x lower: "))
xU = float(input("Input x upper: "))
xtrue = float(input("Input x true: "))
function = input("Input your function: ")
iteration = int(input("How many iteration: "))

metode_bolzano1(function,xL, xU, xtrue, iteration)
```

  xL = Menerima nilai dari Lower

  xU = Menerima nilai dari Upper

  xtrue = Nilai x yang sebenarnya

  function = Fungsi yang dipakai

  iteration = Jumlah iterasi yang dibutuhkan
  
  Fungsi metode_bolzano1 dipanggil

**4. Membuat fungsi Bolzano**

  ```python
  def metode_bolzano1(function, xL, xU, xtrue, iteration):
  ```

  Didalam fungsi Bolzano, terdapat 2 fungsi yaitu:

  **f(x): berfungsi untuk fungsi yang akan dipakai**

  ```python
      def f(x): #Evaluating mathematical function into expression
        f = eval(function)
        return f
  ```

  **graphic(): berfungsi untuk visualisasi grafik**

  ```python
      def graphic(): #Draw the graphic of Bolzano Method
        x = np.linspace(-10, 10, 100)
        y = f(x)

        plt.plot(x, y)
        plt.title("Visualization of Bolzano Method with given function")
        plt.draw()
        plt.show()
  ```
    
  Fungsi awal untuk mencari nilai iterasi 1
  
  ```python
    #First value for each xR,f(xL),f(xU),f(xR),Et, and Ea
    xR = float("{:.5f}".format((xL+xU)/2))
    yL = ("{:.5f}".format(f(xL)))
    yU = ("{:.5f}".format(f(xU)))
    yR = ("{:.5f}".format(f(xR)))
    Et = ("{:.5f}".format(abs(((xtrue - xR) / xtrue)*100)))
    Ea = "Not yet"
  ```
  
  xR    = Taksiran pertama
  
  f(xL) = nilai function dengan x bernilai xL
  
  f(xU) = nilai function dengan x bernilai xU
  
  f(xR) = nilai function dengan x bernilai xR
  
  Et    = Mencari error true dengan xTrue
  
  Ea    = Mencari error approximate dengan nilai xR bertahap (Bernilai not yet di awal karena xR hanya ada satu)
  
  **Menggunakan perulangan while loop untuk melakukan iterasi sesuai input user (mencari nilai-nilai terbaru juga)**
  ```python
    i = 1
    while (abs(f(xR)) > 0 and i < iteration): #While loop for iteration
        print (f"Iterasi = {i} | xL = {xL} | xU = {xU} | xR = {xR} | f(xL) = {yL}| f(xU) = {yU} | f(xR) = {yR} | Et = {Et} | Ea = {Ea}")
        if f(xL)*f(xR) < 0:
            xU = xR

        elif f(xL)*f(xR) > 0:
            xL = xR

        else:
            print(xR)

        b = xR #xR value before updated into a new one (for Ea)
        
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
    
```    
 Perulangan dilakukan dengan syarat-syarat berikut:
 1. Nilai absolut f(xR) belum lebih besar 0 dan iterasi belum mencapai input user
 2. Kondisi perubahan nilai yang dilakukan terhadap xL dan xU serta f(xL) dan f(xR)
 3. Nilai b merupakan nilai xR yang belum diperbarui (berfungsi untuk Error Approximate)
 4. Perbaruan nilai dari komponen xL, xU, xR, f(xL), f(xU), f(xR), Et, dan Ea
 
 Terakhir
 
 - Print iterasi terakhir untuk xL, xU, xR, f(xL), f(xU), f(xR), Et, dan Ea
 
 - Visualisasi ditunjukan

**NOTE**

Metode tanpa xtrue bernama *metode_bolzano2*, caranya sama seperti *metode_bolzano1* tapi semua hal yang berkaitan dengan xtrue, Ea, dan Et tidak ada.
