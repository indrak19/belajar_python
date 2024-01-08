
Menu = { "Burger": 200000,
         "Teh": 5000,
        }
            



print("============= Menu =============")

for nama in Menu:
    print(f"{nama} \t : {Menu[nama]} ")

print("================================")

while True:
    Pilihan = input("Masukkan Pilihan Menu : ")
    pesan=input("ingin Memesan Lagi (Y/N) = ")
    if pesan.lower() == "n":
        break
    else:
        continue



print(f"Harga Yang dibayar = {Menu[Pilihan]}")