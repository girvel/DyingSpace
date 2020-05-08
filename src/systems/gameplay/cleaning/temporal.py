from src.tools.limited import Limited


class Temporal:
    def __init__(self, maximal_living_time):
        self.living_time = Limited(maximal_living_time, 0, maximal_living_time)
