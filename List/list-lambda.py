""" 
list dengan ekspresi lambda 
"""


def main():
    listku = [10, 20, 30]
    listmu = list(map(lambda x: x * 2, listku))
    print(f'listku:{listku}')
    print(f'listmu:{listmu}')


if __name__ == '__main__':
    main()
