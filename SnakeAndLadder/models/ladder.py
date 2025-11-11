class Ladder:
    def __init__(self, start, end):
        if start >= end:
            raise ValueError("Invalid Ladder: start should be less than end.")
        self.start = start
        self.end = end