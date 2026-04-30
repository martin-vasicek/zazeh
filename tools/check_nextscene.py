import re

for fname in ['script/events/room.js', 'script/events/global.js', 'script/events/outside.js']:
    print(f'\n\n===== {fname} =====')
    with open(fname, 'r', encoding='utf-8', newline='') as f:
        content = f.read()
    pattern = re.compile(r"nextScene: 'end'(?!\s*,\s*\r?\nautoClick)")
    for m in pattern.finditer(content):
        s = max(0, m.start()-200)
        e = min(len(content), m.end()+150)
        print('---')
        print(repr(content[s:e]))
        print()
