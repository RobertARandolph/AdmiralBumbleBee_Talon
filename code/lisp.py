from talon import Context, Module, actions, app, imgui, registry, settings

# This is obviously not lisp, but clojure, and a work in progress. That will change over time.

ctx = Context()
mod = Module()

mod.tag("code_lisp", desc="Tag for enabling lispy (mostly clojure)")

@mod.action_class
class Actions:

    def code_operator_indirection():
        """code_operator_indirection"""
# loops
    def code_loop_loop():
        """code_loop_loop"""
    def code_loop_for():
        """code_loop_for"""
    def code_loop_while():
        """code_loop_while"""
    def code_loop_recur():
        """code_loop_recur"""
    def code_loop_trampoline():
        """code_loop_trampoline"""
    def code_loop_dotimes():
        """code_loop_dotimes"""
    def code_loop_doseq():
        """code_loop_doseq"""

# def
    def code_state_def():
        """code_state_def"""
    def code_state_defmulti():
        """code_state_defmulti"""
    def code_state_defonce():
        """code_state_defonce"""
    def code_state_defun():
        """code_state_defun"""
    def code_state_private():
        """code_state_private"""
    def code_state_fun():
        """code_state_fun"""
    def code_state_defmacro():
        """code_state_defmacro"""

# branching

    def code_branch_if():
        """code_branch_if""" 
    def code_branch_when():
        """code_branch_when""" 
    def code_branch_whennot():
        """code_branch_whennot""" 
    def code_branch_case():
        """code_branch_case""" 
    def code_branch_cond():
        """code_branch_cond""" 
    def code_branch_condp():
        """code_branch_condp""" 

# thread
    def code_arrow_first():
        """code_arrow_first""" 
    def code_arrow_first():
        """code_arrow_first""" 
    def code_arrow_some():
        """code_arrow_some""" 
    def code_arrow_some_last():
        """code_arrow_some_last""" 
    def code_arrow_as():
        """code_arrow_as""" 
    def code_arrow_cond():
        """code_arrow_cond""" 
    def code_arrow_cond_last():
        """code_arrow_cond_last""" 
