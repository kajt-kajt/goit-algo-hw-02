# Let's use linked list to implement stack

class Node:
    """
    Class represents a single node of Linked List
    """
    def __init__(self, symbol:str, next_node = None):
        self.value = symbol
        self.next = next_node

class Stack:
    """
    Stack as Linked List
    """
    def __init__(self):
        self.head = None

    def put(self, symbol:str):
        """
        Add element to stack
        """
        self.head = Node(symbol, self.head)

    def get(self) -> str:
        """
        Get element out of stack
        """
        if self.head:
            result = self.head.value
            self.head = self.head.next
            return result
        return None

    def is_empty(self):
        """
        Return True if stack is empty
        """
        return self.head is None

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += curr.value
            curr = curr.next
        return result
    
OPENING_BRACKETS = "({[<"
CLOSING_BRACKETS = ")}]>"

def analyze_line(line: str) -> bool:
    """
    Analyze line for brackets balance.
    """
    stack = Stack()
    for symbol in line:
        if symbol in OPENING_BRACKETS:
            stack.put(symbol)
        elif symbol in CLOSING_BRACKETS:
            opening_bracket = stack.get()
            if not opening_bracket:
                # stack is empty, but closing bracket was found
                return False
            if OPENING_BRACKETS.index(opening_bracket) != CLOSING_BRACKETS.index(symbol):
                return False
    return stack.is_empty()

def main():
    """
    Main loop
    """
    print("Program analyzes brackets balance. Press Ctrl+C to exit.")
    try:
        while True:
            line = input(">>> ")
            print("Symmetric" if analyze_line(line) else "Not symmetric")
    except KeyboardInterrupt:
        print("\n Exiting program.")


if __name__ == "__main__":
    main()
