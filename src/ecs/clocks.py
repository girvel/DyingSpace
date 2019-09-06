from time import time, sleep


class Clocks:
    ups = 50
    current_ups = 1

    class EndGameError(Exception):
        pass

    def __init__(self, *systems):
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

                Clocks.current_ups = min(1 / t, self.ups)
                sleep(max(0., 1 / self.ups - t))
        except Clocks.EndGameError:
            pass


def delta_time():
    return 1 / Clocks.current_ups
