from src.ecs.clocks import delta_time
from src.ecs.requirements.has import has


def clean(temporal, destructor):
    temporal.living_time.step(-delta_time())
    if temporal.living_time.value <= 0:
        destructor.clocks_destruction_list.append(temporal)


cleaning = (
    ("temporal" | has("living_time")) * ("destructor" | has("clocks_destruction_list")) >> clean,
)
