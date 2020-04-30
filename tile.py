

class Tile:

    def __init__(self, name, selectable = True):
        self.name = name;
        self.selectable = selectable;
        self.id = "tile";

    def get_name(self):
        return self.name;

    def get_id(self):
        return self.id;

    def set_select(self, select):
        self.selectable = select;

    def can_select(self):
        return self.selectable;

    def __str__(self):
        return "Tile('{self.name}', {self.selectable})".format(self=self);

    def __repr__(self):
        return "Tile('{self.name}', {self.selectable})".format(self=self);
