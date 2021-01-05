mode: user.clojure
mode: command
and code.language: clojure
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic
tag(): user.code_lisp

settings():
    user.code_private_function_formatter = "DASH_SEPARATED"
    user.code_protected_function_formatter = "DASH_SEPARATED"
    user.code_public_function_formatter = "DASH_SEPARATED"
    user.code_private_variable_formatter = "DASH_SEPARATED"
    user.code_protected_variable_formatter = "DASH_SEPARATED"
    user.code_public_variable_formatter = "DASH_SEPARATED"

# loop

action(user.code_loop_loop):
    insert("(loop )")
    key(left)
action(user.code_loop_recur):
    insert("(recur )")
    key(left)
action(user.code_loop_trampoline):
    insert("(trampoline )")
    key(left)
action(user.code_loop_dotimes):
    insert("(dotimes [])")
    key(left)
    key(left)
action(user.code_loop_doseq):
    insert("(doseq [])")
    key(left)
    key(left)
action(user.code_loop_while):
  insert("while ()")
  key(left)

action(user.code_loop_for):
  insert("(for [])")
  key(left)
  key(left)

# def

action(user.code_state_def):
    insert("(def )")
    key(left)
action(user.code_state_defmulti):
    insert("(defmulti  ())")
    key(left)
    key(left)
    key(left)
    key(left)
action(user.code_state_defonce):
    insert("(defonce )")
    key(left)
action(user.code_state_defun):
    insert("(defn")
    key(enter)
    insert("\"\"")
    key(enter)
    insert("[]")
    key(enter)
    insert(")")
    key(left)
action(user.code_state_private):
    insert("(defn-")
    key(enter)
    insert("\"\"")
    key(enter)
    insert("[]")
    key(enter)
    insert(")")
    key(left)
action(user.code_state_fun):
    insert("(fn [])")
    key(left)
    key(left)
action(user.code_state_defmacro):
    insert("()")
    key(left)
    insert("defmacro")
    key(enter)
    insert("\"\"")
    key(enter)
    insert("[]")
    key(up)
    key(up)
    key(esc)
    key(shift-a)
    key("")


# Predicates

action(user.code_is_not_null): "(nil? )"

action(user.code_is_null): "(some? )"

action(user.code_block): 
  insert("()") 
  key(left)

# Branching

action(user.code_branch_if):
  insert("(if )")
  key(left)

action(user.code_branch_when):
  insert("(when )")
  key(left)

action(user.code_branch_whennot):
  insert("(when-not )")
  key(left)

action(user.code_branch_case):
    insert("(case )")
    key(left)

action(user.code_branch_cond):
    insert("(cond )")
    key(left)
action(user.code_branch_condp): 
    insert("(condp )")
    key(left)

# thread

action(user.code_arrow_first):
    insert("(-> )")
    key(left)
action(user.code_arrow_first):
    insert("(->> )")
    key(left)
action(user.code_arrow_some):
    insert("(some-> )")
    key(left)
action(user.code_arrow_some_last):
    insert("(some->> )")
    key(left)
action(user.code_arrow_as):
    insert("(as-> )")
    key(left)
action(user.code_arrow_cond):
    insert("(cond-> )")
    key(left)
action(user.code_arrow_cond_last):
    insert("(cond->> )")
    key(left)

# noop

action(user.code_state_go_to): ""
action(user.code_state_switch): ""

action(user.code_import): "import "

action(user.code_from_import):
  insert(" from  \"\"")
  key(left)

action(user.code_type_class): "class "

action(user.code_state_return): ""
action(user.code_include): ""

action(user.code_include_system): ""

action(user.code_include_local): ""

action(user.code_type_definition): ""

action(user.code_typedef_struct): ""

action(user.code_state_for_each):
  insert(".forEach()")
  key(left)

action(user.code_break): "break;"
action(user.code_next): "continue;"
action(user.code_true): "true"
action(user.code_false): "false"

action(user.code_null): "null"

action(user.code_operator_indirection): ""
action(user.code_operator_address_of): ""
action(user.code_operator_structure_dereference): ""
action(user.code_operator_lambda): " => "
action(user.code_operator_subscript):
  insert("[]")
  key(left)
action(user.code_operator_assignment): " = "
action(user.code_operator_subtraction): " - "
action(user.code_operator_subtraction_assignment): " -= "
action(user.code_operator_addition): " + "
action(user.code_operator_addition_assignment): " += "
action(user.code_operator_multiplication): " * "
action(user.code_operator_multiplication_assignment): " *= "
action(user.code_operator_exponent): " ** "
action(user.code_operator_division): " / "
action(user.code_operator_division_assignment): " /= "
action(user.code_operator_modulo): " % "
action(user.code_operator_modulo_assignment): " %= "
action(user.code_operator_equal): " == "
action(user.code_operator_not_equal): " != "
(op | is) strict equal: " === "
(op | is) strict not equal: " !== "
action(user.code_operator_greater_than): " > "
action(user.code_operator_greater_than_or_equal_to): " >= "
action(user.code_operator_less_than): " < "
action(user.code_operator_less_than_or_equal_to): " <= "
action(user.code_operator_and): " && "
action(user.code_operator_or): " || "
action(user.code_operator_bitwise_and): " & "
action(user.code_operator_bitwise_and_assignment): " &= "
action(user.code_operator_bitwise_or): " | "
action(user.code_operator_bitwise_or_assignment): " |= "
action(user.code_operator_bitwise_exclusive_or): " ^ "
action(user.code_operator_bitwise_exclusive_or_assignment): " ^= "
action(user.code_operator_bitwise_left_shift): " << "
action(user.code_operator_bitwise_left_shift_assignment): " <<= "
action(user.code_operator_bitwise_right_shift): " >> "
action(user.code_operator_bitwise_right_shift_assignment): " >>= "

state const: "const "

state let: "let "

state var: "var "

state async: "async "

state await: "await "

state map:
  insert(".map()")
  key(left)

state filter:
  insert(".filter()")
  key(left)

state reduce:
  insert(".reduce()")
  key(left)

state spread: "..."

^funky <user.text>$: user.code_private_function(text)
^pro funky <user.text>$: user.code_protected_function(text)
^pub funky <user.text>$: user.code_public_function(text)