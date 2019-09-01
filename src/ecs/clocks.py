from time import time, sleep


class Clocks:
    class EndGameError(Exception):
        pass

    def __init__(self, *systems, ups=50):
        self.ups = ups
        self.__systems = [] if systems is None else systems

    def register_entity(self, entity):
        for system in self.__systems:
            for i, pair in enumerate(system):
                pair.try_add_subject(entity)

    def update(self):
        for system in self.__systems:
            for pair in system:
                pair.execute()

    def mainloop(self):
        try:
            while True:
                t = time()
                self.update()
                t = time() - t

                sleep(max(0., 1 / self.ups - t))
        except Clocks.EndGameError:
            pass
