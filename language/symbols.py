from talon import Module, Context

mod = Module()
mod.list("symbol", desc="Commonly used non-alphanum typed characters")

symbols = {
    # Number row
    "back tick": "`",
    "back tic": "`",
    "batik": "`",
    "baltic": "`",
    "grave": "`",

    "tilde": "~",

    "exclamation mark": "!",
    "exclamation point": "!",
    "bang": "!",

    "at sign": "@",

    "hash sign": "#",
    "number sign": "#",
    "hash": "#",

    "dollar": "$",
    "dollar sign": "$",

    "percent sign": "%",
    "percent": "%",

    "caret": "^",

    "and sign": "&",
    "ampersand": "&",

    "asterisk": "*",
    "star": "*",

    "paren": "(",
    "round": "(",
    "left paren": "(",
    "left round": "(",
    "left parenthesis": "(",

    "right round": ")",
    "roundish": ")",
    "right parenthesis": ")",

    "minus": "-",
    "dash": "-",

    "under score": "_",
    "underscore": "_",

    "plus": "+",

    "equals": "=",

    # right cluster - same key grouped assuming ISO/IEC 9995-2

    "left square": "[",
    "left bracket": "[",
    "square": "[",
    "curly": "{",
    "brace": "{",
    "left brace": "{",

    "right square": "]",
    "right bracket": "]",
    "squarish": "]",
    "right brace": "}",
    "churlish": "}",

    "colon": ":",
    "semicolon": ";",

    "dubquote": '"',
    "double quote": '"',
    "double": '"',
    "quote": "'",
    "apostrophe": "'",
    "single": "'",

    "angle": "<",
    "left angle": "<",
    "less than": "<",
    "comma": ",",

    "R angle": ">",
    "right angle": ">",
    "greater than": ">",
    "period": ".",
    "point": ".",
    "full stop": ".",
    "dot": ".",

    "pipe": "|",
    "spike": "|",
    "backslash": "\\",

    "question mark": "?",
    "forward slash": "/",
    "slash": "/",

    # Currencies
    "pound": "£",
    "pound sign": "£",
    "euro": "€",
    "euro sign": "€",
    "won": "₩",
    "won sign": "₩",
    "korean won": "₩",
    "korean won sign": "₩",
    "yuan": "¥",
    "chinese yuan": "¥",
    "yuan sign": "¥",
    "chinese yuan sign": "¥",
    "yen": "¥",
    "japanese yen": "¥",
    "yen sign": "¥",
    "japanese yen sign": "¥"
}

ctx = Context()
ctx.lists["self.symbol"] = symbols

@mod.capture(rule="{self.symbol}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol
