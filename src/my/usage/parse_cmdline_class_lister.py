from my.class_lister_registry import REGISTRY
from seppl import Plugin, split_cmdline, split_args, args_to_objects

cmdline = "other some-plugin -i /some/where/blah.txt dud"
plugins = REGISTRY.plugins(Plugin)
args = split_args(split_cmdline(cmdline), plugins.keys())
parsed = args_to_objects(args, plugins, allow_global_options=False)
for p in parsed:
    print(p)
