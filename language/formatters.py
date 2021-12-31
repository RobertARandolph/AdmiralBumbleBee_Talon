from talon import Module, Context
from talon.grammar import Phrase
from talon.grammar.vm import Capture
from inspect import getmembers, isfunction
from user.robert_talon.language import formatter_fns
from user.robert_talon.language import substitutions
    
# Acquire a list of formatter functions. The fn names are the trigger words
formatters_list = dict(getmembers(formatter_fns, isfunction))

ctx = Context()
mod = Module()

mod.list('formatter_dict', desc='formatter mapping')
# create a 1:1 dict of fn name: fn name as strings. Talon doesn't like str: fn
ctx.lists["self.formatter_dict"] = {k: k for (k , v) in formatters_list.items()}

@mod.capture(rule="^({self.formatter_dict}) (<phrase>)+")
def formatters(m: Capture) -> str:
    "call formatter with m"
    return substitutions.substitute(formatters_list[m.formatter_dict](m))
