-

(cursor laptop|left) | (left display|monitor):
    key(ctrl-left)

(cursor center) | (center display|monitor):
    key(ctrl-down)

(cursor right) | (right display|monitor):
    key(ctrl-right)

[open|view] iterm:
    key(alt-space)

moon right:
    key(ctrl-cmd-r)

moon full:
    key(ctrl-cmd-f)

moon lower left:
    key(ctrl-cmd-3)

moon upper left:
    key(ctrl-cmd-2)

moon left:
    key(ctrl-cmd-1)

moon move right:
    key(ctrl-cmd-0)

moon move left:
    key(ctrl-cmd-9)

Alfred <phrase>$:
    key(cmd-space)
    sleep(250ms)
    insert(phrase)
    key(enter)

dot hypertext:
    insert(".html")

# Apparently "sege" is how I say "clj"?
sege:
    insert("clj")

# Language Modes

^set closure: user.code_set_language_mode("clojure")