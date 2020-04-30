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

### add code here ###
from pipe import *;
class PipeGame:
    """
    A game of Pipes.
    """
    def __init__(self, game_file='game_1.csv'):
        """
        Construct a game of Pipes from a file name.

        Parameters:
            game_file (str): name of the game file.
        """
        #########################COMMENT THIS SECTION OUT WHEN DOING load_file#######################
        self.board_layout = [[Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Tile('tile', True)], [StartPipe(1), Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Tile('tile', True), Tile('tile', True)], [Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Pipe('junction-t', 0, False), Tile('tile', True), Tile('tile', True)], [Tile('tile', True), \
        Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('locked', False), Tile('tile', True)], \
        [Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('tile', True), EndPipe(3), \
        Tile('tile', True)], [Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Tile('tile', True)]];

        self.playable_pipes = {'straight': 1, 'corner': 1, 'cross': 1, 'junction-t': 1, 'diagonals': 1, 'over-under': 1};

        self.start_pipe = None;
        self.end_pipe = None;

        self.end_pipe_positions();
        #########################COMMENT THIS SECTION OUT WHEN DOING load_file#######################

        ### add code here ###
    def get_board_layout(self):
        return self.board_layout;

    def get_playable_pipes(self):
        return self.playable_pipes;

    def change_playable_amount(self, name, amount):
        self.playable_pipes[name] += amount;

    def get_pipe(self, position):
        row = position[0];
        col = position[1];
        return self.board_layout[row][col];

    def set_pipe(self, pipe, position):
        self.board_layout[position[0]][position[1]] = pipe;
        self.change_playable_amount(pipe.get_name(), -1);


    def pipe_in_position(self, position):
        if(isinstance(self.board_layout[position[0]][position[1]], Pipe)):
            return self.board_layout[position[0]][position[1]];
        return None;

    def remove_pipe(self, position):
        pipe = self.board_layout[position[0]][position[1]];
        self.change_playable_amount(pipe.get_name(), 1);
        self.board_layout[position[0]][position[1]] = Tile('tile', True);

    def position_in_direction(self, direction, position):
        d = None;
        row = position[0];
        col = position[1];
        if direction == 'N' :
            row -= 1;
            d = 'S';
        elif direction == 'E':
            col += 1;
            d = 'W';
        elif direction == 'S':
            row += 1;
            d = 'N';
        elif direction == 'W':
            col -= 1;
            d = 'E';

        if row < 0 or row > len(self.board_layout) - 1 or col< 0 or col> len(self.board_layout[0]) - 1:
            return None;

        return (d, (row, col));

    def end_pipe_positions(self):
        for i in range(len(self.board_layout)):
            for j in range(len(self.board_layout[0])):
                if isinstance(self.board_layout[i][j], StartPipe):
                    self.start_pipe = (i,j);
                elif isinstance(self.board_layout[i][j], EndPipe):
                    self.end_pipe = (i, j);

    def get_starting_position(self):
        return self.start_pipe;

    def get_ending_position(self):
        return self.end_pipe;


    #########################UNCOMMENT THIS FUNCTION WHEN READY#######################
    def check_win(self):
        """
        (bool) Returns True  if the player has won the game False otherwise.
        """
        position = self.get_starting_position()
        pipe = self.pipe_in_position(position)
        queue = [(pipe, None, position)]
        discovered = [(pipe, None)]
        while queue:
            pipe, direction, position = queue.pop()
            for direction in pipe.get_connected(direction):

                if self.position_in_direction(direction, position) is None:
                    new_direction = None
                    new_position = None
                else:
                    new_direction, new_position = self.position_in_direction(direction, position)
                if new_position == self.get_ending_position() and direction == self.pipe_in_position(
                        new_position).get_connected()[0]:
                    return True
                pipe = self.pipe_in_position(new_position)
                if pipe is None or (pipe, new_direction) in discovered:
                    continue
                discovered.append((pipe, new_direction))
                queue.append((pipe, new_direction, new_position))
        return False
    #########################UNCOMMENT THIS FUNCTION WHEN READY#######################


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
