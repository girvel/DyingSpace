class Animated:
    def __init__(self, dict_):
        self.__dict = dict_

    def __repr__(self):
        return f'{{Animated: {len(self.__dict)} animations}}'
