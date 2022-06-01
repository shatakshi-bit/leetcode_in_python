class OrderedStream:

    def __init__(self, n: int):
        self.stream = [''] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        self.chunks = []
        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            print(self.stream[self.ptr])
            self.chunks.append(self.stream[self.ptr])
            self.ptr += 1
        return self.chunks