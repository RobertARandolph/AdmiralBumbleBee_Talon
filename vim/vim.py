from talon import Module, Context, actions, app, imgui, grammar
from pathlib import Path
from typing import Any, Union
import re
mod = Module()
ctx = Context()

# Requires this elisp
# (defun write-mode (mode)
#   (with-temp-file "~/.emacs.d/mode"
#     (insert mode)))
# 
# (defun check-evil-state (&optional _)
#   (message "checking")
#   (if (not (minibufferp))
#       (cond
#        ((eq evil-state 'normal) (write-mode "normal"))
#        ((eq evil-state 'insert) (write-mode "insert"))
#        ((eq evil-state 'visual) (write-mode "visual")))))
# 
# (add-hook 'window-buffer-change-functions #'check-evil-state)
# 
# (add-hook 'evil-insert-state-entry-hook
#           (lambda ()
#             (write-mode "insert")))
# 
# (add-hook 'evil-visual-state-entry-hook
#           (lambda ()
#             (write-mode "visual")))
# 
# (add-hook 'evil-normal-state-entry-hook
#           (lambda ()
#             (write-mode "normal")))
def emacs_mode():
    with open(str(Path.home()) + '/.emacs.d/mode', 'r') as reader:
        return reader.readline().strip()


# Entering a mode after an Escape->command-> cycle
vim_mode_key = {"insert": "a", # use a instead of i to get cursor in correct place
                "visual": "v",
                "normal": "esc"}

def switch_normal(reset: int=0):
    print(emacs_mode())
    if emacs_mode() == "insert":
        actions.key("esc")


def normal_mode_command(s: str, reset: int=0):
    """Keys to send in normal mode"""
    cleanup = ""
    print("ESCAPING")
    if reset == 1:
        cleanup = vim_mode_key[emacs_mode()]
    actions.key("esc")
    for i in s.split(" "):
        actions.key(i)
    if cleanup:
        actions.key(cleanup)

@mod.action_class
class Actions:
    def normal_command(s: str, reset: int=0):
        """Keys to send in normal mode"""
        normal_mode_command(s, reset)

# Things I'm ignoring because I don't use them:
# Automatic marks ('<, '', etc..) except a few.
# [[ ]] [] etc... 
# Anything for linewrap
# % - I use da) and it's ilk instead. % as a motion, but not for editing.
# Window moving commands (H, M, L)

def to_str(m: grammar.vm.Capture) -> str:
    return ''.join(str(x) for x in m)

def to_spaced_str(m: grammar.vm.Capture) -> str:
    return ' '.join(str(x) for x in m)

mod.list('vim_text_object_scope', desc='Vim text object scope')
ctx.lists['self.vim_text_object_scope'] = {
    "around": "a",
    "in": "i",
    "surround": "s",
 }

mod.list('vim_text_objects', desc='Vim text objects')
ctx.lists['self.vim_text_objects'] = {
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
    "dubquote": '"',
    "double quote": '"',
    "word": "w",
    "big word": "W",
    "tag": "t",
    "block": "b",
    "big block": "B",
    "paragraph": "p",
    "sentence": "s"
}

# symbol key to support surround, such as ysi)"
@mod.capture(rule='{self.vim_text_object_scope} {self.vim_text_objects} [<user.symbol_key>]')
def vim_text_object(m) -> str:
    return to_spaced_str(m)

mod.list('vim_mark_indicator', desc='Vim mark use command')
ctx.lists['self.vim_mark_indicator'] = {
    "to position": "`",
    "to line": "\'",}

# List for position only
mod.list('vim_mark_target', desc='Vim mark targets')
ctx.lists['self.vim_mark_target'] = {
    "last change": ".",
    "last insert": "^",
    "last exit": "\"",
    "last position": "\'",
    "start of yank": "[",
    "end of yank": "]",
    "next visual": "<",
    "previous visual": ">",
}

@mod.capture(rule='{self.vim_mark_indicator} ({self.vim_mark_target}|<user.letter>)')
def vim_mark_unit(m) -> str:
    return to_spaced_str(m)
    
#############
## Command ##
#############
@mod.capture(rule='<self.vim_mark_unit>')
def vim_mark_command(m) -> str:
    normal_mode_command(to_spaced_str(m), 1)
    return ""

# Operators
mod.list('vim_operators', desc='Vim Grammar verbs')
ctx.lists['self.vim_operators'] = {
    "uppercase": "gU",
    "lowercase": "gu",
    "visual": "v",
    "wrap": "ys",
    "surround": "ys",
    "format": "=",
    "indent": "=",
    "eval": "go",
}

# Operators
mod.list('vim_registerable_operators', desc='Vim Grammar verbs that can enter data into a register')
ctx.lists['self.vim_registerable_operators'] = {
    "change": "c",
    "kill": "d",
    "delete": "d",
    "yank": "y",
}

@mod.capture(rule='[<self.vim_write_register>] {self.vim_registerable_operators}')
def vim_registerable_operators(m) -> str:
    return to_spaced_str(m)

