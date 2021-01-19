import atexit
import threading
from typing import List, Any
from pythonosc import dispatcher, osc_server

fx_bank_size = 1024
fx_display_size = 24
marker_bank_size = 128
marker_display_size = 24
region_bank_size = 128
region_display_size = 24
cur_display_bank = 1
cur_marker_bank = 1
cur_region_bank = 1
cur_fx_name = ""

cur_params = [{} for _ in range(fx_bank_size)]
cur_markers = [{} for _ in range(marker_bank_size)]
cur_regions = [{} for _ in range(region_bank_size)]

def fxparam_updater(address: str, *args: List[Any]):
    _, fx_number, fx_key, *t = address.lstrip("/").split("/")
    new_dict = {fx_key : args[0]}
    if fx_number == 'last_touched':
        print("Last Touched")
        return
    fx_int = int(fx_number)

    if fx_int > fx_bank_size:
        return

    cur_params[fx_int - 1].update(new_dict)
    #print(f"Number: {fx_int}, Key: {fx_key}, val: {args[0]}")

def fxname_updater(address: str, *args: List[Any]):
    global cur_fx_name
    cur_fx_name = args[0]

# duplication of fxparam_updater, TODO generalize 
def marker_updater(address: str, *args: List[Any]):
    _, marker_number, marker_key, *t = address.lstrip("/").split("/")
    new_dict = {marker_key : args[0]}
    marker_int = int(marker_number)

    if marker_int > marker_bank_size:
        return

    cur_markers[marker_int - 1].update(new_dict)
    #print(f"address: {address} args: {args}")

# duplication of fxparam_updater, TODO generalize 
def region_updater(address: str, *args: List[Any]):
    _, region_number, region_key, *t = address.lstrip("/").split("/")
    new_dict = {region_key : args[0]}
    region_int = int(region_number)

    if region_int > region_bank_size:
        return

    cur_regions[region_int - 1].update(new_dict)

def server_thread():
    d = dispatcher.Dispatcher()
    d.map("/fxparam/*/name", fxparam_updater)
    d.map("/fxparam/*/value*", fxparam_updater)

    d.map("/fx/name", fxname_updater)

    d.map("/marker/*", marker_updater)

    d.map("/region/*", region_updater)

    # Don't uncomment this unless you're brave, or stupid, or me.
    #d.map("/*", print)

    server = osc_server.ThreadingOSCUDPServer(("", 9000), d)
    server.allow_reuse_address = True
    server.serve_forever()

x = threading.Thread(target=server_thread)
x.start()

@atexit.register
def shutdown_server():
    x.exit()
