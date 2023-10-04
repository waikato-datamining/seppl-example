from my.registry import REGISTRY
from seppl import Plugin

plugins = REGISTRY.plugins("myplugins", Plugin)
for p in plugins:
    print(plugins[p].name())
