from talon import Module, Context, actions, app, imgui
from talon.grammar import Phrase
from typing import Any, Union
import pickle
import os.path
import datetime
from os import path
import user.robert_talon.reaper.reaperserver as rs

mod = Module()
ctx = Context()

showing_fx = False
showing_markers = False
showing_regions = False

parameter_favorites_file = "user/robert_talon/settings/parameter_favorites.p"
if path.exists(parameter_favorites_file):
    with open(parameter_favorites_file, "rb") as f:
        parameter_favorites = pickle.load(f)
else:
    parameter_favorites = {}

# Requires ~/.talon/bin/pip install python-osc
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 8000)

def refresh_osc():
    client.send_message("/action", 41743)

def init_reaper():
    client.send_message("/reaper/track/follows", "DEVICE")
    client.send_message("/device/track/follows", "LAST_TOUCHED")
    client.send_message("/device/fx/follows", "FOCUSED")
    client.send_message("/device/fxparam/count", rs.fx_bank_size)
    client.send_message("/device/marker/count", rs.marker_bank_size)
    client.send_message("/device/region/count", rs.region_bank_size)
    refresh_osc()

init_reaper()

@imgui.open(y=0, software=app.platform == "linux")
def param_gui(gui: imgui.GUI):
    gui.text(f"Current Bank: {rs.cur_display_bank}")

    for i in range(rs.fx_display_size):
        offset = (rs.cur_display_bank - 1) * rs.fx_display_size
        cur_index = i + offset
        if cur_index > rs.fx_bank_size:
            break;
        gui.line()
        d = rs.cur_params[cur_index]
        gui.text("{}: {} -- {}".format(cur_index + 1, d['name'], d['value']))

@imgui.open(y=0, software=app.platform == "linux")
def marker_gui(gui: imgui.GUI):
    gui.text(f"Current Bank: {rs.cur_marker_bank}")

    for i in range(rs.marker_display_size):
        offset = (rs.cur_marker_bank - 1) * rs.marker_display_size
        cur_index = i + offset
        if cur_index > rs.marker_bank_size:
            break;
        d = rs.cur_markers[cur_index]
        if not d:
            continue

        name = d.get("name")
        time = d.get("time")

        if not name and not time:
            continue

        gui.line()

        time = datetime.timedelta(seconds=float(time))
        if not name:
            gui.text("{}: {}".format(cur_index + 1, time))
        else:
            gui.text("{}: {} -- {}".format(cur_index + 1, name, time))

@imgui.open(y=0, software=app.platform == "linux")
def region_gui(gui: imgui.GUI):
    gui.text(f"Current Bank: {rs.cur_region_bank}")

    for i in range(rs.region_display_size):
        offset = (rs.cur_region_bank - 1) * rs.region_display_size
        cur_index = i + offset
        if cur_index > rs.region_bank_size:
            break;
        d = rs.cur_regions[cur_index]

        if not bool(d):
            continue

        name = d.get("name")
        time = d.get("time")
        length = d.get("length")

        if not name and not time:
            continue

        time = datetime.timedelta(seconds=float(time))
        length = datetime.timedelta(seconds=float(length))

        if not name:
            gui.text("{}:".format(cur_index + 1))
        else:
            gui.text("{}: {}".format(cur_index + 1, name))

        gui.text("Start: {}".format(time))
        gui.text("Length: {}".format(length))

@imgui.open(y=0, software=app.platform == "linux")
def favorite_params_gui(gui: imgui.GUI):
    cur_name = rs.cur_fx_name
    gui.text(f"{cur_name} Favorites")

    params = parameter_favorites.get(cur_name)

    if params is None:
        gui.text("No Favorites :(")
    else:
        for k, v in sorted(parameter_favorites[cur_name].items()):
            gui.line()
            cur_val = rs.cur_params[k - 1].get("value")
            gui.text(f"{k}: {v} - {cur_val}")

def save_favorite_parameters():
    with open(parameter_favorites_file, "wb") as f:
        pickle.dump(parameter_favorites, f)

 
