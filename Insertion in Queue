queue = []
front = -1
rear = -1
def enqueue(front,rear):
    element = input("Enter the element to enqueue: ")
    if front == -1 and rear == -1:
        front = 0
        rear = 0
    elif front ==0:
        rear =rear + 1
    queue.append(element)
    print(f"{element} enqueued to queue")
    print(f"Current queue: {queue}")
    print(f"Front index: {front}, Rear index: {rear}")
    return front,rear
n = int(input("Enter number of elements to enqueue: "))
for i in range(0,n):
    enqueue(front,rear)
