# What is this?

This is my configuration for [Talon Voice](https://talonvoice.com)

# What does it require?

This assumes that you're using [knausj_talon](https://github.com/knausj85/knausj_talon)

I use [Emacs](https://www.gnu.org/software/emacs/) with the Vi/m emulation mode [Evil](https://github.com/emacs-evil/evil).

Most Vim things should work in Vim.

I use [Vimium in Chrome](https://github.com/philc/vimium/blob/master/README.md), so vimium.org has full support for vimium usage. It should mostly mirror vim usage, and I'll improve that over time.

# What can you do?

Most of these commands know if emacs is in insert or normal mode, and acts accordingly. You can say "delete up to fine" while in insert mode and it will jump to normal mode, delete up to "f" and go back into insert.

* Vim Grammar support (main things are there, including counts, and growing)
  * "Visual Around Word" = "vaw"
    * Creates a selection around a word.
  * "Change To Uppercase Sit" = "ctI"
    * Delete text up to the letter "I" and enter insert mode.
  * "Wrap On Letter Back Crunch" = "ysFk"
    * Wrap from here to, and including, the letter k with...
  * "Kill In Tag"" = dit"
    * Delete all text in an xml/html tag.
  * "Yank 2 Big Word" = "y2W"
    * Copy from here to 2 whitespace delimited words forward.
  * "Change surround angle left paren" - cs>(
    * Change the nearest surrounding <> to () without affecting other text.
  * etc...
  * Registers - most evil registers supported, uses correct command automatically for insert/normal
    * "register black hole change up to ship fine" - "_ctF
      * Change from here to the next capital F, do not clobber the kill ring with the killed text.
    * "register cap yank around sentence" - "cyas
      * Put the "sentence" (could language/mode dependent) into the register c.
    * "put register drum" - "dp
      * Put the contents of register d.
    * "put register file name" - "%p
      * Put the current file name.

* Various Vim commands - The things I use are there, but I'll add more over time. See vim.talon.
  * "Search selected" - yq/p
    * Search for the current visually selected text (using q/ command mode)
  * Full Mark support
    * "Last change" - `.
      * Jump to last change
    * "Mark position Drum" - md
      * Mark current position in position d
    * Marks work with text objects
      * "yank to position red" - y`r
        * yank all text to position r
* Moderate [Vimium](https://vimium.github.io) support
* Very basic Emacs Commands
* Some Clojure stuff that needs a lot of work.
* lispyville stuff in progress

## VIM

Documentation form: "word": "key-press",

### Operators that work with a register:

"change": "c",
"kill": "d",
"delete": "d",
"yank": "y",

### Operators which do not work with a register:

"uppercase": "g U",
"lowercase": "g u",
"visual": "v",
"wrap": "y s",
"surround": "y s",
"format": "=",
"indent": "=",
"eval": "go",

### Motions that work on their own (no operator/object needed):

"up": "k",
"down": "j",
"left": "h",
"right": "l",
"down non blank": "+",
"up non blank": "-",
"word": "w",
"big word": "W",
"back": "b",
"big back": "B",
"end word": "e",
"big end word": "E",
"end back": "ge",
"end back big": "g E",
"sentence": "(",
"sentence back": ")",
"paragraph": "{",
"paragraph back": "}",
"end of line": "g_",
"newline": "$",
"start of line": "0",
"first non blank": "^",
"first word": "^",
"beginning of file": "g g",
"end of file": "G",
"next": "n",
"previous": "N",
"find next": ";",
"find previous": ","

### Motions that do not work on their own (operator/object needed):

"up to": "t",
"on": "f",
"up to back": "T",
"on back": "F"


### Scope

Scope for operator _____ object

"around": "a",
"in": "i",
"surround": "s",

### Mark indicator (mark scope trigger)

Used as a scope for marks i.e. "Delete to position last change"

"to position": "`",
"to line": "\'"

### Text Objects:

"quote": "'",
"L square": "[",
"left square": "[",
"square": "[",
"R square": "]",
"right square": "]",
"paren": ")",
"L paren": "(",
"left paren": "(",
"R paren": ")",
"right paren": ")",
"brace": "}",
"left brace": "{",
"R brace": "}",
"right brace": "}",
"angle": ">",
"left angle": "<",
"less than": "<",
"rangle": ">",
"R angle": ">",
"right angle": ">",
"greater than": ">",
"dubquote": '",
"double quote": '",
"word": "w",
"big word": "W",
"tag": "t",
"block": "b",
"big block": "B",
"paragraph": "p",
"sentence": "s"

### Mark Targets

Text objects for marks. Letters are also mark targets.

"last change": ".",
"last insert": "^",
"last exit": "\"",
"last position": "\'",
"start of yank": "[",
"end of yank": "]",
"next visual": "<",
"previous visual": ">",

### Mark Indicators

"to position": "`",
"to line": "\'"

### Special registers to write to (not letters):

"black hole": "_",
"clipboard": "+",

### Special registers to read from (not letters):

"unnamed": "\"",
"small delete": "-",
"small kill": "-",
"last search": "/",
"last inserted": ".",
"file name": "%",
"other file name": "#",
"last command": ":",
"clipboard": "+",

## REAPER

See [the first article about this](https://admiralbumblebee.com/music/2021/01/18/Reaper-Day-24.html) or [the first video](https://youtu.be/xAbigyf6OQ0)

REAPER setup requires [SWS Extensions](https://www.sws-extension.org), and my setup [as explored in this series](https://admiralbumblebee.com/music/2020/11/19/Starting-over-with-Reaper.html).

# Notes

words.csv contains a list of words on [my website](https://www.admiralbumblebee.com). Just scan all files, remove anything that looks like html, code, etc... throw all the remaining words into a set. Sort that. Print that.

I manually filtered through the words to remove nonsense, then vocabulary.py it into talon.

So this will have a lot of words that probably mean nothing to you, but are meaningful to me.

