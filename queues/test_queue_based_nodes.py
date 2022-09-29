from node_based_queue import Queue

if __name__ == '__main__':
    food = Queue()

    food.enqueue('egg')
    food.enqueue('ham')
    food.enqueue('spam')

    print(food.head)

    print(food.head.next.data)

    print(food.tail.data)
    print(food.tail.previous.data)

    print(food.count)

    print(food.dequeue())
    print(food.count)
