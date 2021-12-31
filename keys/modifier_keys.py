from talon import Module, Context, app, actions

modifier_keys = {
    "alt": "alt", 
    "control": "ctrl",
    "shift": "shift",
    "super": "super"
}

# Partially taken from https://github.com/knausj85/knausj_talon

if app.platform  == "mac":
    modifier_keys["command"] = "cmd"
    modifier_keys["option"] = "alt"

ctx = Context()
mod = Module()

mod.list("modifier_key", desc="All modifier keys")
ctx.lists["self.modifier_key"] = modifier_keys

@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)

@mod.capture(rule="<self.modifiers> <self.unmodified_key>")
def modified_key(m) -> str:
    print(f"{m.modifiers}-{m.unmodified_key}")
    return f"{m.modifiers}-{m.unmodified_key}"
