nilai_teori = input("nilai:")
nilai_teori = int(nilai_teori)
nilai_praktek = input("nilai:")
nilai_praktek = int(nilai_praktek)
minimal = 70

if nilai_teori >= minimal and nilai_praktek >= minimal:
    print("Selamat, anda lulus!")
elif nilai_teori < minimal and nilai_praktek >= minimal:
    print("Anda harus mengulang ujian teori.")
elif nilai_teori >= minimal and nilai_praktek < minimal:
    print("Anda harus mengulang ujian praktek.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")