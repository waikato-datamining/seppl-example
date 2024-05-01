from my.class_lister_registry import REGISTRY
from seppl import Plugin

plugins = REGISTRY.plugins(Plugin)
for p in plugins:
    print(plugins[p].name())
