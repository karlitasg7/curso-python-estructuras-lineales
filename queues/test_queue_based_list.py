from list_based_queue import ListQueue

if __name__ == '__main__':
    food = ListQueue()

    food.enqueue('eggs')
    food.enqueue('ham')
    food.enqueue('spam')

    print(food.dequeue())

    food.traverse()
