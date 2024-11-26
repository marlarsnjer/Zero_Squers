import time
import matplotlib.pyplot as plt
from collections import deque
from state import State
import copy
import heapq
class Play:
    def __init__(self, state_ins):
        self.state_ins = state_ins
        self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 6))
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

    # def dfs(self):
    #     initial_state = self.state_ins
    #     stack = [(initial_state, [])]
    #     visited_states = set()

    #     while stack:
    #         current_state, current_path = stack.pop() 
    #         state_key = str(current_state.mattrix)
            
    #         if state_key in visited_states:
    #             continue
            
    #         visited_states.add(state_key)
            
    #         if current_state.check_win(current_state.mattrix):
    #             print("Path found by DFS:", current_path)
    #             return current_path
            
    #         for direction in ['up', 'down', 'left', 'right']:
    #             next_state = current_state.move1(current_state, direction)
    #             next_state_key = str(next_state.mattrix)
                
    #             if next_state_key not in visited_states:
    #                 stack.append((next_state, current_path + [direction]))
    #                 plt.draw()

    #     print("No Path found by DFS.")
    #     return None

    def recursive_dfs(self, current_state=None, current_path=None, visited_states=None):
        if current_state is None:
            current_state = self.state_ins
            current_path = []
            visited_states = set()

        state_key = str(current_state.mattrix)
        if state_key in visited_states:
            return None
        visited_states.add(state_key)
        if current_state.check_win(current_state.mattrix):
            print("Path found by Recursive DFS:", current_path)
            return current_path
        
        for direction in ['up', 'down', 'left', 'right']:
            next_state = current_state.move1(current_state, direction)
            next_state_key = str(next_state.mattrix)
            if next_state_key not in visited_states:
                result = self.recursive_dfs(next_state, current_path + [direction], visited_states)
                if result: 
                    return result
                return None

    

    def ucs(self):
        initial_state = self.state_ins
        pq = []  
        heapq.heappush(pq, (0, str(initial_state.mattrix), []))  
        visited_states = set() 

        while pq:
            current_cost, state_key, current_path = heapq.heappop(pq)
            if state_key in visited_states:
                continue

            visited_states.add(state_key)
            current_state = State.from_key(state_key)

            if current_state.check_win(current_state.mattrix):
                print("Path found by UCS:", current_path)
                return current_path

            for direction in ['up', 'down', 'left', 'right']:
                next_state = current_state.move1(current_state, direction)
                next_state_key = str(next_state.mattrix)
                movement_cost = 1 
                new_cost = current_cost + movement_cost

                if next_state_key not in visited_states:
                    heapq.heappush(pq, (new_cost, next_state_key, current_path + [direction]))

        print("No Path found by UCS.")
        return None



    #لحتى شغل ال DFS ببدل بالكومنتات
    def Bfs_Dfs_gor(self):
    # BFS
        # bfs_path = self.bfs()
        # if bfs_path:
        #     print("Playing BFS path...")
        #     for move in bfs_path:
        #         self.h_move(move)
        #         plt.pause(1.5)
            
        # plt.pause(1) 
    
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
    #UCS
        # ucs_path = self.ucs()
        # if ucs_path:
        #         print("Playing UCS path...")
        #         for move in ucs_path:
        #             self.h_move(move)
        #             plt.pause(1.5)

        # plt.pause(1)

        recursive_dfs_path = self.recursive_dfs()
        if recursive_dfs_path:
                print("Playing recursive dfs path...")
                for move in recursive_dfs_path:
                    self.h_move(move)
                    plt.pause(1.5)

        plt.pause(1)


    

def equalll(mattrix1, mattrix2):
    return mattrix1 == mattrix2
