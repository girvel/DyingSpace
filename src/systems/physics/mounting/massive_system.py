class MassiveSystem:
    """Requires Mounted, Massive and Massive .mounting_object"""
    def union_init(self, union):
        parent = union.mounting_object
        union.system_mass = union.mass + (parent.system_mass if hasattr(parent, "system_mass") else parent.mass)
        update_mass(union.mounting_object, union.system_mass)


def update_mass(union, value):
    union.system_mass = value
    if hasattr(union, "mounting_object"):
        update_mass(union.mounting_object, value)

    if hasattr(union, "mounted_objects"):
        for u in union.mounted_objects:
            if not hasattr(u, "system_mass") or union.system_mass != value:
                update_mass(u, value)
