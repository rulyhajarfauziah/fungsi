def faktorial (n):
    if n==0 or n==1:
        return 1
    else:
        return n*(faktorial(n-1))

r = int (input("masukkan nilai yang akan dicari :"))   
cari_faktorial = faktorial (r)
print ("nilai dari",r, "! adalah ",cari_faktorial)
