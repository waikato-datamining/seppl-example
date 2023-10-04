from my.registry import REGISTRY, ENTRYPOINT_MYPLUGINS
from seppl import Plugin, output_help, HELP_FORMAT_MARKDOWN

plugins = REGISTRY.plugins(ENTRYPOINT_MYPLUGINS, Plugin)
# this will generate markdown files for each of the plugins in the current directory
output_help(plugins.values(), help_format=HELP_FORMAT_MARKDOWN, output=".")
