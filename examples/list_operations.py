if __name__ == '__main__':
    fruits = []  # create an empty list

    # add elements
    fruits.append("Kiwi")
    fruits.append("Berry")
    fruits.append("Melon")

    # show the current elements
    print(fruits)

    # sort the elements alphabetically
    fruits.sort()
    print(fruits)

    # delete the last element
    fruits.pop()
    print(fruits)

    # add element in specific index
    fruits.insert(0, "Apple")
    fruits.insert(1, "Strawberry")
    print(fruits)

    # delete element in specific index
    fruits.pop(1)
    print(fruits)

    # remove element by value
    fruits.remove("Apple")
    print(fruits)
