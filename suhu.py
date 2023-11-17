
Suhu = float(input("Masukan Suhu : "))
satuan = input("Masukkan Indeks Satuan Skala Suhu : ")

if (satuan == "c"):
    print(Suhu,"derajat celcius: ")
    print("fahrenheit: ", (Suhu*9/5)+32,"derajat")
    print("kelvin: ", Suhu+273, "derajat")

elif (satuan == "f"):
    print(Suhu,"derajat fahrenheit: ")
    print("celsius: ", (Suhu*5/9)-32, "derajat")
    print("kelvin: ", (Suhu-32)*(5/9)+273, "derajat")

elif (satuan == "k"):
    print(Suhu,"derajat Kelvin: ")
    print("celsius: ", Suhu-273, "derajat")
    print("fahrenheit: ", (Suhu-273)*(9/5)+32, "derajat")