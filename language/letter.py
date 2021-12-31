from talon import Module, Context
from talon.grammar import Phrase
from talon.grammar.vm import Capture

# Reusing the phonetic alphabet from https://github.com/knausj85/knausj_talon/ and some code.
# May change in future, thank you to the knausj_talon devs.

alphabet_words = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split(" ")
letters_string = "abcdefghijklmnopqrstuvwxyz"

alphabet_dict = dict(zip(alphabet_words, letters_string))

ctx = Context()
mod = Module()

mod.list("letter", desc="Spoken Alphabet")
ctx.lists["self.letter"] = alphabet_dict

@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)

@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter
