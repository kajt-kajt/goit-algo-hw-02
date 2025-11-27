from queue import Queue
from random import randint
from time import sleep

queue = Queue()

class Task:
    """
    Class represents a task to process. 
    Task has its own sequential number. 
    """
    counter = 0

    def __init__(self):
        self.id = Task.counter
        Task.counter += 1

    def __str__(self):
        return f"Task #{self.id}"

    def __repr__(self):
        return f"Task #{self.id}"


def generate_request():
    """
    Add new task to queue
    """
    task = Task()
    print(f"New {task}")
    queue.put(task)

def process_request():
    """
    Process some request from queue
    """
    if queue.qsize() > 0:
        task = queue.get()
        print(f"Processing {task}")
    else:
        print("Queue is empty")


def main():
    """
    Main loop
    """
    actions = [generate_request, process_request]
    print("Press Ctrl+C to exit program.")
    try:
        while True:
            # infinite loop, to be interrupted by Ctrl+C
            sleep(0.5)
            # imitate activity:
            # create new request or process the one from queue
            actions[randint(0,1)]()
    except KeyboardInterrupt:
        print("\n\nExiting program")
        print(f"Queue state: {list(queue.queue)}")

if __name__ == "__main__":
    main()
