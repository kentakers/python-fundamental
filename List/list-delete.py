
"""
Di python untuk menghapus elemen yang ada didalam list ada 2 metode yaitu remove() dan clear()
1. remove()
- Metode remove() berfungsi untuk menghapus elemen yang ada didalam list.
- Jika terdapat dua atau lebih elemen yang sama maka hanya akan menghapus satu elemen yang ditemukan pertama kali.
- Nilai/elemen yang ingin dihapus harus sama dengan yang ada di dalam list : 
    * Jeruk == Jeruk
    * Jeruk >< jeruk
    
2. pop()
- Metode pop() berfungsi untuk menghapus elemen berdasarkan index yang ada di dalam list.
- Jika nilainya kosong pop(), maka elemen terakhir yang akan dihapus.

3. clear()
Untuk menghapus seluruh elemen/nilai yang ada di dalam list, gunakan metode clear()
"""


def main():
    # membuat list
    buah = ["Mangga", "Jeruk", "Melon", "Jeruk", "Mangga", "Mangga"]
    print("Sebelum dihapus:")
    print(buah)

    # menghapus elemen list dengan remove()
    buah.remove("Mangga")
    buah.remove("Jeruk")

    # menampilkan hasil setelah dihapus menggunakan remove()
    print("\nSetelah dihapus menggunakan remove()")
    print(buah)

    # menghapus elemen list dengan pop()
    buah.pop(2)

    # menampilkan hasil setelah dihapus menggunakan remove()
    print("\nSetelah dihapus menggunakan pop()")
    print(buah)

    # menghapus seluruh elemen di dalam list
    buah.clear()

    # menampilkan hasil setelah dihapus menggunakan clear()
    print("\nSetelah dihapus menggunakan clear()")
    print(buah)


if __name__ == '__main__':
    main()
