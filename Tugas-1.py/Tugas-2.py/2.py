Nama = ['Fawaz','John']
No_tlp = ['08123456789', '08987654321']

print("Selamat datang! \n --- Menu --- \n 1. Daftar Kontak  \n 2. Tambah Kontak \n 3. Keluar ")

check_address = int(input("Pilih menu:"))
if check_address == 1:
  print(Nama, No_tlp)
elif check_address == 2:
  Nama.append(input("Masukkan nama: ")), 
  No_tlp.append(input("Masukkan no telepon:")), 
  for (a,b) in zip(Nama, No_tlp):
     print(a, b)
elif check_address == 3:
   print("Program selesai sampai jumpa!") 
else:
    print("Menu tidak tersedia")