@mod.action_class
class Actions:
    def send_osc_msg(s: str, n: Any):
        """sends an OSC message to a path with a given value"""
        client.send_message(s, n)

    def send_osc_action(n: int):
        """sends an OSC message to an action via INT ID"""
        client.send_message("/action", n)

    def send_osc_action_str(s: str):
        """sends an OSC message to an action via STR ID"""
        client.send_message("/action", s)

    def send_osc_toggle_action(n: int):
        """sends an OSC message to a toggle action"""
        client.send_message(f"/action/{n}", 1)
    
    def send_MIDI_osc_action(n: int):
        """sends an OSC message to trigger an action in the MIDI context"""
        client.send_message("/midiaction", n)

    def set_fx_bank_display_size(n: int):
        """FX Parameter display size"""
        rs.fx_display_size = n

    def fx_bank_jump(n: int):
        """Move up a bank for FX params"""
        rs.cur_display_bank = n
        #client.send_message("/device/fxparam/bank/+", 1)

    def fx_bank_up():
        """Move up a bank for FX params"""
        rs.cur_display_bank += 1
        #client.send_message("/device/fxparam/bank/+", 1)

    def fx_bank_down():
        """Move up a bank for FX params"""
        if rs.cur_display_bank == 1:
            rs.cur_display_bank = 1
        else:
            rs.cur_display_bank -= 1
        #client.send_message("/device/fxparam/bank/-", 1)

    def show_params():
        """Show FX Params"""
        global showing_fx
        showing_fx = True
        refresh_osc()
        param_gui.hide()
        param_gui.show()

    def close_params():
        """Close FX Params"""
        showing_fx = False
        param_gui.hide()

    def show_markers():
        """Show markers"""
        global showing_markers
        showing_markers = True
        refresh_osc()
        marker_gui.hide()
        marker_gui.show()

    def close_markers():
        """close markers"""
        showing_markerss = False
        marker_gui.hide()

    def go_to_marker(n: int):
        """go to markers"""
        if n < 10:
            actions.insert(str(n))
        elif n == 10:
            actions.insert("0")
        else:
            client.send_message("/marker", n)
        
    def rename_marker(n: int, p: Union[str, Phrase]):
        """go to markers"""
        if isinstance(p, str):
            client.send_message(f"/marker_id/{n}/name", p)
        else:
            print("Got phrase, what do we do here?")

    def show_regions():
        """Show regions"""
        global showing_regions
        showing_regions = True
        refresh_osc()
        region_gui.hide()
        region_gui.show()

    def close_regions():
        """close regions"""
        showing_regionss = False
        region_gui.hide()

    def go_to_region(n: int):
        """go to markers"""
        client.send_message("/region", n)

    def rename_region(n: int, p: Union[str, Phrase]):
        """go to markers"""
        if isinstance(p, str):
            client.send_message(f"/region_id/{n}/name", p)
        else:
            print("Got phrase, what do we do here?")

    def show_favorite_params():
        """Show favorite FX Params"""
        global showing_fx
        showing_fx = True
        favorite_params_gui.hide()
        favorite_params_gui.show()

    def close_favorite_params():
        """Show FX Params"""
        showing_fx = False
        favorite_params_gui.hide()

    def save_parameter(n: int):
        """Save a parameter for a given FX name"""
        if n == 0:
            return
        parameter_favorites.setdefault(rs.cur_fx_name, {}) 
        cur_name = rs.cur_fx_name
        update_dict = {n: rs.cur_params[n - 1].get('name')}
        parameter_favorites[cur_name].update(update_dict)
        save_favorite_parameters()

    def remove_parameter(n: int):
        """Save a parameter for a given FX name"""
        cur_name = rs.cur_fx_name
        cur_key = parameter_favorites.get(cur_name)
        if cur_key is None:
            return
        cur_key.pop(n)
        save_favorite_parameters()

    def console_through(s: str, n: int, n2: int, open: int = 0):
        """ReaConsole command for doing things to multiple tracks"""
        client.send_message("/action", s)
        big_n, little_n = (n2, n) if n2 > n else (n, n2)
        actions.sleep("200ms")
        actions.insert(little_n)
        actions.insert("-")
        actions.insert(big_n)
        actions.insert(" ")
        if not open:
            actions.key("enter")
            actions.key("esc")


def set_volume(loc, val, minus, track=-1):
    if track > 0:
        track_index = f"/{track}"
    else:
        track_index = ""
    if (minus == "minus" or minus == "negative"):
        client.send_message(f"/{loc}{track_index}/volume/str", f"-{val}")
    else:
        client.send_message(f"/{loc}{track_index}/volume/str", f"{val}")

