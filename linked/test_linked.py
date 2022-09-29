from linked_list import SinglyLinkedList

if __name__ == '__main__':
    words = SinglyLinkedList()

    words.append('egg')
    words.append('ham')
    words.append('spam')

    current = words.tail

    while current:
        print(current.data)
        current = current.next

    # another way to print
    for word in words.iter():
        print(word)

    words.search("spam")

    words.search("juice")
