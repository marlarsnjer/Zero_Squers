import time
import matplotlib.pyplot as plt
from collections import deque
import copy
class Play:
    def __init__(self, state_ins):
        self.state_ins = state_ins
        self.fig, self.ax = plt.subplots(1, 1, figsize=(19, 15))
        self.state_ins.print(self.state_ins.mattrix, self.ax)
        self.ax.set_title("BFS Search")
        plt.tight_layout() 

    def press(self, event):
        self.next_state()

    def next_state(self):
        dir = ['right', 'left', 'up', 'down']
        s_obj = []
        for idx, dir in enumerate(dir, start=1):
            n_state = self.state_ins.move1(self.state_ins, dir)
            s_obj.append(n_state)
            n_state.print(n_state.mattrix, self.ax)
        plt.draw()

    def h_move(self, dir, is_bfs=True):
        self.pre_mattrix = [row[:] for row in self.state_ins.mattrix]
        n_state_ins = self.state_ins.move1(self.state_ins, dir)
        self.state_ins = n_state_ins
        if is_bfs:
            self.state_ins.print(self.state_ins.mattrix, self.ax)

        plt.draw()

    def bfs(self):
        initial_state = self.state_ins
        queue = deque([(initial_state, [])])  
        visited_states = set()

        while queue:
            current_state, current_path = queue.popleft()
            state_key = str(current_state.mattrix)  
            if state_key in visited_states:
                continue
            visited_states.add(state_key)
            if current_state.check_win(current_state.mattrix):
                print("Path found by BFS:", current_path)
                return current_path
            for direction in ['up', 'down', 'left', 'right']:
                next_state = current_state.move1(current_state, direction)
                next_state_key = str(next_state.mattrix) 
                
                if next_state_key not in visited_states:
                    queue.append((next_state, current_path + [direction]))

        print("No Path found by BFS.")
        return None

    def dfs(self):
        initial_state = self.state_ins
        stack = [(initial_state, [])]
        visited_states = set()

        while stack:
            current_state, current_path = stack.pop() 
            state_key = str(current_state.mattrix)
            
            if state_key in visited_states:
                continue
            
            visited_states.add(state_key)
            
            if current_state.check_win(current_state.mattrix):
                print("Path found by DFS:", current_path)
                return current_path
            
            for direction in ['up', 'down', 'left', 'right']:
                next_state = current_state.move1(current_state, direction)
                next_state_key = str(next_state.mattrix)
                
                if next_state_key not in visited_states:
                    stack.append((next_state, current_path + [direction]))
                    plt.draw()

        print("No Path found by DFS.")
        return None

    #لحتى شغل ال DFS ببدل بالكومنتات
    def Bfs_Dfs_gor(self):
    # BFS
        bfs_path = self.bfs()
        if bfs_path:
            print("Playing BFS path...")
            for move in bfs_path:
                self.h_move(move)
                plt.pause(1.5)
            
        plt.pause(1) 
    
    # DFS
        # dfs_path = self.dfs()
        # if dfs_path:
        #     print("Playing DFS path...")
        #     for move in dfs_path:
        #         self.h_move(move)
        #         plt.pause(1.5)
        #     dfs_path = self.dfs()
        #     if dfs_path:
        #         print("Playing DFS path...")
        #         for move in dfs_path:
        #             self.h_move(move, is_bfs=False) 
        #             plt.pause(1.5)

def equalll(mattrix1, mattrix2):
    return mattrix1 == mattrix2
