from talon import Module, Context

arrow_key_words = "up down left right".split(" ")
arrow_key_dict = {x: x for x in arrow_key_words}

ctx = Context()
mod = Module()

mod.list("arrow_key", desc="Arrow keys")
ctx.lists["self.arrow_key"] = arrow_key_dict

@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


