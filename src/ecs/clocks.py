class Clocks:
    def __init__(self, systems=None):
        self.__systems = [] if systems is None else systems

    def register_entity(self, entity):
        for system in self.__systems:
            for i, requirement in system.requirements:


            # required_part = (entity.get_component(component_type) for component_type in system.requirements)
            #
            # if all(c is not None for c in required_part):
            #     system.__subjects.append(required_part)

    def update(self):
        for system in self.__systems:
            system.update()
