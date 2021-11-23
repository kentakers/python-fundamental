def lipat_ganda(x):
    return x * 2


listku = [10, 20, 30]

"""
Elemen yang ada di listku akan di masukkan ke dalam nilai x fungsi lipat_ganda
kemudian hasilnya akan di input ke dalam listmu
"""
listmu = list(map(lipat_ganda, listku))
print(f'listku:{listku}')
print(f'listmu:{listmu}')
