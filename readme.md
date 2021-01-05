# What is this?

This is my configuration for [Talon Voice](https://talonvoice.com)

# What does it require?

This assumes that you're using [knausj_talon](https://github.com/knausj85/knausj_talon)

I use [Emacs](https://www.gnu.org/software/emacs/) with the Vi/m emulation mode [Evil](https://github.com/emacs-evil/evil).

Most Vim things should work in Vim.

# What can you do?

* Vim Grammar support (main things are there, including counts, and growing)
  * "Visual Around Word" = "vaw"
    * Creates a selection around a word.
  * "Change Find Letter Uppercase Sit" = "ctI"
    * Delete text up to the letter "I" and enter insert mode.
  * "Wrap On Letter Back Crunch" = "ysFk"
    * Wrap from here to, and including, the letter k with...
  * "Kill In Tag"" = dit"
    * Delete all text in an xml/html tag.
  * "Yank 2 Big Word" = "y2W"
    * Copy from here to 2 whitespace delimited words forward.
  * etc...
* Various Vim commands - The things I use are there, but I'll add more over time. See vim.talon.
* Very basic Emacs Commands
* Some Clojure stuff that needs a lot of work.

# Notes

words.csv contains a list of words on [my website](https://www.admiralbumblebee.com). Just scan all files, remove anything that looks like html, code, etc... throw all the remaining words into a set. Sort that. Print that.

I manually filtered through the words to remove nonsense, then vocabulary.py it into talon.

So this will have a lot of words that probably mean nothing to you, but are meaningful to me.
