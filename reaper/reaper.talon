os: mac
app: REAPER
-

<user.dummy>:
    insert(dummy)

# Meta tooling

[Open] Console:
    user.send_osc_action_str("_SWSCONSOLE")

# Mixing

<user.input_assign>:
    user.console_through("_SWSCONSOLEINPUT", number_1, number_2)
    user.send_osc_action_str("_SWSCONSOLEINPUT")
    sleep(200ms)
    insert(input_assign)
    key("enter")
    key(esc)

arm tracks <number> through <number>:
    user.console_through("_SWSCONSOLEEXSEL", number_1, number_2)

(only|solo) tracks <number> through <number>:
    user.console_through("_SWSCONSOLESOLO", number_1, number_2)

(mute|kill) tracks <number> through <number>:
    user.console_through("_SWSCONSOLEMUTE", number_1, number_2)

toggle effects on tracks <number> through <number>:
    user.console_through("_SWSCONSOLEFX", number_1, number_2)

<user.record_enable_track>:
    insert(record_enable_track)

<user.record_disable_track>:
    insert(record_disable_track)

<user.track_volume>:
    insert(track_volume)

<user.track_number_volume>:
    insert(track_number_volume)

<user.track_pan>:
    insert(track_pan)

<user.track_number_pan>:
    insert(track_number_pan)

<user.send_volume>:
    insert(send_volume)

<user.send_pan>:
    insert(send_pan)

<user.master_volume>:
    insert(master_volume)

<user.master_pan>:
    insert(master_pan)

<user.master_send_volume>:
    insert(master_send_volume)

<user.master_send_pan>:
    insert(master_send_pan)

toggle record:
    key(r)

Toggle solo:
    key(s)

Toggle mute:
    key(m)

# FX Management

<user.open_fx>:
    insert(open_fx)

<user.close_fx>:
    insert(close_fx)

<user.open_track_fx>:
    insert(open_track_fx)

<user.initialize_reaper>:
    insert(initialize_reaper)

<user.bypass_fx>:
    insert(bypass_fx)

<user.unbypass_fx>:
    insert(unbypass_fx)

quick adder:
    key(f12)

Open [Effects] Browser:
    key(f11)

Open Effects [Chain]:
    key(ctrl-f11)

Open Master Effects [chain]:
    key(ctrl-alt-f11)

show parameters:
    user.show_params()

close parameters:
    user.close_params()

<user.change_focused_fx_param>:
    insert(change_focused_fx_param)

parameter bank <number>:
    user.fx_bank_jump(number)

parameter bank up:
    user.fx_bank_up()

parameter bank down:
    user.fx_bank_down()

next parameter bank:
    user.fx_bank_up()

previous parameter bank:
    user.fx_bank_down()

parameter bank size <number>:
    user.set_fx_bank_display_size(number)

save parameter <number>:
    user.save_parameter(number)

remove parameter <number>:
    user.remove_parameter(number)

[show] favorite parameters:
    user.show_favorite_params()

close favorite parameters:
    user.close_favorite_params()

# Transport

stop:
    key(space)

pause:
    key(enter)

play:
    key(space)

cycle|repeat:
    key(cmd-r)

# Project Navigation

clear find:
    key(alt-f2)
    key("delete")
    key("enter")

find track <phrase>$:
     key("alt-f2")
     insert(phrase)
     key("enter")

(go to|select) track <number>:
    user.send_osc_msg("/device/track/select", number)

select tracks <number> through <number>:
    user.console_through("_SWSCONSOLEEXSEL", number_1, number_2)

# Meta Navigation

Focus arrange:
    key(f1)

Focus tracks:
    key(f2)

Focus MIDI editor:
    key(alt-f1)

Focus Track Manager:
    key(alt-f2)

item edit:
    key(f3)

Edit:
    key(f4)

Mixer:
    key(f5)

midi:
    key(f6)
    sleep(200ms)
    key(alt-f1)

open MIDI item:
    key(shift-enter)

# Temporal Navigation

left grid:
    key(h)

right grid:
    key(l)

start of measure:
    key(a)

forward measure:
    key(e)
    
Go to start of project:
    key(shift-a)

Go to end of project:
    key(shift-e)

right to nearest item edge:
    key(alt-l)

next item:
    key(alt-l)

left to nearest item edge:
    key(alt-h)

previous item:
    key(alt-h)

next transient:
    key(tab)

previous transient:
    key(shift-tab)

go to measure <user.number_string>:
    key(cmd-j)
    sleep(100ms)
    key(delete)
    insert("{number_string}")
    insert(".1.00")
    key("enter")

go back <user.number_string> measures:
    key(cmd-j)
    sleep(100ms)
    key(delete)
    insert("-")
    insert("{number_string}")
    insert(".0.00")
    sleep(300ms)
    key("enter")

