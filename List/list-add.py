def main():
    # membuat list
    buah = ["Mangga", "Apel", "Durian"]
    print("Elemen awal : ")
    print(buah)

    # menggunakan metode append()
    buah.append("Jeruk")
    print("\nSetelah append():")
    print(buah)

    # menggunakan metode insert()
    buah.insert(1, "Kiwi")          # angka 1 merupakan index
    print("\nSetelah insert():")
    print(buah)

    # menggunakan metode extend()
    buah.extend(["Melon", "Anggur"])
    print("\nSetelah extend():")
    print(buah)


if __name__ == '__main__':
    main()
