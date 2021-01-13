mode: user.clojure
mode: command
and code.language: clojure
-

settings():
    user.code_private_function_formatter = "DASH_SEPARATED"
    user.code_protected_function_formatter = "DASH_SEPARATED"
    user.code_public_function_formatter = "DASH_SEPARATED"
    user.code_private_variable_formatter = "DASH_SEPARATED"
    user.code_protected_variable_formatter = "DASH_SEPARATED"
    user.code_public_variable_formatter = "DASH_SEPARATED"

<user.clj_string>:
    insert(clj_string)

<user.clj_core>:
    insert(clj_core)
    
## loop
#
#action(user.code_loop_loop):
#    insert("(loop )")
#    key(left)
#action(user.code_loop_recur):
#    insert("(recur )")
#    key(left)
#action(user.code_loop_trampoline):
#    insert("(trampoline )")
#    key(left)
#action(user.code_loop_dotimes):
#    insert("(dotimes [])")
#    key(left)
#    key(left)
#action(user.code_loop_doseq):
#    insert("(doseq [])")
#    key(left)
#    key(left)
#action(user.code_loop_while):
#  insert("while ()")
#  key(left)
#
#action(user.code_loop_for):
#  insert("(for [])")
#  key(left)
#  key(left)
#
## def
#
#action(user.code_state_def):
#    insert("(def )")
#    key(left)
#action(user.code_state_defmulti):
#    insert("(defmulti  ())")
#    key(left:4)
#action(user.code_state_defonce):
#    insert("(defonce )")
#    key(left)
#action(user.code_state_defun):
#    insert("(defn")
#    key(enter)
#    insert("\"\"")
#    key(enter)
#    insert("[]")
#    key(enter)
#    insert(")")
#    key(left)
#action(user.code_state_private):
#    insert("(defn-")
#    key(enter)
#    insert("\"\"")
#    key(enter)
#    insert("[]")
#    key(enter)
#    insert(")")
#    key(left)
#action(user.code_state_fun):
#    insert("(fn [])")
#    key(left)
#    key(left)
#action(user.code_state_defmacro):
#    insert("()")
#    key(left)
#    insert("defmacro")
#    key(enter)
#    insert("\"\"")
#    key(enter)
#    insert("[]")
#    key(up:2)
#    key(esc)
#    key(shift-a)
#    key("")
#
#
## Predicates
#
#action(user.code_is_not_null): "(nil? )"
#
#action(user.code_is_null): "(some? )"
#
#action(user.code_block): 
#  insert("()") 
#  key(left)
#
## Branching
#
#action(user.code_branch_if):
#  insert("(if )")
#  key(left)
#
#action(user.code_branch_when):
#  insert("(when )")
#  key(left)
#
#action(user.code_branch_whennot):
#  insert("(when-not )")
#  key(left)
#
#action(user.code_branch_case):
#    insert("(case )")
#    key(left)
#
#action(user.code_branch_cond):
#    insert("(cond )")
#    key(left)
#action(user.code_branch_condp): 
#    insert("(condp )")
#    key(left)
#
## thread
#
#action(user.code_arrow_first):
#    insert("(-> )")
#    key(left)
#action(user.code_arrow_first):
#    insert("(->> )")
#    key(left)
#action(user.code_arrow_some):
#    insert("(some-> )")
#    key(left)
#action(user.code_arrow_some_last):
#    insert("(some->> )")
#    key(left)
#action(user.code_arrow_as):
#    insert("(as-> )")
#    key(left)
#action(user.code_arrow_cond):
#    insert("(cond-> )")
#    key(left)
#action(user.code_arrow_cond_last):
#    insert("(cond->> )")
#    key(left)
#
## noop
#
#action(user.code_state_go_to): ""
#action(user.code_state_switch): ""
#
#action(user.code_import): "import "
#
#action(user.code_from_import):
#  insert(" from  \"\"")
#  key(left)
#
#action(user.code_type_class): "class "
#
#action(user.code_state_return): ""
#action(user.code_include): ""
#
#action(user.code_include_system): ""
#
#action(user.code_include_local): ""
#
#action(user.code_type_definition): ""
#
#action(user.code_typedef_struct): ""
#
#action(user.code_state_for_each):
#  insert(".forEach()")
#  key(left)
#
#action(user.code_break): "break;"
#action(user.code_next): "continue;"
#action(user.code_true): "true"
#action(user.code_false): "false"
#
#action(user.code_null): "null"
#
#
## Unused Operators
#action(user.code_operator_indirection): ""
#action(user.code_operator_address_of): ""
#action(user.code_operator_structure_dereference): ""
#action(user.code_operator_subscript): ""
#action(user.code_operator_subtraction_assignment): ""
#action(user.code_operator_addition_assignment): ""
#action(user.code_operator_multiplication_assignment): ""
#(op | is) strict equal: ""
#(op | is) strict not equal: ""
#action(user.code_operator_division_assignment): ""
#action(user.code_operator_modulo_assignment): ""
#action(user.code_operator_bitwise_or_assignment): ""
#action(user.code_operator_bitwise_and_assignment): ""
#action(user.code_operator_bitwise_exclusive_or_assignment): ""
#action(user.code_operator_bitwise_left_shift_assignment): ""
#action(user.code_operator_bitwise_right_shift_assignment): ""
#
## Active Operators
#action(user.code_operator_lambda):
#    key("(fn [])")
#    key(left:2)
#action(user.code_operator_assignment):
#    key("(let [])")
#    key(left:2)
#action(user.code_operator_subtraction):
#    key("(- )")
#    key(left)
#action(user.code_operator_addition):
#    key("(+ )")
#    key(left)
#action(user.code_operator_multiplication):
#    key("(* )")
#    key(left)
#action(user.code_operator_exponent):
#    key("(Math/pow )")
#    key(left)
#action(user.code_operator_division):
#    key("(/ )")
#    key(left)
#action(user.code_operator_modulo):
#    key("(% )")
#    key(left)
#action(user.code_operator_equal):
#    key("(= )")
#    key(left)
#action(user.code_operator_not_equal):
#    key("(not= )")
#    key(left)
#action(user.code_operator_greater_than):
#    key("(> )")
#    key(left)
#action(user.code_operator_greater_than_or_equal_to):
#    key("(>= )")
#    key(left)
#action(user.code_operator_less_than):
#    key("(< )")
#    key(left)
#action(user.code_operator_less_than_or_equal_to):
#    key("(<= )")
#    key(left)
#action(user.code_operator_and):
#    key("(and )")
#    key(left)
#action(user.code_operator_or):
#    key("(or )")
#    key(left)
#action(user.code_operator_bitwise_and):
#    key("(bit-and )")
#    key(left)
#action(user.code_operator_bitwise_or):
#    key("(bit-or )")
#    key(left)
#action(user.code_operator_bitwise_exclusive_or):
#    key("(bit-xor )")
#    key(left)
#action(user.code_operator_bitwise_left_shift):
#    key("(bit-shift-left )")
#    key(left)
#action(user.code_operator_bitwise_right_shift):
#    key("(bit-shift-right )")
#    key(left)
#action(user.code_bit_flip)
#    key("(bit-flip )")
#    key(left)
#action(user.code_bit_clear)
#    key("(bit-clear )")
#    key(left)
#action(user.code_bit_set)
#    key("(bit-set )")
#    key(left)
#action(user.code_bit_test)
#    key("(bit-test )")
#    key(left)

