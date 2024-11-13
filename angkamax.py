def max (angka1, angka2, angka3):
    if ((angka1 > angka2)) and ((angka1 > angka3)):
        return angka1
    elif ((angka2 > angka1)) and ((angka2 > angka3)):
        return angka2
    else:
        return angka3
    
l = int(input("masukkan angka1 :"))
o = int(input("masukkan angka2 :"))
u = int(input("masukkan angka3 :"))

cek_max = max(l,o,u)
print ("nilai maksimal dari",l, "dan",o, "dan",o, "adalah :",cek_max)
