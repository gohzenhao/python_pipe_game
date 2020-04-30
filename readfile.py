EMPTY_TILE = "tile"
START_PIPE = "start"
END_PIPE = "end"
LOCKED_TILE = "locked"

SPECIAL_TILES = {
    "S": START_PIPE,
    "E": END_PIPE,
    "L": LOCKED_TILE
}

PIPES = {
    "ST": "straight",
    "CO": "corner",
    "CR": "cross",
    "JT": "junction-t",
    "DI": "diagonals",
    "OU": "over-under"
}

import csv
import sys

from pipe import *;

board_layout = [];
playable_pipes = {
    'straight': 0,
    'corner': 0,
    'cross': 0,
    'junction': 0,
    'diagonals': 0,
    'over-under': 0
}
f = open('game_1.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        l = [];
        for a in row:
            if a == '#':
                l.append(Tile('tile', True));
            if 'ST' in a:
                if len(a) == 2:
                    l.append(Pipe('straight',0, False));
                else:
                    l.append(Pipe('straight',int(a[-1]), False));
            elif 'CO' in a:
                if len(a) == 2:
                    l.append(Pipe('corner',0, False));
                else:
                    l.append(Pipe('corner',int(a[-1]), False));
            elif 'CR' in a:
                if len(a) == 2:
                    l.append(Pipe('cross',0, False));
                else:
                    l.append(Pipe('cross',int(a[-1]), False));
            elif 'JT' in a:
                if len(a) == 2:
                    l.append(Pipe('junction-t',0, False));
                else:
                    l.append(Pipe('junction-t',int(a[-1]), False));
            elif 'DI' in a:
                if len(a) == 2:
                    l.append(Pipe('diagonal',0, False));
                else:
                    l.append(Pipe('diagonal',int(a[-1]), False));
            elif 'OU' in a:
                if len(a) == 2:
                    l.append(Pipe('over-under',0, False));
                else:
                    l.append(Pipe('over-under',int(a[-1]), False));
            elif 'S' in a:
                if len(a) == 1:
                    l.append(StartPipe());
                else:
                    print("what");
                    l.append(StartPipe(int(a[-1])));
            elif 'E' in a:
                if len(a) == 1:
                    l.append(EndPipe());
                else:
                    l.append(EndPipe(int(a[-1])));
            elif 'L' in a:
                l.append(Tile('locked',False));


        board_layout.append(l);

finally:
    f.close()

print(board_layout);

a = 'abc';
b = 'abc';
