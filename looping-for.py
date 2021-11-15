"""
Perulangan menggunakan for digunakan untuk mengambil atau menelusuri elemen yang terdapat pada tipe-tipe koleksi seperti
string, list, tuple, dictionary, set, dan objek bertipe range.
"""


def main():
    # membuat list
    daftar = ['Matematika', 'Fisika', 'kimia']
    
    # menggunakan for pada tipe list
    for i in range(len(daftar)):
        print("%d : %s" % (i, daftar[i]))
    

if __name__ == "__main__":
    main()
