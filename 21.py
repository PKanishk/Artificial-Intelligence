class MonkeyBananaProblem:
    def __init__(self, room):
        self.room = room
        self.monkey_position = None
        self.box_position = None
        self.banana_position = None
        self.initialize_positions()

    def initialize_positions(self):
        for i in range(len(self.room)):
            for j in range(len(self.room[i])):
                if self.room[i][j] == 'M':
                    self.monkey_position = (i, j)
                elif self.room[i][j] == 'B':
                    self.box_position = (i, j)
                elif self.room[i][j] == 'X':
                    self.banana_position = (i, j)

    def is_valid_position(self, position):
        i, j = position
        return 0 <= i < len(self.room) and 0 <= j < len(self.room[0]) and self.room[i][j] != '#'

    def move_monkey(self, direction):
        di, dj = 0, 0
        if direction == 'up':
            di = -1
        elif direction == 'down':
            di = 1
        elif direction == 'left':
            dj = -1
        elif direction == 'right':
            dj = 1

        new_monkey_position = (self.monkey_position[0] + di, self.monkey_position[1] + dj)
        new_box_position = (self.box_position[0] + di, self.box_position[1] + dj)

        if self.is_valid_position(new_monkey_position):
            if new_monkey_position == self.box_position and self.is_valid_position(new_box_position):
                self.monkey_position = new_monkey_position
                self.box_position = new_box_position
                print("Monkey pushed the box.")
            elif new_monkey_position == self.banana_position:
                print("Monkey reached the bananas! Problem solved.")
            else:
                self.monkey_position = new_monkey_position
                print("Monkey moved.")
        else:
            print("Invalid move.")

    def display_room(self):
        for i in range(len(self.room)):
            for j in range(len(self.room[i])):
                if (i, j) == self.monkey_position:
                    print('M', end=' ')
                elif (i, j) == self.box_position:
                    print('B', end=' ')
                elif (i, j) == self.banana_position:
                    print('X', end=' ')
                elif self.room[i][j] == '#':
                    print('#', end=' ')
                else:
                    print('-', end=' ')
            print()


room = [
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', 'M', '-', '-', '-', '-'],
    ['-', '-', '-', 'B', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', 'X', '-']
]

monkey_problem = MonkeyBananaProblem(room)
monkey_problem.display_room()

while True:
    direction = input("Enter direction (up, down, left, right): ")
    monkey_problem.move_monkey(direction)
    monkey_problem.display_room()
