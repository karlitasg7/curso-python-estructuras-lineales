from stack_based_queue import Queue

if __name__ == '__main__':
    numbers = Queue()

    numbers.enqueue(5)
    numbers.enqueue(6)
    numbers.enqueue(7)

    print(numbers.inbound_stack)

    print(numbers.dequeue())

    print(numbers.inbound_stack)
    print(numbers.outbound_stack)