@mod.capture(rule='<self.vim_registerable_operators> | {self.vim_operators}')
def vim_operators(m) -> str:
    return to_spaced_str(m)

#############
## Command ##
#############
@mod.capture(rule='<self.vim_operators> [<user.number_string>] (<user.vim_text_object>|<user.vim_mark_unit>)')
def vim_text_object_command(m) -> str:
    normal_mode_command(to_spaced_str(m), 1)
    return ""

mod.list('vim_motion', desc='Vim motions')
ctx.lists['self.vim_motion'] = {
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
    "end": "e",
    "big end": "E",
    "end back": "ge",
    "end back big": "gE",
    "sentence": "(",
    "sentence back": ")",
    "paragraph": "{",
    "paragraph back": "}",
    "end of line": "g_",
    "newline": "$",
    "start of line": "0",
    "first non blank": "^",
    "first word": "^",
    "beginning of file": "gg",
    "end of file": "G",
    "next": "n",
    "previous": "N",
    "find next": ";",
    "find previous": ","
    # No idea what ]] ][ [[ [] do. Doesn't appear to apply to what I work on.
}

## TODO - parse for modifier-key before returning strings

#############
## Command ##
#############
@mod.capture(rule='^[<user.number_string>] {self.vim_motion}$')
def vim_motion_command(m) -> str:
    normal_mode_command(to_spaced_str(m), 1)
    return "" 

#############
## Command ##
#############
@mod.capture(rule='^[<user.number_string>] <self.vim_operators> <user.vim_motion_command> $')
def vim_operator_motion(m) -> str:
    normal_mode_command(to_spaced_str(m), 1)
    return "" 

# Countable
# Usable with an operator or alone, followed by any character!
mod.list('vim_active_ops', desc='Vim operators that do things on their own')
ctx.lists['self.vim_active_ops'] = {
    "up to": "t",
    "on": "f",
    "up to back": "T",
    "on back": "F"
}

@mod.capture(rule='[ship|uppercase] <user.letter>')
def vim_letter(m) -> str:
    parsed = ""

    if m[0] == "ship" or m[0] == "uppercase":
        l = m.letter.capitalize()
    else:
        l = m.letter

    return str(l)

@mod.capture(rule='{self.vim_active_ops} <self.vim_letter>')
def vim_active_letters(m) -> str:
    return to_spaced_str(m)

@mod.capture(rule='{self.vim_active_ops} <user.symbol_key>')
def vim_active_other(m) -> str:
    if m[1] == "space":
        return m[0] + " "
    else:
        return to_spaced_str(m)

#############
## Command ##
#############
@mod.capture(rule='<self.vim_operators> (<user.vim_active_letters>|<user.vim_active_other>)')
def vim_operator_active(m) -> str:
    normal_mode_command(to_spaced_str(m), 1)
    return ""

#############
## Command ##
#############
@mod.capture(rule='<user.vim_active_letters>|<user.vim_active_other>')
def vim_active(m) -> str:
    normal_mode_command(to_spaced_str(m), 1)
    return ""

# I don't discern between readable/writeable registers in captures
# because this is not linked to a specific command
# but they are separated here in case I wish to change that
mod.list('vim_write_registers', desc='Registers')
ctx.lists['self.vim_write_registers'] = {
    "black hole": "_",
    "clipboard": "+",
}

mod.list('vim_read_registers', desc='Registers')
ctx.lists['self.vim_read_registers'] = {
    "unnamed": "\"",
    "small delete": "-",
    "small kill": "-",
    "last search": "/",
    "last inserted": ".",
    "file name": "%",
    "other file name": "#",
    "last command": ":",
    "clipboard": "+",
}

# I don't combine this with other commands because I frequently pause after using the register
@mod.capture(rule='register ({user.vim_read_registers}|{user.vim_write_register}|<user.number_string>|<self.vim_letter>)') 
def vim_read_register(m) -> str:
    return str("\" " + m[1])

# I don't combine this with other commands because I frequently pause after using the register
@mod.capture(rule='register ({user.vim_write_registers}|<self.vim_letter>)') 
def vim_write_register(m) -> str:
    return str("\" " + m[1])

def put_command(r: [str, None]):
    """Keys to send in normal mode"""    
    register = ""
    if r is not None:
        register = r

    if emacs_mode() == "insert":
        actions.key("ctrl-r")
        actions.insert(register[1:].replace(" ", ""))
    else:
        actions.insert(register.replace(" ", ""))
        actions.key("p")

#############
## Command ##
#############
@mod.capture(rule='put [<self.vim_read_register>]') 
def vim_put(m) -> str:
    if hasattr(m, 'vim_read_register'):
        put_command(m.vim_read_register)
    else:
        put_command(None)
    return ""

@mod.capture(rule="go to line <user.number_string>")
def ex_mode(m) -> str:
    parsed = ""
    actions.insert(f":{m.number_string}")
    actions.key("enter")
    return ""

