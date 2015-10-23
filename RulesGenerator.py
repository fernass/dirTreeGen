import os

__author__ = 'fernass daoud'


class Rule:
    def __init__(self, line, line_no):
        self.prefix = ""
        keys = line.split("-")
        if keys[0].isalpha():
            self.prefix = keys[0]
            del(keys[0])

        if len(keys) < 2:
            raise SyntaxError("Only one Argument on line {}. At least two Expected".format(line_no))
        elif len(keys) > 3:
            raise SyntaxError("More Than Three Arguments on line {}. At Maximum Three Expected".format(line_no))
        elif len(keys) == 2:
            try:
                self.start = int(keys[0].strip())
                self.end = int(keys[1].strip())
                self.incr = 1
            except:
                raise SyntaxError("None Integer Values on Line No. {} of Input File".format(line_no))
        else:
            try:
                self.start = int(keys[0].strip())
                self.end = int(keys[1].strip())
                self.incr = int(keys[2].strip())
            except:
                raise SyntaxError("None Integer Values on Line No. {} of Input File".format(line_no))

        return


class RulesGenerator:
    def __init__(self, cmd_obj):
        try:
            self.file = open(cmd_obj.args.inputfile, mode='r')
        except:
            print("Can't access input file!")
            raise PermissionError("Either Access Rights are Granted, or File is not Available")

        self.rules = list()
        return

    def generate(self):
        self.file.seek(0)
        line_no = 0
        for line in self.file:
            line_no += 1
            if line.find("#") == 0:
                continue
            new_rule = Rule(line, line_no)
            self.rules.append(new_rule)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.rules):
            self.index += 1
            return self.rules[self.index - 1]
        else:
            raise StopIteration

    def apply(self):
        for R in self:
            for directory in range(R.start, R.end, R.incr):
                os.mkdir(R.prefix + str(directory), mode=0o775)
        return
