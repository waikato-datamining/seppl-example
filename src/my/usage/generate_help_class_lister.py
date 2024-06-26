from my.class_lister_registry import REGISTRY
from seppl import Plugin, generate_help, HELP_FORMAT_MARKDOWN

plugins = REGISTRY.plugins(Plugin)
# this will generate markdown files for each of the plugins in the current directory
generate_help(plugins.values(), help_format=HELP_FORMAT_MARKDOWN, output_path=".")
