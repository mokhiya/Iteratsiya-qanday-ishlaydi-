class CustomRange:
    def __init__(self, start=0, end=None, step=1):
        if end is None:
            end = start
            start = 1

        if step == 0:
            raise ValueError("Step must be greater than zero")

        self.step = step
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.end:
            self.current += self.step
            return self.current - self.step
        raise StopIteration
