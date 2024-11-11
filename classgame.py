import matplotlib.pyplot as plt
#Easy
# matrix1=[
#     [0, 0, 0, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 'M', 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 'R', 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1]
# ]
#Medium
# matrix1 = [
#     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 'M', 0, 0, 1, 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 'B', 'A', 1,1],
#     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# ]
#Hard
matrix1=[
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 'L', 1, 'M', 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 'O', 'R', 'B', 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 'A', 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1]
]


class Cell:
    def __init__(self, value):
        self.value = value
        self.border_color = self.get_border_color()

    def get_border_color(self):
        border_colors = {
            'M': 'red',
            'A': 'blue',
            'L': 'orange'
        }
        return border_colors.get(self.value, None)

    def get_color(self):
        colors = {
            1: 'black',
            'R': 'red',
            'B': 'blue',
            'M': 'white',
            'A': 'white',
            'L': 'white',
            'O': 'orange'
        }
        return colors.get(self.value, 'white')


class State:
    def __init__(self, matrix):
        self.matrix = [[Cell(value) for value in row] for row in matrix]
        self.fig, self.ax = plt.subplots()
        self.plot_binary_matrix()
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

    def plot_binary_matrix(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        self.ax.clear()

        for i in range(rows):
            for j in range(cols):
                cell = self.matrix[i][j]
                color = cell.get_color()
                rect = plt.Rectangle((j, i), 1, 1, color=color)
                self.ax.add_patch(rect)

                if cell.border_color:
                    self.add_border(i, j, cell.border_color)

        self.ax.set_xlim([0, cols])
        self.ax.set_ylim([0, rows])
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        plt.draw()

    def add_border(self, i, j, border_color):
        border_rect = plt.Rectangle((j, i), 1, 1, edgecolor=border_color, facecolor='none', linewidth=2)
        self.ax.add_patch(border_rect)

    def can_move(self, i, j, direction):
        if direction == 'right':
            return j + 1 < len(self.matrix[0]) and self.matrix[i][j + 1].value not in [1, 'R', 'B', 'O']
        elif direction == 'left':
            return j - 1 >= 0 and self.matrix[i][j - 1].value not in [1, 'R', 'B', 'O']
        elif direction == 'down':
            return i + 1 < len(self.matrix) and self.matrix[i + 1][j].value not in [1, 'R', 'B', 'O']
        elif direction == 'up':
            return i - 1 >= 0 and self.matrix[i - 1][j].value not in [1, 'R', 'B', 'O']
        return False

    def move(self, direction):
        positions = [(i, j) for i in range(len(self.matrix)) for j in range(len(self.matrix[0])) if self.matrix[i][j].value in ['R', 'B', 'O']]
        for (i, j) in positions:
            new_i, new_j = i, j
            while self.can_move(new_i, new_j, direction):
                if direction == 'right':
                    new_j += 1
                elif direction == 'left':
                    new_j -= 1
                elif direction == 'down':
                    new_i += 1
                elif direction == 'up':
                    new_i -= 1

                
                self.check_and_update_goal(new_i, new_j)

            if (new_i, new_j) != (i, j):
                self.matrix[new_i][new_j].value = self.matrix[i][j].value
                self.matrix[i][j].value = 0

        self.plot_binary_matrix()

    def check_and_update_goal(self, i, j):
        """
        تحقق مما إذا كانت الخلية المتحركة تطابق لون الحواف للخلية الهدف.
        في حال التطابق، يتم تغيير لون الخلية الهدف بالكامل إلى الأبيض.
        """
        cell = self.matrix[i][j]

        # خريطة تربط الخلايا المتحركة بالخلايا الهدف وألوانها
        goal_map = {
            'R': 'M',
            'B': 'A',
            'O': 'L'
        }

        if cell.value in goal_map:  # إذا كانت الخلية متحركة
            target_value = goal_map[cell.value]
            for row in self.matrix:
                for target_cell in row:
                    if target_cell.value == target_value and target_cell.border_color == cell.get_color():
                        target_cell.value = 0  # تحويل الخلية الهدف للون الأبيض
                        target_cell.border_color = 'white'  # تغيير حافة الخلية إلى الأبيض

    def on_key_press(self, event):
        if event.key == 'right':
            self.move('right')
        elif event.key == 'left':
            self.move('left')
        elif event.key == 'down':
            self.move('down')
        elif event.key == 'up':
            self.move('up')


state_instance = State(matrix1)
plt.show()