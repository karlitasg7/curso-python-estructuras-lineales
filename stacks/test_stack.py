from stack import Stack

if __name__ == '__main__':
    food = Stack()

    print(food.peek())

    food.push('egg')
    food.push('ham')
    food.push('spam')

    print(food.pop())

    print(food.peek())
