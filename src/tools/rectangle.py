class Rectangle:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, v, r=0):
        return v.x + r > self.start.x \
            and v.y + r > self.start.y \
            and v.x - r < self.end.x \
            and v.y - r < self.end.y

    def __contains__(self, item):
        return self.contains(item)
