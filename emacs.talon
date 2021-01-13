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

# This is my most common key sequence. Kill active commands, normal mode, save.
reset:
    key(ctrl-g)
    sleep(200ms)
    key(ctrl-[)
    sleep(200ms)
    key(ctrl-x ctrl-s)

# Package added
        
av char:
    key(ctrl-;)

visual replace:
    key(ctrl-c r)

# Buffer

other buffer:
    key(ctrl-x b)

list buffers:
    key(ctrl-x ctrl-b)

(kill | close) buffer:
    key(ctrl-x k enter)

# Windows

other window:
    key(ctrl-x o)

move window:
    key(ctrl-x o m)

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

projectile (find | open) file:
    key(ctrl-x p f)

projectile switch project:
    key(ctrl-x p b)

projectile replace string:
    key(ctrl-x p r)

projectile project root:
    key(ctrl-x p shift-d)

# Magit

magit:
    key(ctrl-x g)

magit file log:
    key(ctrl-c alt-g l)

magit stage file:
    key(ctrl-c alt-g s)

magit unstage file:
    key(ctrl-c alt-g u)

magit diff (buffer | file):
    key(ctrl-c alt-g d)

magit buffer status:
    key(ctrl-c alt-g g)

magit blame:
    key(ctrl-c alt-g shift-b)

magit diff:
    key(ctrl-c alt-g shift-d)

magit commit:
    key(ctrl-c alt-g c)

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