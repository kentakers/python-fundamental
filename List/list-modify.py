def main():\
        # membuat list
    buah = ["Mangga", "Apel", "Durian"]
    print("Elemen sebelum diubah : ")
    print(buah)

    # mengubah nilai elemen list
    buah[1] = "Melon"
    buah[-1] = "Semangka"

    # menampilkan hasil perubahan
    print("\nSetelah diubah:")
    print(buah)


if __name__ == '__main__':
    main()
