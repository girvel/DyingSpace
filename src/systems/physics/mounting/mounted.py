class Mounted:
    def __init__(self, mounting_object, mounting_offset, mounting_force=float('inf')):
        self.mounting_object = mounting_object
        self.mounting_offset = mounting_offset
        self.position = self.mounting_object.position + self.mounting_offset
        self.mounting_force = mounting_force
