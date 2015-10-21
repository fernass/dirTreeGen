__author__ = 'fernass daoud'

from argparse import ArgumentParser

class CommandlineParser:
    def __init__(self):
        parser = ArgumentParser(description="This Program is a Directory Tree Generator. \
        The Rules are defined in extra Input File", usage="dirTreeGen inputfile")

        parser.add_argument("inputfile", type=str)
        self.args = parser.parse_args()
        #print(self.args.inputfile)
        del(parser)
        return None
