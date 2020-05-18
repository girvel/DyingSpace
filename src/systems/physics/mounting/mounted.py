class Mounted:
    """mounting_object must be Positioned"""
    def __init__(self, mounting_object, mounting_offset, mounting_force=float('inf')):
        self.mounting_object = mounting_object
        self.mounting_offset = mounting_offset
        self.mounting_force = mounting_force

    def union_init(self, union):
        Mounted.mount(union, union.mounting_object)
        union.position = union.mounting_object.position + union.mounting_offset

    def mount(self, parent):
        self.mounting_object = parent

        if not hasattr(self.mounting_object, "mounted_objects"):
            self.mounting_object.mounted_objects = []
        self.mounting_object.mounted_objects.append(self)

