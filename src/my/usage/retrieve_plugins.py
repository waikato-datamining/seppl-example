from my.registry import REGISTRY, ENTRYPOINT_MYPLUGINS
from seppl import Plugin

plugins = REGISTRY.plugins(ENTRYPOINT_MYPLUGINS, Plugin)
for p in plugins:
    print(plugins[p].name())