def set_pan(loc, val, unit, track=-1):
    if track > 0:
        track_index = f"/{track}"
    else:
        track_index = ""
    val = {"percent": val / 100,
           "right": 0.5 + ((val / 2) / 100),
           "left": 0.5 - ((val / 2) / 100)}
    if unit is not None:
        client.send_message(f"/{loc}{track_index}/pan", val.get(unit, 0.5))


# Many of these could be actions... 

@mod.capture(rule="(initialize|reset|setup) reaper")
def initialize_reaper(m) -> str:
    print("Initializing REAPER")
    init_reaper()
    return "" 

@mod.capture(rule="record (enable|arm) <number>")
def record_enable_track(m) -> str:
    client.send_message(f"/track/{m.number}/recarm", 1)
    return "" 

@mod.capture(rule="record (disenable|disarm) <number>")
def record_disable_track(m) -> str:
    client.send_message(f"/track/{m.number}/recarm", 0)
    return "" 

@mod.capture(rule="track <number> name <phrase>")
def track_number_name(m) -> str:
    client.send_message(f"/track/{m.number}/name", m.phrase)
    return "" 

@mod.capture(rule="input <number> [stereo]")
def input_assign(m) -> str:
    retval = f"{m.number}"
    if len(m) > 2:
        retval += "s"
    return retval

@mod.capture(rule="open effect <number>")
def open_fx(m) -> str:
    client.send_message(f"/fx/{m.number}/openui", 1)
    return "" 

@mod.capture(rule="close effect <number>")
def close_fx(m) -> str:
    client.send_message(f"/fx/{m.number}/openui", 0)
    return "" 

@mod.capture(rule="open track <number> effect <number>")
def open_track_fx(m) -> str:
    client.send_message(f"/track/{m.number_list[0]}/fx/{m.number_list[1]}/openui", 1)
    return "" 

@mod.capture(rule="(bypass|disable) effect <number>")
def bypass_fx(m) -> str:
    client.send_message(f"/fx/{m.number}/bypass", 0)
    return "" 

@mod.capture(rule="(unbypass|enable) effect <number>")
def unbypass_fx(m) -> str:
    client.send_message(f"/fx/{m.number}/bypass", 1)
    return "" 

@mod.capture(rule="parameter <number> update <number> [percent]")
def change_focused_fx_param(m) -> str:
    print(f"/fxparam/{m.number_list[0]}/value", m.number_list[1] / 100)
    client.send_message(f"/fxparam/{m.number_list[0]}/value", m.number_list[1] / 100)
    return "" 

@mod.capture(rule="track volume [minus|negative] <number>")
def track_volume(m) -> str:
    set_volume("track", m.number, m[2])
    return "" 

@mod.capture(rule="track <number> volume [minus|negative] <number>")
def track_number_volume(m) -> str:
    set_volume("track", m.number_list[1], m[3], m.number_list[0])
    return "" 

@mod.capture(rule="master volume [minus|negative] <number>")
def master_volume(m) -> str:
    set_volume("master", m.number, m[2])
    return "" 

@mod.capture(rule="send <number> volume [minus|negative] <number>")
def send_volume(m) -> str:
    set_volume("track/send", m.number_list[1], m[3], m.number_list[0])
    return "" 

@mod.capture(rule="master send <number> volume [minus|negative] <number>")
def master_send_volume(m) -> str:
    set_volume("master/send", m.number_list[1], m[3], m.number_list[0])
    return "" 

@mod.capture(rule="track pan <number> ([percent]|[right|left])")
def track_pan(m) -> str:
    set_pan("track", m.number, m[3])
    return "" 

@mod.capture(rule="master pan <number> ([percent]|[right|left])")
def master_pan(m) -> str:
    set_pan("master", m.number, m[3])
    return "" 

@mod.capture(rule="track <number> pan <number> ([percent]|[right|left])")
def track_number_pan(m) -> str:
    set_pan("track", m.number_list[1], m[4], m.number_list[0])
    return "" 

@mod.capture(rule="send <number> pan <number> ([percent]|[right|left])")
def send_pan(m) -> str:
    set_pan("track/send", m.number_list[1], m[4], m.number_list[0])
    return "" 

@mod.capture(rule="master send <number> pan <number> ([percent]|[right|left])")
def master_send_pan(m) -> str:
    set_pan("master/send", m.number_list[1], m[4], m.number_list[0])
    return "" 

@mod.capture(rule="find track <phrase>")
def find_track(m) -> str:
    actions.key("alt-f2")
    actions.insert(f"{m.phrase}")
    actions.key("enter")
    return ""
