import copy
import matplotlib.pyplot as plt

class State:
    # last_saved_state = None
    def __init__(self, mattrix):
        if mattrix is None:
            print("The matrix cannot be None")
        self.mattrix = mattrix
        self.goal_cells = [['red' if cell == 'M' else 'aqua' if cell == 'A' else 'orange' if cell == 'L' else None for cell in row] for row in mattrix]

    def print(self, mattrix, ax):#لطباعة الرقعة مع الالوان
        rows_len = len(mattrix)
        colums_len = len(mattrix[0])
        ax.clear()

        for i in range(rows_len):
            for j in range(colums_len):
                if mattrix[i][j] == 1:
                    color = 'black'
                elif mattrix[i][j] == 'R':
                    color = 'red'
                elif mattrix[i][j] == 'B':
                    color = 'aqua'
                elif mattrix[i][j] == 'O':
                    color = 'orange'
                else:
                    color = 'white'

                draw = plt.Rectangle((j, i), 1.5, 1.5, color=color)
                ax.add_patch(draw)

                border_c = self.goal_cells[i][j]
                if border_c is not None:
                    border_draw = plt.Rectangle((j, i), 0.7, 0.7, edgecolor=border_c, facecolor='none', linewidth=2)
                    ax.add_patch(border_draw)

        ax.set_xlim([0, colums_len])
        ax.set_ylim([0, rows_len])
        plt.draw()

    def move1(self, state_obj, dir):#بمرر المصفوفة على شكل اوبجيكت 
        mattrix_copy = copy.deepcopy(state_obj.mattrix)# عملت نسخة من المصفوفة الاصلية بال deepcopy لحتى لما عدل ما تتأثر المصفوفة الاصلية 
        positions = self.get_loc(mattrix_copy)
        for (i, j) in positions:
            new_i, new_j = self.move2(mattrix_copy, i, j, dir)
            if (new_i, new_j) != (i, j):
                self.update_mattrix(mattrix_copy, i, j, new_i, new_j)
        
        return State(mattrix_copy)


    def get_loc(self, mattrix):#ليرجعلي احداثيات المربعات الملونة 
            return [(i, j) for i in range(len(mattrix)) for j in range(len(mattrix[0])) if mattrix[i][j] in ['R', 'B', 'O']]

    def move2(self, mattrix, i, j, dir):
        new_i, new_j = i, j
        while self.able_to_move(mattrix, new_i, new_j, dir):
            new_i, new_j = self.new_position(new_i, new_j, dir)
            self.check(mattrix, i, j, new_j, new_i)
        return new_i, new_j

    def new_position(self, i, j, dir):
        if dir == 'right':
            j += 1
        elif dir == 'left':
            j -= 1
        elif dir == 'up':
            i += 1
        elif dir == 'down':
            i -= 1
        return i, j

    def update_mattrix(self, mattrix, old_i, old_j, new_i, new_j):#ليحدث المصفوفة بعد الحركة 
        if (new_i, new_j) != (old_i, old_j):
            mattrix[new_i][new_j] = mattrix[old_i][old_j]
            mattrix[old_i][old_j] = 0

    def able_to_move(self, mattrix, i, j, dir):# بيتأكد انو مافي شي بعيق الحركة بهاد الاتجاه
        if (self.move_to_right(mattrix, i, j, dir) or
            self.move_to_left(mattrix, i, j, dir) or
            self.move_to_up(mattrix, i, j, dir) or
            self.move_to_down(mattrix, i, j, dir)):
            return True
        return False

    def move_to_right(self, mattrix, i, j, dir):
        if dir == 'right':
            if j + 1 < len(mattrix[0]) and mattrix[i][j + 1] not in [1, 'R', 'B', 'O']:# jبتمشي عالاعمدة
                return True
        return False

    def move_to_left(self, mattrix, i, j, dir):
        if dir == 'left':
            if j - 1 >= 0 and mattrix[i][j - 1] not in [1, 'R', 'B', 'O']:
                return True
        return False

    def move_to_up(self, mattrix, i, j, dir):
        if dir == 'up':
            if i + 1 < len(mattrix) and mattrix[i + 1][j] not in [1, 'R', 'B', 'O']:#ه بتمشي عالسطور
                return True
        return False

    def move_to_down(self, mattrix, i, j, dir):
        if dir == 'down':
            if i - 1 >= 0 and mattrix[i - 1][j] not in [1, 'R', 'B', 'O']:
                return True
        return False

    def check(self, mattrix, i, j, new_j, new_i):#هدف للابيض بيتأكد من انو المربع الملون وصل للهدف الصح و بغير لون البوردر لل
        goals = {
            'R': 'M',
            'B': 'A',
            'O': 'L'
        }

        if 0 <= new_i < len(mattrix) and 0 <= new_j < len(mattrix[0]):
            square = mattrix[i][j]
            target = self.mattrix[new_i][new_j]
            if square in goals and target == goals[square]:
                mattrix[new_i][new_j] = 0
                self.goal_cells[new_i][new_j] = None
                self.change_color(mattrix, i, j)
        if self.check_win(mattrix):
            print("You Win :)")

    def change_color(self, mattrix, i, j):#بعد ما يوصل للهدف بيقلب لونو لابيض
        if mattrix[i][j] in ['R', 'B', 'O']:
            mattrix[i][j] = 'white'

    def check_win(self, mattrix):
        goals_reached = {
            'R': 'M',
            'B': 'A',
            'O': 'L'}

        for i in range(len(mattrix)):
            for j in range(len(mattrix[0])):
                cell = mattrix[i][j]
                if cell in goals_reached and mattrix[i][j] != 'white':
                    return False
        return True
