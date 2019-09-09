class Limited:
    def __init__(self, value, min_value=float("-inf"), max_value=float("inf")):
        self.max_value = max_value
        self.min_value = min_value
        self.value = value

    def cycled_step(self, size, final_action=lambda: None):
        self.value += size
        while self.value > self.max_value:
            self.value -= self.max_value
            final_action()

    def step(self, size):
        self.value = max(
            min(self.value + size,
                self.max_value
            ),
            self.min_value
        )

    def reset_min(self):
        self.value = self.min_value

    def to_proportion(self):
        return (self.value - self.min_value) / (self.max_value - self.min_value)
