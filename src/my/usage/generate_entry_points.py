from my.registry import REGISTRY, ENTRYPOINT_MYPLUGINS
from seppl import Plugin, generate_entry_points

# at development time, the entry_point group is irrelevant
# you can use the class for filtering instead
# (Plugin is the top-most class and will capture all in
# the defined default modules)
plugins = REGISTRY.plugins("", Plugin).values()
entry_points = {
    ENTRYPOINT_MYPLUGINS: plugins
}
print(generate_entry_points(entry_points))
