import sys

def penjumlahan():
  jumlah = 0
  banyaknya = 0

  # Ambil input angka dari pengguna
  while True:
    angka = input("Masukkan harga barangS (enter untuk berhenti): ")
    if angka == "":
      break

    # Konversi angka ke integer
    angka = int(angka)

    # Tambahkan angka ke total
    jumlah += angka

    # Tambahkan jumlah angka
    banyaknya += 1

  return jumlah, banyaknya

def promo (banyaknya,jumlah):
    if banyaknya == 1:
        diskon = jumlah * 0.05
        harga = jumlah - diskon
    elif banyaknya == 2:
        diskon = jumlah * 0.1
        harga = jumlah - diskon
    else:
        diskon = jumlah * 0.15
        harga = jumlah - diskon
    return diskon, harga


if __name__ == "__main__":
    jumlah, banyaknya = penjumlahan()
    diskon, harga = promo(banyaknya, jumlah)

print(f"Banyak barang: {banyaknya}")
print(f"Diskon: {diskon}")
print(f"Harga awal: {jumlah}")
print(f"Total harga semuanya: {harga}")

uang = int(input("Masukan uang pembeli: "))
bayar = uang - harga
if uang < harga:
    sys.exit(print("Uang anda kurang"))
print(f"Kembalian: {bayar}")
