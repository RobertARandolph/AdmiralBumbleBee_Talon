import csv
import re
from talon import Module, Context, actions, grammar
from talon.grammar import Phrase
from talon.grammar.vm import Capture

with open('user/robert_talon/translations/substitutions.csv', mode='r') as f:
    reader = csv.reader(f)
    custom_substitutions = {rows[0]: rows[1] for rows in reader}


print(f"{custom_substitutions}")

def substitute(s: str) -> str:
    ret = s
    the_replacements = []
    
    for k, v in custom_substitutions.items():
        # keep a list of matches for later undo with UI
        # must be run after any replacements
        ret = ret.replace(k, v)
        print(f"Replacing {k} with {v}")

        for m in re.finditer(re.compile(v), ret):
            n = {"start": m.start(),
                 "end": m.end(),
                 "match": m.group(0)}
            the_replacements.append(n.copy())

    print(f"{the_replacements}")
    return ret
