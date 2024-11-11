import matplotlib.pyplot as plt
from copy import deepcopy
# import matplotlib.colors as mcolors
#Easy
# matrix=[
#     [0, 0, 0, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 'M', 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 'R', 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1]
# ]
#Medium
# matrix = [
#     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 'M', 0, 0, 0, 'B', 'A', 1,1],
#     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# ]
##########bad
matrix=[
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 'L', 1, 'M', 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 'O', 'R', 'B', 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 'A', 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1]
]
###########
# matrix = [
#     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 'O', 1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 0, 'A', 0, 'L', 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 'M', 0, 'B', 0, 1, 1],
#     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# ]
##########################################
# matrix = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#     [1, 0, 0, 1, 'M', 0, 0, 0, 1, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
#     [1, 'A', 1, 0, 0, 0, 0, 1, 'L', 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
#     [1, 1, 1, 'B', 'R', 'O', 1, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
# ]
###########
# matrix = [
#     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 'O', 1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 0, 'A', 0, 'L', 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 'M', 0, 'B', 0, 1, 1],
#     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# ]
fixed_targets = {
    (1, 4): 'M',
    (5, 5): 'A',
    (4, 8): 'L'
}
class State:
    def __init__(self, matrix):
        self.matrix = matrix
        self.target_borders = [['red' if cell == 'M' else 'aqua' if cell == 'A' else 'orange' if cell == 'L' else None for cell in row] for row in matrix]
        self.fig, self.ax = plt.subplots(1, 5, figsize=(15, 3))
        self.print(self.matrix, self.ax[0])
        self.fig.canvas.mpl_connect('key_press_event', self.press)
        self.state_history = []  

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

                draw = plt.Rectangle((j, i), 1.5, 1.5, color=color)
                ax.add_patch(draw)

                border_c = self.target_borders[i][j]
                if border_c is not None:
                    border_draw = plt.Rectangle((j, i), 0.7, 0.7, edgecolor=border_c, facecolor='none', linewidth=2)
                    ax.add_patch(border_draw)

        ax.set_xlim([0, colums_len])
        ax.set_ylim([0, rows_len])
        
        plt.draw()

    def move1(self, matrix, direction):
        matrix_copy = deepcopy(matrix)  
        positions = self.get_positions(matrix_copy)  
    
        for (i, j) in positions:
            new_i, new_j = self.move_square(matrix_copy, i, j, direction)
            if (new_i, new_j) != (i, j):  
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
        elif direction == 'up':
            i += 1
        elif direction == 'down':
            i -= 1
        return i, j
    
    def update_matrix(self, matrix, old_i, old_j, new_i, new_j):
        if (new_i, new_j) != (old_i, old_j):
            matrix[new_i][new_j] = matrix[old_i][old_j]
            matrix[old_i][old_j] = 0
    
    def move_to_right(self, matrix, i, j, direction):
        if direction == 'right':
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] not in [1, 'R', 'B', 'O']:
                return True
        return False

    def move_to_left(self, matrix, i, j, direction):
        if direction == 'left':
            if j - 1 >= 0 and matrix[i][j - 1] not in [1, 'R', 'B', 'O']:
                return True
        return False

    def move_to_up(self, matrix, i, j, direction):
        if direction == 'up':
            if i + 1 < len(matrix) and matrix[i + 1][j] not in [1, 'R', 'B', 'O']:
                return True
        return False

    def move_to_down(self, matrix, i, j, direction):
        if direction == 'down':
            if i - 1 >= 0 and matrix[i - 1][j] not in [1, 'R', 'B', 'O']:
                return True
        return False

    def able_to_move(self, matrix, i, j, direction):
        if (self.move_to_right(matrix, i, j, direction) or 
            self.move_to_left(matrix, i, j, direction) or 
            self.move_to_up(matrix, i, j, direction) or 
            self.move_to_down(matrix, i, j, direction)):
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
            self.attempt_move('right')
        elif event.key == 'left':
            self.attempt_move('left')
        elif event.key == 'up':
            self.attempt_move('up')
        elif event.key == 'down':
            self.attempt_move('down')

        directions = ['right', 'left', 'up', 'down']
        for idx, direction in enumerate(directions, start=1):
            simulated_matrix = self.move1(self.matrix, direction)
            self.print(simulated_matrix, self.ax[idx])
        
        plt.draw()

    def attempt_move(self, direction):
        if any(self.able_to_move(self.matrix, i, j, direction) for i, j in self.get_positions(self.matrix)):
            new_matrix = self.move1(self.matrix, direction)
            self.state_history.append(deepcopy(new_matrix))  
            print(f"State {len(self.state_history)} after {direction}:\n")
            for row in new_matrix:
                print(row)
                print("-" * 20)
            self.matrix = new_matrix  
            self.print(self.matrix, self.ax[0])
            plt.draw()

State_instance = State(matrix)
plt.show()