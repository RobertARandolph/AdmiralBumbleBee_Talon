from talon import Context, Module, actions, grammar
from ..knausj_talon.code.user_settings import bind_list_to_csv, bind_word_map_to_csv
import csv
import os

# Default words that need to be remapped.
_word_map_defaults = {
    # E.g:
    # "cash": "cache",

}

_capitalize_defaults = []

# Default words that should be added to Talon's vocabulary.
_simple_vocab_default = []

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'words.csv')
with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        _simple_vocab_default.append(row[0])

# Defaults for different pronounciations of words that need to be added to
# Talon's vocabulary.
_mapping_vocab_default = {}

mod = Module()

mod.list("vocabulary", desc="user vocabulary")

ctx = Context()


_default_word_map = {}
_default_word_map.update(_word_map_defaults)
_default_word_map.update({word.lower(): word for word in _capitalize_defaults})
# "dictate.word_map" is used by `actions.dictate.replace_words` to rewrite words
# Talon recognized. Entries in word_map don't change the priority with which
# Talon recognizes some words over others.
bind_word_map_to_csv(
    "robert_words_to_replace.csv",
    csv_headers=("Replacement", "Original"),
    default_values=_default_word_map,
)

_default_vocabulary = {}
_default_vocabulary.update({word: word for word in _simple_vocab_default})
_default_vocabulary.update(_mapping_vocab_default)
# "user.vocabulary" is used to explicitly add words/phrases that Talon doesn't
# recognize. Words in user.vocabulary (or other lists and captures) are
# "command-like" and their recognition is prioritized over ordinary words.
bind_list_to_csv(
    "user.vocabulary",
    "robert_additional_words.csv",
    csv_headers=("Word(s)", "Spoken Form (If Different)"),
    default_values=_default_vocabulary,
)
