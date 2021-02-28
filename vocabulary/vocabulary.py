from talon import Context, Module, actions, grammar, fs
from ...knausj_talon.code.user_settings import bind_list_to_csv, bind_word_map_to_csv
import csv
import os

mod = Module()
ctx = Context()

#ctx.lists['user.vocabulary'] = { "datum": "poop" }

#mod.list('beecabulary', desc="additional beecabulary words")
#

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'word_map.csv')

robert_vocab = {}

def _update_vocab(*_):
    global robert_vocab

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] != '':
                robert_vocab.update({row[0]: row[1]})
            else:
                robert_vocab.update({row[0]: row[0]})
    ctx.lists['user.vocabulary'] = robert_vocab
    print(robert_vocab)            

_update_vocab()
fs.watch(str(dirname), _update_vocab)

#
##print(f"{_default_vocabulary}")
#
##ctx.settings["dictate.word_map"] = _default_vocabulary
#
#no_space_before = set("\n .,!?;:-/%)]}")
#no_space_after = set("\n -/#([{$£€¥₩₽₹")
#def format_phrase(m):
#    words = capture_to_word_list(m)
#    result = ""
#    for i, word in enumerate(words):
#        if i > 0 and word not in no_space_before and words[i - 1][-1] not in no_space_after:
#            result += " "
#        result += word
#    return result
#
#def capture_to_word_list(m):
#    words = []
#    for item in m:
#        words.extend(
#            actions.dictate.replace_words(actions.dictate.parse_words(item))
#            if isinstance(item, grammar.vm.Phrase) else
#            item.split(" "))
#    return words
#
#@mod.capture(rule="({self.beecabulary} | <word>)")
#def word(m) -> str:
#    print("beecab")
#    try:
#        return m.beecabulary
#    except AttributeError:
#        return " ".join(actions.dictate.replace_words(actions.dictate.parse_words(m.word)))
#
#@mod.capture(rule="({self.beecabulary} | <phrase>)+")
#def text(m) -> str: return format_phrase(m)
#
#@mod.capture(rule="({self.beecabulary} | {user.punctuation} | <phrase>)+")
#def prose(m) -> str: return format_phrase(m)

## Defaults for different pronounciations of words that need to be added to
## Talon's vocabulary.
#_mapping_vocab_default = {}
#
#
#mod.list("vocabulary", desc="user vocabulary")
#
#
#_default_word_map = {}
#_default_word_map.update(_word_map_defaults)
##_default_word_map.update({word.lower(): word for word in _capitalize_defaults})
## "dictate.word_map" is used by `actions.dictate.replace_words` to rewrite words
## Talon recognized. Entries in word_map don't change the priority with which
## Talon recognizes some words over others.
#bind_word_map_to_csv(
    #"robert_words_to_replace.csv",
    #csv_headers=("Replacement", "Original"),
    #default_values=_default_word_map,
#)
#
#_default_vocabulary = {}
#_default_vocabulary.update({word: word for word in _simple_vocab_default})
##_default_vocabulary.update(_mapping_vocab_default)
## "user.vocabulary" is used to explicitly add words/phrases that Talon doesn't
## recognize. Words in user.vocabulary (or other lists and captures) are
## "command-like" and their recognition is prioritized over ordinary words.
#bind_list_to_csv(
    #"user.vocabulary",
    #"robert_additional_words.csv",
    #csv_headers=("Word(s)", "Spoken Form (If Different)"),
    #default_values=_default_vocabulary,
#)
