import csv
import re
from typing import List
from talon import Module, Context, actions, grammar, imgui, ui
from talon.grammar import Phrase
from talon.grammar.vm import Capture
from user.robert_talon.utils import list_utils

mod = Module()
mod.mode("substitutions")

with open('user/robert_talon/translations/substitutions.csv', mode='r') as f:
    reader = csv.reader(f)
    custom_substitutions = {rows[0]: rows[1] for rows in reader}

# Throw all keys in a compiled regex like (item1|item2|item3)

subs = ""

substitution_items = list(custom_substitutions.items())
subs = "(" + substitution_items[0][0] + ")"

i = 1
while i < len(substitution_items):
   subs += "|(\\b" + substitution_items[i][0] + "\\b)"
   i += 1

compiled_sub_regex = re.compile(subs)

print(f'{subs}')
# Build substitution list

# map of dicts of the last replacements
last_replacements = []
# last phrase _inserted_, not spoken (for backspacing when subbing)
last_phrase = ""
# List of full sub options
last_sub_options = []

def create_subs(l: List, s: str) -> List[str]:
    ret = []
    for replacement in l:
        cur_replacement = s
        cur_diff = 0
        for x in replacement:
            to_sub = custom_substitutions[x["match"]]

            # use diff from previous subs
            start = x["start"] + cur_diff
            end = x["end"] + cur_diff
            cur_replacement = cur_replacement[:start] + to_sub + cur_replacement[end:]

            # store offset if matches differ in size, necessary for substitutions later in the string
            replacing = cur_replacement[start:end]
            cur_diff = len(to_sub) - len(replacing)

        ret.append(cur_replacement)
    return ret

def substitute(s: str) -> str:
    global last_replacements
    global last_phrase
    global last_sub_options
    last_replacements = []
 
    for m in re.finditer(compiled_sub_regex, s):
         n = {"start": m.start(),
              "end": m.end(),
              "match": m.group(0)}
         last_replacements.append(n.copy())

    last_phrase = str(s)

    if last_replacements is not None:

        # get all combinations of replacements
        combinations = list_utils.subsets(last_replacements)

        # perform all replacements and store in list of strings
        sub_list = create_subs(combinations, last_phrase)
        last_sub_options = sub_list

        show_substitutions()
    
    return s

main_screen = ui.main_screen()

def show_substitutions():
    actions.mode.enable("user.substitutions")
    gui.show()

@mod.action_class
class Actions:
    def hide_substitutions():
        """Hide Substitutions window"""
        actions.mode.disable("user.substitutions")
        gui.hide()
    def select_substitution():
        """Select a specific option"""

@imgui.open(x=main_screen.x + main_screen.width / 2.6, y=main_screen.y)
def gui(gui: imgui.GUI):
    gui.text(last_phrase)
    gui.text("-"*len(last_phrase))
    for i, s in enumerate(last_sub_options):
        gui.text(f'{i}: {s}')

@mod.capture(rule="select <self.number_string>")
def select_substitution(m: Capture) -> str:
    global last_phrase

    for x in range(len(last_phrase)):
        actions.key("backspace")

    actions.insert(last_sub_options[int(m.number_string)])
    hide_substitutions()
    return ""
