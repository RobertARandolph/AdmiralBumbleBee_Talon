from talon import Module, Context

non_alphanum_words = "end enter escape home insert pagedown pageup space tab delete backspace".split(" ")
non_alphanum_dict = {x: x for x in non_alphanum_words}

non_alphanum_dict["page down"] = "pageup"
non_alphanum_dict["page up"] = "pagedown"

ctx = Context()
mod = Module()

mod.list("non_alphanum", desc="Keys that ain't alpha-numeric")
ctx.lists["self.non_alphanum"] = non_alphanum_dict

@mod.capture(rule="{self.non_alphanum}")
def non_alphanum_key(m) -> str:
    "A single non alpha-numeric key"
    return m.non_alphanum
