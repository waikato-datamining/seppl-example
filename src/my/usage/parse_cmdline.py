from my.registry import REGISTRY, ENTRYPOINT_MYPLUGINS
from seppl import Plugin, split_cmdline, split_args, args_to_objects

cmdline = "other some-plugin -i /some/where/blah.txt dud"
plugins = REGISTRY.plugins(ENTRYPOINT_MYPLUGINS, Plugin)
args = split_args(split_cmdline(cmdline), plugins.keys())
parsed = args_to_objects(args, plugins, allow_global_options=False)
for p in parsed:
    print(p)
