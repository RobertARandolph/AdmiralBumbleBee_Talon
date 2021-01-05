app.name: Emacs
app.name: Vim
-

[norm] abram:
    key(ctrl-[)

insert:
    key(i)

append:
    key(a)

visual:
    key(v)

<user.vim_command>:
    insert(vim_command)

<user.ex_mode>:
    insert(ex_mode)

# Put

put:
    key(p)

insert (put | paste):
    key(ctrl-r shift-')

# Character changes

replace:
    key("r")

kill:
    key(x)
 
make lower:
    key(g u)

make upper:
    key(g U)


# Visual Mode

select line:
    key(V) 
 
select column:
    key(ctrl-v) 
 
# 2 character commands

(kill | delete) line:
    key(d d)

(start | beginning) of buffer:
   key(g g)

# Insert Mode entry

[insert] line below:
    key(o)

[insert] line above:
    key(O)
    
(append line) | (insert at end of line):
    key(shift-a)
    
prepend line:
    key(shift-i)

# Surround

Surround:
    key(shift-s)

# Search

search:
    key(/)

next result:
    key(n)

previous result:
    key(shift-n)

# Formatting

shift right:
    key(">")

shift left:
    key("<")

# Navigation

page up:
     key(ctrl-u)

page down:
   key(ctrl-d)
   
end of buffer:
   key(shift-g)

# Do things

filter:
    key(shift-1)

undo:
    key(esc u)

redo:
    key(ctrl-r)

# Cursor

last cursor:
    key(ctrl-o)

next cursor:
    key(ctrl-i)

matching:
    key(%)

# Marks

last change:
   key("`")
   key(".")

last insert:
   key(`)
   key(shift-6)

(beginning | start) of yank:
   key(` [)

end of yank:
   key(` ])

mark position <user.letter>:
   key(m)
   key("{letter}")

recall position <user.letter>:
   key(`)
   key("{letter}")

recall line <user.letter>:
   key(')
   key("{letter}")

# Package added
snipe four:
    key(s)

snipe back:
    key(shift-s)

find next:
    key(;)
 
find previous:
    key(,)
