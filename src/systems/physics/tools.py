def distance_vector(from_, to):
    result = to.position - from_.position

    if hasattr(from_, "radius"):
        result *= (1 - from_.radius / abs(result))

    if hasattr(to, "radius"):
        result *= (1 - to.radius / abs(result))

    return result