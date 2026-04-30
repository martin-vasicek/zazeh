#!/usr/bin/env python3
"""
Add autoClick to all dismissal buttons in event files.
"""
import os

BASE = r'c:\Users\marti\Desktop\zazeh-test\script\events'

NL = '\r\n'

def n(s):
    """Convert \n to \r\n for CRLF files."""
    return s.replace('\n', NL)

def patch(path, replacements):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        content = f.read()
    changed = 0
    for old, new in replacements:
        old_crlf = n(old)
        new_crlf = n(new)
        if old_crlf in content:
            content = content.replace(old_crlf, new_crlf)
            changed += 1
            print(f'  OK: {repr(old[:70])}')
        else:
            print(f'  MISS: {repr(old[:70])}')
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print(f'  → {changed}/{len(replacements)} replacements made in {os.path.basename(path)}')
    return changed

# ==== room.js ====
ROOM = os.path.join(BASE, 'room.js')
room_replacements = [
    # Noises Outside start: 'ignore them'
    (
        "'ignore': {\n\t\t\t\t\t\ttext: _('ignore them'),\n\t\t\t\t\t\tnextScene: 'end'\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'nothing': {",
        "'ignore': {\n\t\t\t\t\t\ttext: _('ignore them'),\n\t\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\t\tautoClick: 20\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'nothing': {"
    ),
    # Noises Inside start: 'ignore them'
    (
        "'ignore': {\n\t\t\t\t\ttext: _('ignore them'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tscales: {",
        "'ignore': {\n\t\t\t\t\ttext: _('ignore them'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 20\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tscales: {"
    ),
    # Noises Inside scales: 'leave'
    (
        "$SM.addM('stores', {'wood': -numWood, 'scales': numScales});\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tteeth: {",
        "$SM.addM('stores', {'wood': -numWood, 'scales': numScales});\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tteeth: {"
    ),
    # Noises Inside teeth: 'leave'
    (
        "$SM.addM('stores', {'wood': -numWood, 'teeth': numTeeth});\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tcloth: {",
        "$SM.addM('stores', {'wood': -numWood, 'teeth': numTeeth});\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tcloth: {"
    ),
    # Noises Inside cloth: 'leave'
    (
        "$SM.addM('stores', {'wood': -numWood, 'cloth': numCloth});\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\t}\n\t},\n\t{ /* The Beggar",
        "$SM.addM('stores', {'wood': -numWood, 'cloth': numCloth});\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\t}\n\t},\n\t{ /* The Beggar"
    ),
    # Beggar start: 'turn him away'
    (
        "'deny': {\n\t\t\t\t\ttext: _('turn him away'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tscales: {\n\t\t\treward: { scales: 20 },",
        "'deny': {\n\t\t\t\t\ttext: _('turn him away'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 60\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\tscales: {\n\t\t\treward: { scales: 20 },"
    ),
    # Beggar scales: 'say goodbye'
    (
        "scales: {\n\t\t\treward: { scales: 20 },\n\t\t\ttext: [\n\t\t\t\t_('the beggar expresses his thanks.'),\n\t\t\t\t_('leaves a pile of small scales behind.')\n\t\t\t],\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "scales: {\n\t\t\treward: { scales: 20 },\n\t\t\ttext: [\n\t\t\t\t_('the beggar expresses his thanks.'),\n\t\t\t\t_('leaves a pile of small scales behind.')\n\t\t\t],\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Beggar teeth: 'say goodbye'
    (
        "teeth: {\n\t\t\treward: { teeth: 20 },\n\t\t\ttext: [\n\t\t\t\t_('the beggar expresses his thanks.'),\n\t\t\t\t_('leaves a pile of small teeth behind.')\n\t\t\t],\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "teeth: {\n\t\t\treward: { teeth: 20 },\n\t\t\ttext: [\n\t\t\t\t_('the beggar expresses his thanks.'),\n\t\t\t\t_('leaves a pile of small teeth behind.')\n\t\t\t],\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Beggar cloth: 'say goodbye'
    (
        "cloth: {\n\t\t\treward: { cloth: 20 },\n\t\t\ttext: [\n\t\t\t\t_('the beggar expresses his thanks.'),\n\t\t\t\t_('leaves some scraps of cloth behind.')\n\t\t\t],\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "cloth: {\n\t\t\treward: { cloth: 20 },\n\t\t\ttext: [\n\t\t\t\t_('the beggar expresses his thanks.'),\n\t\t\t\t_('leaves some scraps of cloth behind.')\n\t\t\t],\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Shady Builder start: 'say goodbye' (deny)
    (
        "'deny': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'steal': {",
        "'deny': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 60\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'steal': {"
    ),
    # Shady Builder steal: 'go home'
    (
        "'steal': {\n\t\t\ttext:[\n\t\t\t\t_(\"the shady builder has made off with your wood\")\n\t\t\t],\n\t\t\tnotification: _('the shady builder has made off with your wood'),\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "'steal': {\n\t\t\ttext:[\n\t\t\t\t_(\"the shady builder has made off with your wood\")\n\t\t\t],\n\t\t\tnotification: _('the shady builder has made off with your wood'),\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Mysterious Wanderer wood start: 'turn him away'
    (
        "'deny': {\n\t\t\t\t\ttext: _('turn him away'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'wood100': {",
        "'deny': {\n\t\t\t\t\ttext: _('turn him away'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 60\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'wood100': {"
    ),
    # Mysterious Wanderer wood100: 'say goodbye'
    (
        "}, 'Room[4].scenes.wood100.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.5) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "}, 'Room[4].scenes.wood100.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.5) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Mysterious Wanderer wood500: 'say goodbye'
    (
        "}, 'Room[4].scenes.wood500.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.3) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "}, 'Room[4].scenes.wood500.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.3) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Mysterious Wanderer fur start: 'turn her away'
    (
        "'deny': {\n\t\t\t\t\ttext: _('turn her away'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'fur100': {",
        "'deny': {\n\t\t\t\t\ttext: _('turn her away'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 60\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'fur100': {"
    ),
    # Mysterious Wanderer fur100: 'say goodbye'
    (
        "}, 'Room[5].scenes.fur100.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.5) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "}, 'Room[5].scenes.fur100.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.5) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Mysterious Wanderer fur500: 'say goodbye'
    (
        "}, 'Room[5].scenes.fur500.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.3) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "}, 'Room[5].scenes.fur500.action', delay);\n\t\t\t},\n\t\t\tonLoad: function() {\n\t\t\t\tif(Math.random() < 0.3) {\n\t\t\t\t\tthis.action(60);\n\t\t\t\t}\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('say goodbye'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Wandering Master start: 'turn him away'
    (
        "'deny': {\n\t\t\t\t\ttext: _('turn him away'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'agree': {",
        "'deny': {\n\t\t\t\t\ttext: _('turn him away'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 60\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'agree': {"
    ),
    # Sick Man start: 'tell him to leave'
    (
        "'ignore': {\n\t\t\t\t\ttext: _('tell him to leave'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "'ignore': {\n\t\t\t\t\ttext: _('tell him to leave'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 60\n\t\t\t\t}"
    ),
    # Sick Man alloy: 'say goodbye'
    (
        "$SM.add('stores[\"alien alloy\"]', 1);\n\t\t},\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end'\n\t\t\t}\n\t\t}\n\t},\n\t'cells': {",
        "$SM.add('stores[\"alien alloy\"]', 1);\n\t\t},\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end',\n\t\t\t\tautoClick: 15\n\t\t\t}\n\t\t}\n\t},\n\t'cells': {"
    ),
    # Sick Man cells: 'say goodbye'
    (
        "$SM.add('stores[\"energy cell\"]', 3);\n\t\t},\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end'\n\t\t\t}\n\t\t}\n\t},\n\t'scales': {",
        "$SM.add('stores[\"energy cell\"]', 3);\n\t\t},\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end',\n\t\t\t\tautoClick: 15\n\t\t\t}\n\t\t}\n\t},\n\t'scales': {"
    ),
    # Sick Man scales: 'say goodbye'
    (
        "$SM.add('stores.scales', 5);\n\t\t},\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end'\n\t\t\t}\n\t\t}\n\t},\n\t'nothing': {",
        "$SM.add('stores.scales', 5);\n\t\t},\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end',\n\t\t\t\tautoClick: 15\n\t\t\t}\n\t\t}\n\t},\n\t'nothing': {"
    ),
    # Sick Man nothing: 'say goodbye'
    (
        "'nothing': {\n\t\ttext: [\n\t\t\t_('the man expresses his thanks and hobbles off.')\n\t\t],\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end'\n\t\t\t}\n\t\t}\n\t}\n\t}\n\t}\n];",
        "'nothing': {\n\t\ttext: [\n\t\t\t_('the man expresses his thanks and hobbles off.')\n\t\t],\n\t\tbuttons: {\n\t\t\t'bye': {\n\t\t\t\ttext: _('say goodbye'),\n\t\t\t\tnextScene: 'end',\n\t\t\t\tautoClick: 15\n\t\t\t}\n\t\t}\n\t}\n\t}\n\t}\n];"
    ),
]

print('=== Patching room.js ===')
patch(ROOM, room_replacements)

# ==== global.js ====
GLOBAL = os.path.join(BASE, 'global.js')
global_replacements = [
    # Thief hang: 'leave'
    (
        "$SM.set('game.thieves', 2);\n\t\t\t\t$SM.remove('income.thieves');\n\t\t\t\t$SM.addM('stores', $SM.get('game.stolen'));\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'spare': {",
        "$SM.set('game.thieves', 2);\n\t\t\t\t$SM.remove('income.thieves');\n\t\t\t\t$SM.addM('stores', $SM.get('game.stolen'));\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'spare': {"
    ),
    # Thief spare: 'leave'
    (
        "$SM.set('game.thieves', 2);\n\t\t\t\t$SM.remove('income.thieves');\n\t\t\t\t$SM.addPerk('stealthy');\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\t}\n\t}\n];",
        "$SM.set('game.thieves', 2);\n\t\t\t\t$SM.remove('income.thieves');\n\t\t\t\t$SM.addPerk('stealthy');\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'leave': {\n\t\t\t\t\ttext: _('leave'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\t}\n\t}\n];"
    ),
]

print('=== Patching global.js ===')
patch(GLOBAL, global_replacements)

# ==== outside.js ====
OUTSIDE = os.path.join(BASE, 'outside.js')
outside_replacements = [
    # Ruined Traps start: 'ignore them'
    (
        "'ignore': {\n\t\t\t\t\ttext: _('ignore them'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'nothing': {\n\t\t\t\ttext: [\n\t\t\t\t\t_('the tracks disappear",
        "'ignore': {\n\t\t\t\t\ttext: _('ignore them'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 30\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'nothing': {\n\t\t\t\ttext: [\n\t\t\t\t\t_('the tracks disappear"
    ),
    # Ruined Traps nothing: 'go home'
    (
        "_('the tracks disappear after just a few minutes.'),\n\t\t\t\t\t_('the forest is silent.')\n\t\t\t\t],\n\t\t\t\tnotification: _('nothing was found'),\n\t\t\t\tbuttons: {\n\t\t\t\t\t'end': {\n\t\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\t\tnextScene: 'end'\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t},\n\t\t\t'catch': {",
        "_('the tracks disappear after just a few minutes.'),\n\t\t\t\t\t_('the forest is silent.')\n\t\t\t\t],\n\t\t\t\tnotification: _('nothing was found'),\n\t\t\t\tbuttons: {\n\t\t\t\t\t'end': {\n\t\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\t\tautoClick: 15\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t},\n\t\t\t'catch': {"
    ),
    # Ruined Traps catch: 'go home'
    (
        "reward: {\n\t\t\t\t\tfur: 100,\n\t\t\t\t\tmeat: 100,\n\t\t\t\t\tteeth: 10\n\t\t\t\t},\n\t\t\t\tbuttons: {\n\t\t\t\t\t'end': {\n\t\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\t\tnextScene: 'end'\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t},\n\t{ /* Hut fire */",
        "reward: {\n\t\t\t\t\tfur: 100,\n\t\t\t\t\tmeat: 100,\n\t\t\t\t\tteeth: 10\n\t\t\t\t},\n\t\t\t\tbuttons: {\n\t\t\t\t\t'end': {\n\t\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\t\tautoClick: 15\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t},\n\t{ /* Hut fire */"
    ),
    # Hut fire: 'mourn'
    (
        "'mourn': {\n\t\t\t\t\t\ttext: _('mourn'),\n\t\t\t\t\t\tnotification: _('some villagers have died'),\n\t\t\t\t\t\tnextScene: 'end'\n\t\t\t\t\t}",
        "'mourn': {\n\t\t\t\t\t\ttext: _('mourn'),\n\t\t\t\t\t\tnotification: _('some villagers have died'),\n\t\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\t\tautoClick: 20\n\t\t\t\t\t}"
    ),
    # Sickness healed: 'go home'
    (
        "'healed': {\n\t\t\ttext: [\n\t\t\t\t_('the sickness is cured in time.')\n\t\t\t],\n\t\t\tnotification: _('sufferers are healed'),\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'death': {\n\t\t\ttext: [\n\t\t\t\t_('the sickness spreads",
        "'healed': {\n\t\t\ttext: [\n\t\t\t\t_('the sickness is cured in time.')\n\t\t\t],\n\t\t\tnotification: _('sufferers are healed'),\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t'death': {\n\t\t\ttext: [\n\t\t\t\t_('the sickness spreads"
    ),
    # Sickness death: 'go home'
    (
        "_('the sickness spreads through the village.'),\n\t\t\t\t_('the days are spent with burials.'),\n\t\t\t\t_('the nights are rent with screams.')\n\t\t\t],\n\t\t\tnotification: _('sufferers are left to die'),\n\t\t\tonLoad: function() {\n\t\t\t\tvar numKilled = Math.floor(Math.random() * Math.floor($SM.get('game.population', true)/2)) + 1;\n\t\t\t\tOutside.killVillagers(numKilled);\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "_('the sickness spreads through the village.'),\n\t\t\t\t_('the days are spent with burials.'),\n\t\t\t\t_('the nights are rent with screams.')\n\t\t\t],\n\t\t\tnotification: _('sufferers are left to die'),\n\t\t\tonLoad: function() {\n\t\t\t\tvar numKilled = Math.floor(Math.random() * Math.floor($SM.get('game.population', true)/2)) + 1;\n\t\t\t\tOutside.killVillagers(numKilled);\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Plague healed: 'go home'
    (
        "'healed': {\n\t\t\ttext: [\n\t\t\t\t_('the plague is kept from spreading.'),\n\t\t\t\t_('only a few die.'),\n\t\t\t\t_('the rest bury them.')\n\t\t\t],\n\t\t\tnotification: _('epidemic is eradicated eventually'),\n\t\t\tonLoad: function() {\n\t\t\t\tvar numKilled = Math.floor(Math.random() * 5) + 2;\n\t\t\t\tOutside.killVillagers(numKilled);\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "'healed': {\n\t\t\ttext: [\n\t\t\t\t_('the plague is kept from spreading.'),\n\t\t\t\t_('only a few die.'),\n\t\t\t\t_('the rest bury them.')\n\t\t\t],\n\t\t\tnotification: _('epidemic is eradicated eventually'),\n\t\t\tonLoad: function() {\n\t\t\t\tvar numKilled = Math.floor(Math.random() * 5) + 2;\n\t\t\t\tOutside.killVillagers(numKilled);\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Plague death: 'go home'
    (
        "_('the plague rips through the village.'),\n\t\t\t\t_('the nights are rent with screams.'),\n\t\t\t\t_('the only hope is a quick death.')\n\t\t\t],\n\t\t\tnotification: _('population is almost exterminated'),\n\t\t\tonLoad: function() {\n\t\t\t\tvar numKilled = Math.floor(Math.random() * 80) + 10;\n\t\t\t\tOutside.killVillagers(numKilled);\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end'\n\t\t\t\t}",
        "_('the plague rips through the village.'),\n\t\t\t\t_('the nights are rent with screams.'),\n\t\t\t\t_('the only hope is a quick death.')\n\t\t\t],\n\t\t\tnotification: _('population is almost exterminated'),\n\t\t\tonLoad: function() {\n\t\t\t\tvar numKilled = Math.floor(Math.random() * 80) + 10;\n\t\t\t\tOutside.killVillagers(numKilled);\n\t\t\t},\n\t\t\tbuttons: {\n\t\t\t\t'end': {\n\t\t\t\t\ttext: _('go home'),\n\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\tautoClick: 15\n\t\t\t\t}"
    ),
    # Beast attack: 'go home'
    (
        "notification: _('predators become prey. price is unfair'),\n\t\t\t\t\t\tnextScene: 'end'\n\t\t\t\t\t}",
        "notification: _('predators become prey. price is unfair'),\n\t\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\t\tautoClick: 20\n\t\t\t\t\t}"
    ),
    # Military raid: 'go home'
    (
        "notification: _('warfare is bloodthirsty'),\n\t\t\t\t\t\tnextScene: 'end'\n\t\t\t\t\t}",
        "notification: _('warfare is bloodthirsty'),\n\t\t\t\t\t\tnextScene: 'end',\n\t\t\t\t\t\tautoClick: 20\n\t\t\t\t\t}"
    ),
]

print('=== Patching outside.js ===')
patch(OUTSIDE, outside_replacements)

print('\nAll done.')
