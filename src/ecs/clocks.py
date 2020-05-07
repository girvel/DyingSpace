import os
from pathlib import Path
from time import time, sleep

from src.ecs.special_entities.creator import Creator
from src.ecs.special_entities.destruction import Destructor


class Clocks:
    ups = 50
    current_ups = 1

    class EndGameError(Exception):
        pass

    def __init__(self, debug_mode=False, *systems):
        self.__systems = [] if systems is None else systems
        self.creator = Creator()
        self.destructor = Destructor()

        self.register_entity(self.creator)
        self.register_entity(self.destructor)

        self.debug_mode = debug_mode
        if self.debug_mode:
            self.debug_subsystems_time = [[0] * len(s) for s in self.__systems]
            self.debug_total_frames = 0

    def __repr__(self):
        return f'{{Clocks: ups={0}, current_ups={1}}}'

    def register_entity(self, entity):
        for system in self.__systems:
            for i, pair in enumerate(system):
                pair.try_add_subject(entity)
        entity.registered = True

    def unregister_entity(self, entity):
        for system in self.__systems:
            for i, pair in enumerate(system):
                pair.try_remove_subject(entity)
        entity.registered = False

    def update(self):
        if self.debug_mode:
            self.debug_total_frames += 1

            for i, system in enumerate(self.__systems):
                for j, pair in enumerate(system):
                    t = time()
                    pair.execute()
                    t = time() - t

                    self.debug_subsystems_time[i][j] += t
        else:
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
        finally:
            path = Path(os.getenv('APPDATA'), 'DyingSpace')

            if not path.exists():
                path.mkdir()

            with Path(path, 'latest_systems_statistics.txt').open('w') as f:
                for system_data in self.debug_subsystems_time:
                    for value in system_data:
                        f.write(str(round(value * self.ups / self.debug_total_frames, 4)) + '\n')
                    f.write('\n')


def delta_time():
    return 1 / Clocks.ups
