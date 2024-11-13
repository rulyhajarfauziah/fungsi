def luaspersegipanjang(panjang,lebar):
    return panjang*lebar
def kelilingpersegipanjang(panjang,lebar):
    return 2*(panjang,lebar)

le = int(input("masukkan panjang :"))
vi = int(input("masukkan lebar :"))

hasil_luas = luaspersegipanjang(le,vi)
hasil_keliling = kelilingpersegipanjang(le,vi)
print("luasnya adalah ",hasil_luas)
print("kelilingnya adalah ",hasil_keliling)
