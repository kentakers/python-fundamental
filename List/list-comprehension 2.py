"""

"""


def main():

    print("\nPerintah del dengan list comprehension START:END:STEP")
    buah = ["Mangga", "Jeruk", "Melon", "Mangga"]
    del buah[0::2]      # START:END:STEP
    for i in range(0, len(buah)):
        print(buah[i])


if __name__ == '__main__':
    main()
