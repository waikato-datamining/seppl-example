import argparse
from seppl import Plugin, OutputProducer, InputConsumer
from typing import List


class SomeReader(Plugin, OutputProducer):

    def name(self) -> str:
        return "some-reader"

    def description(self) -> str:
        return "This description is being used for the argparse description."

    def generates(self) -> List:
        return [str]

    def _create_argparser(self) -> argparse.ArgumentParser:
        parser = super()._create_argparser()
        parser.add_argument("-i", "--input_file", type=str, help="A text file to read", required=True)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        super()._apply_args(ns)
        self.input_file = ns.input_file


class SomeFilter(Plugin, InputConsumer, OutputProducer):

    def name(self) -> str:
        return "some-filter"

    def description(self) -> str:
        return "This description is being used for the argparse description."

    def accepts(self) -> List:
        return [str]

    def generates(self) -> List:
        return [str]


class SomeWriter(Plugin, InputConsumer):

    def name(self) -> str:
        return "some-writer"

    def description(self) -> str:
        return "This description is being used for the argparse description."

    def accepts(self) -> List:
        return [str]

    def _create_argparser(self) -> argparse.ArgumentParser:
        parser = super()._create_argparser()
        parser.add_argument("-o", "--output_file", type=str, help="The text file to write to", required=True)
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        super()._apply_args(ns)
        self.output_file = ns.output_file
