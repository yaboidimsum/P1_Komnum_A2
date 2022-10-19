# P1_Komnum_A2
Praktikum 1 Komputasi Numerik

Anggota Kelompok:

-Christian Kevin Emor   - 5025211153

-Nayya Kamila Putri     - 5025211183

-Dimas Prihady Setyawan - 5025211184

-Layyinatul Fuadah      - 5025211207

-Shahnaaz A. Firdaus    - 05111940000158

--------------------------------------------

**Contoh Soal Bolzano**

f(x)= x^3 + 10x^2 - 7x - 196

xLower       = -5

xUpper       = 8

x sebenarnya = 4

Iterasi = 1 | xL = -5.0 | xU = 8.0 | xR = 1.5 | f(xL) = -36.00000 | f(xU) = 900.00000 | f(xR) = -180.62500 | Et = 62.50000 | Ea = Not yet

Iterasi = 2 | xL = 1.5 | xU = 8.0 | xR = 4.75 | f(xL) = -180.62500 | f(xU) = 900.00000 | f(xR) = 103.54688 | Et = 18.75000 | Ea = 68.42105

Iterasi = 3 | xL = 1.5 | xU = 4.75 | xR = 3.125 | f(xL) = -180.62500 | f(xU) = 103.54688 | f(xR) = -89.70117 | Et = 21.87500 | Ea = 52.00000

Iterasi = 4 | xL = 3.125 | xU = 4.75 | xR = 3.9375 | f(xL) = -89.70117 | f(xU) = 103.54688 | f(xR) = -7.47681 | Et = 1.56250 | Ea = 20.63492

Iterasi = 5 | xL = 3.9375 | xU = 4.75 | xR = 4.34375 | f(xL) = -7.47681 | f(xU) = 103.54688 | f(xR) = 44.23398 | Et = 8.59375 | Ea = 9.35252

![Figure_1](https://user-images.githubusercontent.com/101172637/196720793-72fc590c-63b2-47c2-9c60-7b2eebd2c1fc.png)

--------------------------------------------

**Penjelasan Program**

**1. Import Libraries**

<img width="328" alt="image" src="https://user-images.githubusercontent.com/101172637/196722380-7eef02f6-4205-41f3-9d94-378e1a648b83.png">

Menggunakan dua library Python yaitu *Matplotlib.pyplot* dan *NumPy* yang berfungsi untuk gambar grafik


**2. Meminta user-input**

<img width="490" alt="image" src="https://user-images.githubusercontent.com/101172637/196723228-73e4e8b8-a5d4-42a0-9e1e-49c697fb1aff.png">

  xL = Menerima nilai dari Lower

  xU = Menerima nilai dari Upper

  xtrue = Nilai x yang sebenarnya

  Function = Fungsi yang dipakai

  Iteration = Jumlah iterasi yang dibutuhkan

**3. Membuat fungsi Bolzano**

  <img width="549" alt="image" src="https://user-images.githubusercontent.com/101172637/196726480-b470d84c-1b52-407c-ba8e-6fcc6b92988b.png">

  Didalam fungsi Bolzano, terdapat 2 fungsi yaitu:

  **f(x): berfungsi untuk function**

  <img width="234" alt="image" src="https://user-images.githubusercontent.com/101172637/196729511-38ee9dfc-73c4-41e8-bdb2-3c73f11bdf87.png">

  **graphic(): berfungsi untuk visualisasi data**

  <img width="720" alt="image" src="https://user-images.githubusercontent.com/101172637/196729581-1c6ed0be-2694-47ec-ae26-44606adadb87.png">


