# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars = ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2-  Liste Kaç elemanlıdır ?
result = len(cars)

# 3-  Listenin ilk ve son elemanı nedir ?
result = cars[0]
result = cars[-1]

# 4- Mazda değerini Toyota ile değiştirin.
cars[3] = "Toyota"

# 5-  Mercedes listenin bir elemanı mıdır ?
result = "Mercedes" in cars

# 6-  Listenin -2 indeksindeki değer nedir ?
result = cars[-2]

# 7-  Listenin ilk 3 elemanını alın.
result = cars[:3]

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
cars[-2:] = ["Toyota", "Renault"]
result = cars

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
cars += ["Audi", "Nissan"]
result = cars

# 10- Listenin son elemanını silin.
del cars[-1]

# 11- Liste elemanlarını tersten yazdırınız.
result = cars[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)



print(result)