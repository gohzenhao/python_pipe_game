from tile import *;
from abc import ABC, abstractmethod;
## straight : 0 or 2 = N / S , 1 or 3 = E / W
## corner : 0 = N / E , 1 = E / S , 2 = S / W , 3 = N / W
## cross : 0 or 1 or 2 or 3 = N / E / S / W
## junction-t : 1 = E / S / W , 2 = N / S / W , 3 = N / E / W , 4 = N / E / S
## diagonals: 0 or 2 = [N / E] & [S / W] , 1 or 3 = [N / W] & [E / S]
## over-under: 0 or 2 = [N / S] & [E / W] , 1 or 3 =
class Pipe(Tile):

    def __init__(self, name, orientation = 0, selectable = True):
        super().__init__(name, selectable);
        self.orientation = orientation;
        self.id = 'pipe';
        self.list = {
            'N': [],
            'E': [],
            'S': [],
            'W': []
        };
        self.set_connected();


    # Set the list based on the pipe type + orientation
    def set_connected(self):
        self.list = {
            'N': [],
            'E': [],
            'S': [],
            'W': []
        };

        if self.name == 'straight':
            if self.orientation == 0 or self.orientation == 2:
                self.list['N'].append('S');
                self.list['S'].append('N');
            if self.orientation == 1 or self.orientation == 3:
                self.list['E'].append('W');
                self.list['W'].append('E');

        elif self.name == 'corner':
            if self.orientation == 0:
                self.list['N'].append('E');
                self.list['E'].append('N');
            elif self.orientation == 1:
                self.list['E'].append('S');
                self.list['S'].append('E');
            elif self.orientation == 2:
                self.list['S'].append('W');
                self.list['W'].append('S');
            elif self.orientation == 3:
                self.list['N'].append('W');
                self.list['W'].append('N');

        elif self.name == 'cross':
            self.list['N'].append('E');
            self.list['N'].append('S');
            self.list['N'].append('W');

            self.list['E'].append('N');
            self.list['E'].append('S');
            self.list['E'].append('W');

            self.list['S'].append('N');
            self.list['S'].append('E');
            self.list['S'].append('W');

            self.list['W'].append('N');
            self.list['W'].append('E');
            self.list['W'].append('S');

        elif self.name == 'junction-t':
            if self.orientation == 0:
                self.list['E'].append('S');
                self.list['E'].append('W');

                self.list['S'].append('E');
                self.list['S'].append('W');

                self.list['W'].append('E');
                self.list['W'].append('S');

            elif self.orientation == 1:
                self.list['N'].append('S');
                self.list['N'].append('W');

                self.list['S'].append('N');
                self.list['S'].append('W');

                self.list['W'].append('N');
                self.list['W'].append('S');
            elif self.orientation == 2:
                self.list['N'].append('E');
                self.list['N'].append('W');

                self.list['E'].append('N');
                self.list['E'].append('W');

                self.list['W'].append('N');
                self.list['W'].append('E');
            elif self.orientation == 3:
                self.list['N'].append('S');
                self.list['N'].append('E');

                self.list['E'].append('N');
                self.list['E'].append('S');

                self.list['S'].append('N');
                self.list['S'].append('E');
        elif self.name == 'diagonals':
            if self.orientation == 0 or self.orientation == 2:
                self.list['N'].append('E');
                self.list['E'].append('N');

                self.list['S'].append('W');
                self.list['W'].append('S');

            elif self.orientation == 1 or self.orientation == 3:
                self.list['N'].append('W');
                self.list['W'].append('N');

                self.list['E'].append('S');
                self.list['S'].append('E');

        elif self.name == 'over-under':
            self.list['N'].append('S');
            self.list['S'].append('N');

            self.list['E'].append('W');
            self.list['W'].append('E');

    def get_connected(self, d):
        return self.list[d];

    def get_orientation(self):
        return self.orientation;

    def rotate(self, direction):
        current_orientation = self.orientation + direction;
        if current_orientation == 4 or current_orientation == 0:
            self.orientation = 0;
        elif current_orientation == 1:
            self.orientation = 1;
        elif current_orientation == 2:
            self.orientation = 2;
        elif current_orientation == -1 or current_orientation == 3:
            self.orientation = 3;

        self.set_connected();

    def __str__(self):
        return "Pipe('{self.name}', {self.orientation})".format(self=self);

    def __repr__(self):
        return "Pipe('{self.name}', {self.orientation})".format(self=self);

class SpecialPipe(Pipe):

    def __init__(self, name, orientation = 0):
        super().__init__(name, orientation, selectable = False);
        self.id = "special_pipe";


    def __str__(self):
        return "SpecialPipe({self.orientation})".format(self=self);


    def __repr__(self):
        return "SpecialPipe({self.orientation})".format(self=self);



class StartPipe(SpecialPipe):

    def __init__(self,  orientation = 0):
        super().__init__(orientation)
        self.face = []
        self.set_connected()
        self.name = "start"

    def __str__(self):
        return "StartPipe({self.orientation})".format(self=self);

    def __repr__(self):
        return "StartPipe({self.orientation})".format(self=self);

    def get_connected(self, side = None):
        return self.face;

    def set_connected(self):
        self.face = [];
        if self.orientation == 3 or self.orientation == -1:
            self.face.append('W');
        elif self.orientation == 1:
            self.face.append('E');
        elif self.orientation == 2:
            self.face.append('S');
        elif self.orientation == 0 or self.orientation == 4:
            self.face.append('N');


class EndPipe(SpecialPipe):

    def __init__(self, orientation = 0):
        super().__init__(orientation);
        self.face = [];
        self.set_connected();
        self.name = 'end';

    def __str__(self):
        return "EndPipe({self.orientation})".format(self=self);

    def __repr__(self):
        return "EndPipe({self.orientation})".format(self=self);

    def get_connected(self, side = None):
        return self.face;

    def set_connected(self):
        self.face = [];
        if self.orientation == 3 or self.orientation == -1:
            self.face.append('E');
        elif self.orientation == 1:
            self.face.append('W');
        elif self.orientation == 2:
            self.face.append('N');
        elif self.orientation == 0 or self.orientation == 4:
            self.face.append('S');
