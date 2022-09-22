from array_1d import Array1D

if __name__ == '__main__':
    menu = Array1D(5)

    print(menu.__len__())

    print(menu.__str__())

    # add value to specific index
    menu.__setitem__(0, 1)
    print(menu.__str__())
