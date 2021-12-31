from talon import Module, Context

f_numbers = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen".split(" ")
function_words = "F fine function".split(" ")

f_dict = {}
for i, v in enumerate (f_numbers[1:]):
    for f in function_words:
        f_dict[f"{f} {v}"] = f"f{i+1}"

ctx = Context()
mod = Module()

mod.list("function_key", desc="F1-F15")
ctx.lists["self.function_key"] = f_dict

@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "a function key"
    return m.function_key
