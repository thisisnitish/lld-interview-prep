class Snake:
    def __init__(self, head, tail):
        if tail >= head:
            raise ValueError("Invalid Snake: tail should be less than head.")
        self.head = head
        self.tail = tail