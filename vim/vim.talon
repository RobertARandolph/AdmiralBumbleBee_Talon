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

<user.vim_text_object_command>:
    insert(user.vim_text_object_command)

<user.vim_mark_unit>:
    insert(user.vim_mark_unit)

<user.vim_motion_command>:
    insert(user.vim_motion_command)
    
<user.vim_operator_motion>:
    insert(user.vim_operator_motion)

<user.vim_operator_active>:
    insert(user.vim_operator_active)

<user.vim_active>:
    insert(user.vim_active)

<user.main_cap>:
    insert(user.main_cap)

<user.ex_mode>:
    insert(ex_mode)

# Put

put:
    user.put_command()

# Character changes

replace:
    user.normal_command("r")

kill:
    user.normal_command("x")

kill back:
    user.normal_command("x")

# Visual Mode

select line:
     user.normal_command("shift-v", 0)
 
select column:
    user.normal_command("ctrl-v", 0)
 
# 2 character commands

(kill | delete) line:
    user.normal_command("d d")

<user.number_string> (kill | delete) line:
    user.normal_command("{number_string} d d")

yank line:
    user.normal_command("y y", 1)

start of buffer:
   user.normal_command("g g")

# Insert Mode entry

[insert] line below:
    user.normal_command("o")

[insert] line above:
    user.normal_command("O")
    
(append line) | (insert at end of line):
    key(shift-a)
    
prepend line:
    user.normal_command("shift-i")

# Surround

Surround:
    key(shift-s)

# Search

search:
    user.normal_command("/")

next:
    user.normal_command("n")

previous:
    user.normal_command("shift-n")

# Formatting

shift right:
    user.normal_command(">")

shift left:
    user.normal_command("<")

# Navigation

page up:
   user.normal_command("ctrl-u")

page down:
   user.normal_command("ctrl-d")
   
end of buffer:
   user.normal_command("shift-g")

# Do things

filter:
    key(shift-1)

undo:
    user.normal_command("u")

redo:
    user.normal_command("ctrl-r")

# Cursor

last cursor:
    user.normal_command("ctrl-o")

next cursor:
    user.normal_command("ctrl-i")

matching:
    user.normal_command("%")

other (end | side) [of visual]:
   key(o)

# Marks

last change:
   user.normal_command("` .")

last insert:
   user.normal_command("` ^")

start of yank:
   user.normal_command("` [")

end of yank:
   user.normal_command("` ]")

mark position <user.letter>:
   user.normal_command("m {letter}")

recall position <user.letter>:
   user.normal_command("` {letter}")

recall line <user.letter>:
   user.normal_command("' {letter}")

# Package added
snipe four:
    user.normal_command("s")

snipe back:
    user.normal_command("shift-s")

find next:
    user.normal_command(";")
 
find previous:
    user.normal_command(",")

toggle case:
    user.normal_command("shift-`")