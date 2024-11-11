import matplotlib.pyplot as plt
from copy import deepcopy

# مصفوفة اللعبة
matrix = [
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

fixed_targets = {
    (1, 4): 'M',
    (5, 5): 'A',
    (4, 8): 'L'
}

class State:
    def __init__(self, matrix):
        self.matrix = matrix
        self.target_borders = [['red' if cell == 'M' else 'aqua' if cell == 'A' else 'orange' if cell == 'L' else None for cell in row] for row in matrix]
        self.fig, self.ax = plt.subplots(figsize=(8, 12))  # تغيير الحجم ليكون عمودي
        self.print(self.matrix, self.ax)
        self.fig.canvas.mpl_connect('key_press_event', self.press)

    def print(self, matrix, ax):
        rows_len = len(matrix)
        colums_len = len(matrix[0])
        ax.clear()

        for i in range(rows_len):
            for j in range(colums_len):
                if matrix[i][j] == 1:
                    color = 'black'
                elif matrix[i][j] == 'R':
                    color = 'red'
                elif matrix[i][j] == 'B':
                    color = 'aqua'
                elif matrix[i][j] == 'O':
                    color = 'orange'
                else:
                    color = 'white'  

                # رسم المستطيلات
                draw = plt.Rectangle((j, -i), 1, 1, color=color)  # عكس الإحداثيات
                ax.add_patch(draw)

                border_color = self.target_borders[i][j]
                if border_color is not None:
                    border_draw = plt.Rectangle((j + 0.15, -i + 0.15), 0.7, 0.7, edgecolor=border_color, facecolor='none', linewidth=2)
                    ax.add_patch(border_draw)

        ax.set_xlim([0, colums_len])
        ax.set_ylim([-rows_len, 0])  # عكس المحور Y
        ax.set_xticks([])
        ax.set_yticks([])

    def move1(self, matrix, direction):
        matrix_copy = deepcopy(matrix)
        positions = self.get_positions(matrix_copy)

        for (i, j) in positions:
            new_i, new_j = self.move_square(matrix_copy, i, j, direction)
            self.update_matrix(matrix_copy, i, j, new_i, new_j)

        return matrix_copy
    
    def get_positions(self, matrix):
        return [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] in ['R', 'B', 'O']]

    def move_square(self, matrix, i, j, direction):
        new_i, new_j = i, j
        while self.able_to_move(matrix, new_i, new_j, direction):
            new_i, new_j = self.calculate_new_position(new_i, new_j, direction)
            self.check(matrix, i, j, new_j, new_i)
        return new_i, new_j
    
    def calculate_new_position(self, i, j, direction):
        if direction == 'right':
            j += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'up':
            i -= 1
        return i, j
    
    def update_matrix(self, matrix, old_i, old_j, new_i, new_j):
        if (new_i, new_j) != (old_i, old_j):
            matrix[new_i][new_j] = matrix[old_i][old_j]
            matrix[old_i][old_j] = 0

    def able_to_move(self, matrix, i, j, direction):
        if direction == 'right':
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] not in [1, 'R', 'B', 'O']:
                return True
        elif direction == 'left':
            if j - 1 >= 0 and matrix[i][j - 1] not in [1, 'R', 'B', 'O']:
                return True
        elif direction == 'down':
            if i + 1 < len(matrix) and matrix[i + 1][j] not in [1, 'R', 'B', 'O']:
                return True
        elif direction == 'up':
            if i - 1 >= 0 and matrix[i - 1][j] not in [1, 'R', 'B', 'O']:
                return True
        return False

    def check(self, matrix, i, j, new_j, new_i):
        goals = {
            'R': 'M',
            'B': 'A',
            'O': 'L'}
        if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
            square = matrix[i][j]
            target = self.matrix[new_i][new_j]
        
            if square in goals and target == goals[square]:
                matrix[new_i][new_j] = 0
                self.target_borders[new_i][new_j] = None

    def press(self, event):
        if event.key == 'right':
            self.move2('right')
        elif event.key == 'left':
            self.move2('left')
        elif event.key == 'up':
            self.move2('up')
        elif event.key == 'down':
            self.move2('down')

        self.print(self.matrix, self.ax)
        plt.draw()

    def move2(self, direction):
        self.matrix = self.move1(self.matrix, direction)
        self.print(self.matrix, self.ax)
        plt.draw()

# إنشاء كائن من الفئة State وعرض الواجهة
State_instance = State(matrix)
plt.show()