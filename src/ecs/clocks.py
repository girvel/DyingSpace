from time import time, sleep

from src.ecs.special_entities.creator import Creator
from src.ecs.special_entities.destruction import Destructor


class Clocks:
    ups = 50
    current_ups = 1

    class EndGameError(Exception):
        pass

    def __init__(self, *systems):
        self.__systems = [] if systems is None else systems
        self.creator = Creator()
        self.destructor = Destructor()

        self.register_entity(self.creator)
        self.register_entity(self.destructor)

    def __repr__(self):
        return f'{{Clocks: ups={0}, current_ups={1}}}'

    def register_entity(self, entity):
        for system in self.__systems:
            for i, pair in enumerate(system):
                pair.try_add_subject(entity)

    def unregister_entity(self, entity):
        for system in self.__systems:
            for i, pair in enumerate(system):
                pair.try_remove_subject(entity)

    def update(self):
        for system in self.__systems:
            for pair in system:
                pair.execute()

        for e in self.creator.clocks_creation_list:
            self.register_entity(e)

        self.creator.clocks_creation_list.clear()

        for e in self.destructor.clocks_destruction_list:
            self.unregister_entity(e)

        self.destructor.clocks_destruction_list.clear()

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
    return 1 / Clocks.ups
