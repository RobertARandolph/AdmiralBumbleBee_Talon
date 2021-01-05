from talon import Module, Context, actions, app
import re
mod = Module()
ctx = Context()

# Operators
mod.list('vim_verbs', desc='Vim Grammar verbs')
ctx.lists['self.vim_verbs'] = {
    "kill": "d",
    "change": "c",
    "yank": "y",
    "visual": "v",
    "wrap": "ys"
}

# Only composable with an operator
mod.list('vim_passive_ops', desc='Vim operaters that do nothing on their own')
ctx.lists['self.vim_passive_ops'] = {
    "around": "a",
    "in": "i"
}

# List for position only
mod.list('vim_position', desc='Vim operaters that do nothing on their own')
ctx.lists['self.vim_position'] = {
    "to position": "\'",
    "position": "\'",
}

# Usable with an operator or alone
mod.list('vim_active_ops', desc='Vim operators that do things on their own')
ctx.lists['self.vim_active_ops'] = {
    "find letter": "t",
    "on letter": "f",
    "find letter back": "T",
    "on letter back": "F"
}

# Usable with operator->action or alone
mod.list('vim_composable_objects', desc='Vim Grammar objects')
ctx.lists['self.vim_composable_objects'] = {
    "word": "w",
    "big word": "W",
    "back": "b",
    "big back": "B",
    "end": "e",
    "big end": "E"
}

# Usable only with operator->action 
mod.list('vim_exclusive_composable_objects', desc='Vim Grammar objects')
ctx.lists['self.vim_exclusive_composable_objects'] = {
    "tag": "t",
    "block": "b",
    "big block": "B",
    "paragraph": "p",
    "sentence": "s",
}

# Commands on their own, or usable with verbs
mod.list('vim_active_objects', desc='Vim Grammar objects')
ctx.lists['self.vim_active_objects'] = {
    "end of line": "$",
    "start of line": "0",
    "first word": "^",
}

@ctx.action_class("core")
class Actions:
    def run_talon_script(ctx, script, m):
        with ctx:
            print(f"CONTEXT: {ctx}")
            print(f"SCRIPT: {script}")
            print(f"COMMAND: {m}")
            app.notify(str(m))
            script.run(actions, namespace=m)

# mildly disgusting, but effective and seems to be accurate (??).
# ({self.vim_verbs} [<user.number_string>] ({self.vim_passive_ops} | {self.vim_active_ops}) ({self.vim_exclusive_composable_objects} | <user.symbol_key> | {self.vim_composable_objects})) |
# ({self.vim_verbs} {self.vim_active_ops} [ship|uppercase] (<user.letters> | <user.symbol_key>)) |
# ({self.vim_verbs} {self.vim_active_objects}) |
# ({self.vim_verbs} {self.vim_position} [ship|uppercase] <user.letter>) |
# ({self.vim_active_ops} [ship|uppercase] (<user.letters> | <user.symbol_key>)) |
# ({self.vim_composable_objects}) |
# ({self.vim_active_objects}))
@mod.capture(rule="({self.vim_verbs} [<user.number_string>] ({self.vim_passive_ops} | {self.vim_active_ops}) ({self.vim_exclusive_composable_objects} | <user.symbol_key> | {self.vim_composable_objects})) | ({self.vim_verbs} {self.vim_active_ops} [ship|uppercase] (<user.letters> | <user.symbol_key>)) | ({self.vim_verbs} {self.vim_active_objects}) | ({self.vim_verbs} {self.vim_position} [ship|uppercase] <user.letter>) | ({self.vim_active_ops} [ship|uppercase] (<user.letters> | <user.symbol_key>)) | ({self.vim_composable_objects}) | ({self.vim_active_objects})")
def vim_command (m) -> str:
    parsed = ""
    itr = iter(m)

    # Parse for "ship" or "uppercase" in command, if present then capitalize (not uppercase) the next thing.
    while True:
        try:
            item = next(itr)
            if item == "ship" or item == "uppercase":
                item = next(itr) # add next item
                if item is not None:
                    parsed += item.capitalize()
            else:
                parsed += item
        except StopIteration:
            break
    return parsed

@mod.capture(rule="go to line <user.number_string>")
def ex_mode(m) -> str:
    actions.insert(f":{m.number_string}")
    actions.key("enter")
    return ""
