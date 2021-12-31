from talon import Module, Context, actions

ctx = Context()
mod = Module()

@mod.capture(rule="( <self.letter> )")
def alphanumeric_keys(m) -> str:
    "alphanums"
    return str(m)

@mod.capture(rule="( <self.alphanumeric_keys> | <self.symbol_key> | <self.function_key> | <self.non_alphanum_key> | <self.arrow_key> )")
def unmodified_key(m) -> str:
    "any key without modifiers"
    return str(m)

@mod.capture(rule="repeat <self.number_string> (<self.unmodified_key>|<self.modified_key>)")
def repeater(m) -> str:
    for i in range(int(m[1])):
        actions.key(m[2:][0])
    return ""
