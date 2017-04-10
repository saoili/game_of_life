from random import choice
from time import sleep


class GameOfLife(object):

    def __init__(self, width, height=None):
        if not height:
            height = width
        self.width = width
        self.height = height
        self.grid = {}
        for x in xrange(width):
            for y in xrange(height):
                self.grid[(x, y)] = 0
        self.random_seed()

    def seed(self):
        self.grid[(1, 2)] = 1
        self.grid[(3, 2)] = 1
        self.grid[(2, 3)] = 1
        self.grid[(2, 5)] = 1
        self.grid[(4, 3)] = 1
        self.grid[(4, 4)] = 1

    def random_seed(self):
        # making not-life slightly more likely
        for key in self.grid:
            self.grid[key] = choice((0, 0, 1))

    def basic_print(self):
        print "\n"
        for y in xrange(self.height):
            for x in xrange(self.width):
                if self.grid[(x, y)]:
                    print "x",
                else:
                    print "_",
            print

    def total_around(self, old_x, old_y):
        total = 0
        x_map = {-1: self.width - 1, self.width: 0}
        y_map = {-1: self.height - 1, self.height: 0}

        for x in xrange(old_x - 1, old_x + 2):
            temp_x = x_map.get(x, x)
            for y in xrange(old_y - 1, old_y + 2):
                temp_y = y_map.get(y, y)
                total += self.grid[(temp_x, temp_y)]
        return total

    def next_value(self, x, y):
        """
        if the current is 0 and there are 3 around -> reproduction
        if the current is 1 and there are 2 around -> maintenence
        --> total of 3 -> live
        if the current is 0 and there are 4 around -> overpopulation
        if the current is 1 and there are 3 around -> maintenence
        --> total of 4 -> keep the same current_value
        total of less than 3 -> underpopulation
        total of more than 4 -> overpopulation
        """
        current_value = self.grid[x, y]
        total = self.total_around(x, y)
        if total == 3:
            return 1
        if total == 4:
            return current_value
        return 0

    def tick(self):
        self.new_grid = {key: self.next_value(*key) for key in self.grid}
        self.grid = self.new_grid


if __name__ == "__main__":
    g = GameOfLife(15, 13)
    ticks = 20
    sleep_time = 1
    for i in xrange(ticks + 1):
        sleep(sleep_time)
        g.basic_print()
        g.tick()