go forward <user.number_string> measures:
    key(cmd-j)
    sleep(100ms)
    key(delete)
    insert("+")
    insert("{number_string}")
    insert(".0.00")
    sleep(300ms)
    key("enter")

go to time <user.number_string>:
    key(cmd-j)
    sleep(100ms)
    key(delete)
    insert("0:")
    insert("{number_string}")
    insert(".00")
    key("enter")

# Markers

Insert [edit] marker:
    key(cmd-')

marker <user.number_string>:
    key("{number_string}")

next marker:
    key(')

Go to previous marker/project start:
    key(alt-')

Renumber all markers:
    key(cmd-')

Remove all markers from time selection:
    key(ctrl-')

show markers:
    user.show_markers()

close markers:
    user.close_markers()

go to marker <number>:
    user.go_to_marker(number)

marker <number> name <phrase>$:
    user.rename_marker(number, phrase)

edit marker:
    user.send_osc_action(40614)

show regions:
    user.show_regions()

close regions:
    user.close_regions()

go to region <number>:
    user.go_to_region(number)

region <number> name <phrase>$:
    user.rename_region(number, phrase)

edit region:
    user.send_osc_action(40616)

# Grid

grid whole:
    key(keypad_1)
grid half:
    key(keypad_2)
grid quarter:
    key(keypad_4)
grid quarter triplet:
    key(keypad_5)
grid eighth:
    key(keypad_8)
grid eighth triplet:
    key(keypad_9)
grid sixteenth:
    key(keypad_6)
grid sixteenth triplet:
    key(keypad_7)
grid thirty second:
    key(keypad_3)

# Track Management

<user.track_name>:
    insert(track_name)

track name <phrase>$:
    user.send_osc_msg("/track/name", phrase)

<user.track_number_name>:
    insert(track_number_name)

(create|new) track:
    user.send_osc_action(40001)

(create|new) track at end:
    user.send_osc_action(40702)

new tracks:
    user.send_osc_action(41067)

create multiple tracks:
    user.send_osc_action(41067)

select all tracks:
    user.send_osc_action(40296)

delete selected tracks:
    user.send_osc_action_str("_SWS_DELTRACKCHLD")

prefix tracks <number> through <number>:
    user.console_through("_SWSCONSOLEPREFIX", number_1, number_2, 1)

suffix tracks <number> through <number>:
    user.console_through("_SWSCONSOLEPREFIX", number_1, number_2, 1)

color tracks <number> through <number>:
    user.console_through("_SWSCONSOLECOLOR", number_1, number_2, 1)

# Editing

Undo:
    key(u)

Redo:
    key(ctrl-r)

Cut:
    key(x)

Copy ignoring time selection:
    key(y)

Paste:
    key(p)

duplicate:
    key(cmd-d)

Copy within time selection:
    key(shift-y)

Cut within time selection:
    key(shift-x)

Insert time and paste items:
    key(cmd-p)

Increase selected track heights:
    key(alt-+)

Decrease selected track heights:
    key(alt--)

Split:
    key(/)

split select right:
    user.send_osc_action(40759)

split select left:
    user.send_osc_action(40758)

Split items at transients:
    key(unused)

trim left:
    key([) 

trim right:
    key(])

nudge item [volume] up:
    key(k)

nudge item [volume] down:
    key(j)

move item left to cursor:
    key(cmd-b)

move item right to cursor:
    key(cmd-e)

contents of item to edit cursor:
    key(c)

Dynamic split:
    key(d)

Trim left [to cursor]:
    key([)

Trim right [to cursor]:
    key(])

move left [to cursor]:
    key(alt-[)

move right [to cursor]:
    key(alt-])

Add stretch marker:
    key(w)

insert midi item:
    user.send_osc_action(40214)
 

# Fades

fade items in:
    key(cmd-f)

fade items out:
    key(cmd-shift-f)

^cycle fade in$:
    key(f)

^cycle fade out$:
    key(shift-f)

remove fade in:
    key(alt-f)

Remove fade out:
    key(alt-shift-f)

Crossfade:
    key(cmd-x)

Cycle crossfade:
    key(shift-command-x)

# Zoom

Zoom time selection:
    key(z)

Restore previous zoom level:
    key(cmd-z)

Horizontal zoom to selected items:
    key(ctrl-z)

action(edit.zoom_in):
    key("=")

action(edit.zoom_out):
	key("-")

Zoom to full project:
    key(cmd-z)

# Time Selection

Set start:
    key(i)

Set end:
    key(o)

time selection to items:
    key(shift-i)

Remove time selection:
    key(alt-i)

nudge left selection [edge] left:
    key(cmd-<)

nudge left selection [edge] right:
    key(cmd->)

nudge right selection [edge] left:
    key(cmd-alt-<)

nudge right selection [edge] right:
    key(cmd-alt->)

Select all items:
    key(shift-v)

Select all items in selection:
    key(ctrl-shift-v)

# Item Selection

Select and move to next:
    key(v)

Select and move to previous:
    key(alt-v)

# Track Selection

next track:
    key(alt-j)

previous track:
    key(alt-k)

Select next track keep selection:
    key(alt-shift-j)

Select previous track keep selection:
    key(alt-shift-k)

select [item] under cursor:
    key(cmd-alt-shift-enter)

Select and move to item in next track:
    key(cmd-↓)

Select and move to item in previous track:
    key(cmd-↑)

# Automation

Insert 4 envelope points:
    key(shift-4)

add envelope point:
    key(alt-a)

Delete automation in selection:
    key(alt-a)

# Take Management

next take:
    key(t)

previous take:
    key(alt-t)

Delete active take:
    key(ctrl-t)

Crop to active take:
    key(cmd-t)

# Recording

^Record$:
    key(`)

Undo recording:
    key(alt-`)

[enable] metronome:
    key(q)

metronome [on]:
    key(q)

[enable] click:
    key(q)

click [on]:
    key(q)

[disable] metroffome:
    key(-alt-q)

metroffome [off]:
    key(-alt-q)

[disable] click:
    key(-alt-q)

click [off]:
    key(-alt-q)

# MIDI

Insert note:
    key(keypad_enter)

Insert air:
    key(a)

Insert air sharp:
    key(ctrl-b)

Insert bat flat:
    key(ctrl-b)

Insert bat:
    key(b)

Insert Cap:
    key(c)

Insert cap sharp:
    key(ctrl-d)

Insert d flat:
    key(ctrl-d)

Insert drum:
    key(d)

Insert drum sharp:
    key(ctrl-e)

Insert each flat:
    key(ctrl-e)

Insert each:
    key(e)

Insert fine:
    key(f)

Insert fine sharp:
    key(alt-g)

Insert gust flat:
    key(opt-g)

Insert gust:
    key(g)

Insert gust sharp:
    key(ctrl-a)

Insert air flat:
    key(ctrl-a)

# Note Editing

notes down:
    key(cmd-j)

notes up:
    key(cmd-k)

notes down octave:
    key(cmd-ctrl-j)

notes up octave:
    key(cmd-ctrl-k)

velocity up:
    key(alt-k)

velocity down:
    key(alt-j)

velocity up big:
    key(ctrl-alt-k)

velocity down big:
    key(ctrl-alt-j)

note length 1:
    key(opt-1)

note length half:
    key(opt-2)

note length quarter:
    key(opt-4)

note length quarter triplet:
    key(opt-5)

note length eighth:
    key(opt-8)

note length eighth triplet:
    key(opt-9)

note length sixteenth:
    key(opt-6)

note length sixteenth triplet:
    key(opt-7)

note length thirty second:
    key(opt-3)

# Pitch Cursor

[pitch] cursor up:
    key(k)

[pitch] cursor down:
    key(j)

[pitch] cursor up (big|octave):
    key(ctrl-k)

[pitch] cursor down (big|octave):
    key(ctrl-j)

[pitch] cursor air:
    key(shift-a)

[pitch] cursor air sharp:
    key(shift-ctrl-b)

[pitch] cursor bat flat:
    key(shift-ctrl-b)

[pitch] cursor bat:
    key(shift-b)

[pitch] cursor cap:
    key(shift-c)

[pitch] cursor cap sharp:
    key(shift-ctrl-d)

[pitch] cursor drum flat:
    key(shift-ctrl-d)

[pitch] cursor drum:
    key(shift-d)

[pitch] cursor drum sharp:
    key(shift-ctrl-e)

[pitch] cursor each flat:
    key(shift-ctrl-e)

[pitch] cursor each:
    key(shift-e)

[pitch] cursor fine:
    key(shift-f)

[pitch] cursor fine sharp:
    key(shift-ctrl-g)

[pitch] cursor gust flat:
    key(shift-ctrl-g)

[pitch] cursor gust:
    key(shift-g)

[pitch] cursor gust sharp:
    key(shift-ctrl-a)

[pitch] cursor air flat:
    key(shift-ctrl-a)

# Note Selection

Select notes at pitch:
    key(shift-v)

Select notes in selection:
    key(ctrl-shift-v)

# MIDI Zoom

Zoom in vertically|vertical:
    key(h)
   
Zoom out vertically|vertical:
    key(alt-h)

Zoom to selected events|notes|(see see):
    key(ctrl-z)

# MIDI Editor Scrolling

Scroll up:
    key(ctrl-u)

Scroll down:
    key(ctrl-d)

Scroll right:
    key(ctrl-alt-u)

Scroll left:
    key(ctrl-alt-d)

# Step Input

step input mode:
    key(m)

# Run Action

find action:
    key(shift-/)

action <phrase>+:
    key(shift-/)
    insert(phrase)
    key(enter:2)