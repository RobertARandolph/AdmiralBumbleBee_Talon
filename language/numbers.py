from talon import Module, Context
from talon.grammar import Phrase
from talon.grammar.vm import Capture

ones = "zero one two three four five six seven eight nine".split()
teens = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
tens = "twenty thirty forty fifty sixty seventy eighty ninety".split()

# tens from 20-99
fill_tens = {}
for i, t in enumerate(tens):
    for j, o in enumerate(ones[1:]):
        fill_tens.update({f"{t} {o}": str (((i+2)*10) + j + 1)})

ones_dict = {x: str(i) for i, x in enumerate(ones)}

tens_dict = {x: str (i+10) for i, x in enumerate(teens)}
tens_dict.update({x: str ((i+2)*10) for i, x in enumerate(tens)})  # i+2 because list starts at 20
tens_dict.update(fill_tens)

sub_hundred = ones_dict
sub_hundred.update(tens_dict)

ctx = Context()
mod = Module()

mod.list('ones', desc='0-9')
ctx.lists["self.ones"] = ones_dict

mod.list('tens', desc='10-99')
ctx.lists["self.tens"] = ones_dict

mod.list('sub_hundred', desc='0-99')
ctx.lists["self.sub_hundred"] = sub_hundred

@mod.capture(rule="{self.sub_hundred}")
def sub_hundred(m: Capture) -> str:
    return str(m.sub_hundred)

@mod.capture(rule="{self.ones} hundred")
def hundreds(m: Capture) -> str:
    return str(m.ones + "00")

@mod.capture(rule="{self.ones} hundred and* {self.tens}")
def sub_thousand(m: Capture) -> str:
    if int(m.tens) < 10:
        s = str(m.ones + "0" + m.tens)
    else:
        s = str(m.ones + m.tens)
    return s

@mod.capture(rule="<self.sub_thousand>|<self.hundreds>")
def over_hundred(m: Capture) -> str:
    return str(m)

@mod.capture(rule="<self.sub_hundred>|<self.hundreds>|<self.sub_thousand>")
def number_string(m: Capture) -> str:
    return str(m)
