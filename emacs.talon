app.name: Emacs
-

# Talon things

^return$:
    key("enter")
   
# Emacs things

emacs escape:
    key(ctrl-g)
   
m down:
    key(ctrl-n)

m up:
    key(ctrl-p)

meta up:
    key(alt-p)

meta down:
    key(alt-n)

find file:
    key(ctrl-x ctrl-f)

meta command:
    key(alt-x)

# commonly used to 'finish' an action
emacs go:
    key(ctrl-c ctrl-c)

# This is my most common key sequence. Kill active commands, normal mode, save.
reset:
    key(ctrl-g)
    sleep(200ms)
    key(ctrl-[)
    sleep(200ms)
    key(ctrl-x ctrl-s)

# Package added
        
jump <user.letter> <user.letter>:
    key(cmd-f)
    sleep(200ms)
    key(letter)
    key(letter_2)

visual replace:
    key(ctrl-c r)

# Buffer

other buffer:
    key(ctrl-x b)

last buffer:
    key(ctrl-x b)
    key(enter)

list buffers:
    key(ctrl-x ctrl-b)

(kill | close) buffer:
    key(ctrl-x k enter)

# Windows

other window:
    key(cmd-m)

move window:
    key(cmd-m m)

close window:
    key(ctrl-x 0)

split horizontal:
    key(ctrl-x 2)

split vertical:
    key(ctrl-x 3)

# file operations

emacs save:
    key(ctrl-x ctrl-s)

# Project Wide

grep:
    key(ctrl-c k)

projectile file:
    key(cmd-p f)

projectile project:
    key(cmd-p p)

projectile replace string:
    key(cmd-cmd-p r)

projectile project root:
    key(cmd-p shift-d)

# Magit

maggot:
    key(cmd-g)

maggot file log:
    key(ctrl-c alt-g)
    sleep(200ms)
    key(l)

maggot stage file:
    key(ctrl-c alt-g)
    sleep(200ms)
    key(s)

maggot unstage file:
    key(ctrl-c alt-g)
    sleep(200ms)
    key(u)

maggot diff (buffer | file):
    key(ctrl-c alt-g)
    sleep(200ms)
    key(d)

maggot buffer status:
    key(ctrl-c alt-g)
    sleep(200ms)
    key(g)

maggot blame:
    key(ctrl-c alt-g)
    sleep(200ms)
    key(shift-b)

maggot diff:
    key(ctrl-c alt-g)
    sleep(200ms)
    key(shift-d)

maggot commit:
    key(ctrl-c alt-g)
    sleep(200ms)
    key(c)

# Org-mode

org expand all:
    key(ctrl-u ctrl-u ctrl-u tab)

org toggle links:
    key(alt-x)
    insert("org-toggle-link-display")
    key(enter)

# Company Mode

complete:
    key(ctrl-f)

# Cider

cider jack in:
    key(ctrl-c)
    key(alt-j)

# Lisp

eval top:
    key(ctrl-alt-x)

eval last:
    key(ctrl-x ctrl-e)

eval top print:
    key(ctrl-shift-alt-x)