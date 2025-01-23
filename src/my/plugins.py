import argparse
from typing import List

from seppl import Plugin, AliasSupporter


class SomePlugin(Plugin):

    def name(self) -> str:
        return "some-plugin"

    def description(self) -> str:
        return "This description is being used for the argparse description."

    def _create_argparser(self) -> argparse.ArgumentParser:
        parser = super()._create_argparser()
        parser.add_argument("-i", "--input_file", type=str, help="A file to read", required=True)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        super()._apply_args(ns)
        self.input_file = ns.input_file


class OtherPlugin(Plugin):

    def name(self) -> str:
        return "other"

    def description(self) -> str:
        return "Another plugin, this time without any additional command-line arguments."


class Dud(Plugin):

    def name(self) -> str:
        return "dud"

    def description(self) -> str:
        return "Dummy plugin."


class PluginWithAlias(Plugin, AliasSupporter):

    def name(self) -> str:
        return "really-long-winded-name"

    def aliases(self) -> List[str]:
        return ["rlwn"]

    def description(self) -> str:
        return "Plugin with a long default name and a short alias."
