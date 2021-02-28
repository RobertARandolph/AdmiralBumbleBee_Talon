# What is this?

This is my configuration for [Talon Voice](https://talonvoice.com)

# What does it require?

This assumes that you're using [knausj_talon](https://github.com/knausj85/knausj_talon)

I use [Emacs](https://www.gnu.org/software/emacs/) with the Vi/m emulation mode [Evil](https://github.com/emacs-evil/evil).

Most Vim things should work in Vim.

I use [Vimium in Chrome](https://github.com/philc/vimium/blob/master/README.md), so vimium.org has full support for vimium usage. It should mostly mirror vim usage, and I'll improve that over time.

# What can you do?

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
  * Registers - most evil registers supported
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
* Very basic Emacs Commands
* Some Clojure stuff that needs a lot of work.

## REAPER

See [the first article about this](https://admiralbumblebee.com/music/2021/01/18/Reaper-Day-24.html) or [the first video](https://youtu.be/xAbigyf6OQ0)

REAPER setup requires [SWS Extensions](https://www.sws-extension.org), and my setup [as explored in this series](https://admiralbumblebee.com/music/2020/11/19/Starting-over-with-Reaper.html).

# Notes

words.csv contains a list of words on [my website](https://www.admiralbumblebee.com). Just scan all files, remove anything that looks like html, code, etc... throw all the remaining words into a set. Sort that. Print that.

I manually filtered through the words to remove nonsense, then vocabulary.py it into talon.

So this will have a lot of words that probably mean nothing to you, but are meaningful to me.
