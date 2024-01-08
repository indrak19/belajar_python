
"""lion perjam 300.000
citylink perjam 500.000
garuda perjam 800.000
batik air perjam 400.000"""


#Harga maskapai per 1 jam
maskapai={
    "lion":300000,
    "city link":500000,
    "garuda":800000,
    "batik air":400000,
}
#Waktu Perjalanan per jam
perjalanan={
    "PKU-JKT": 2,
    "PKU-JGJA":5, 
    "PKU-SMRNDA":8,
    "PKU-BTM":1.5,
}

print("-----------Pesan Tiket Pesawat dengan tujuan---------")

# Menampilkan Tujuan Penerbangan
print("Tujuan Penerbangan")
for i in perjalanan: 
    print(i)
    
p=input("Pilih Perjalanan :")

#Menampilkan Maskapai
print("\nMaskapai Penerbangan")
for j in maskapai:
    print(j)
q=input("Pilih Maskapai :")

r=int(input("\nJumlah Kursi :"))

s=perjalanan[p.upper()]*maskapai[q]*r
print("Total Pembayaran",float(s))


print("------------------------------------------------------")