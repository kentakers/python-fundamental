"""

"""


def main():

    print("\nPerintah del dengan list comprehension")
    buah = ["Mangga", "Jeruk", "Melon",  "Mangga", ]
    del buah[:]
    for i in range(0, len(buah)):
        print(buah[i])

    print("\nPerintah del dengan list comprehension start")
    buah = ["Mangga", "Jeruk", "Melon", "Mangga"]
    del buah[0:-2]      # START:END
    for i in range(0, len(buah)):
        print(buah[i])


if __name__ == '__main__':
    main()
