from state import State
from play import Play
import matplotlib.pyplot as plt
import time
def get_levels():
    levels = {
        "Easy": [
            [0, 0, 0, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 'M', 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 'R', 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ],
        "Medium": [
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 'M', 0, 0, 0, 'B', 'A', 1, 1],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        ],
        "hard": [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 'L', 1, 'M', 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 'O', 'R', 'B', 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 1],
            [0, 1, 0, 'A', 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1],
        ],
    }
    return levels

def run_game(level_name, mattrix):
    print(f"Running level: {level_name}")
    state_ins = State(mattrix)
    play_instance = Play(state_ins)
    
    
    plt.ion() #لتشغيل ال DFS لازم بدل بالكومنتات
    # print("\nRunning BFS...")
    # bfs_path = play_instance.bfs()
    # if bfs_path:
    #     print("BFS Solution Path:", bfs_path)
    #     for move in bfs_path:
    #         play_instance.h_move(move)
    #         plt.pause(1.5) 

    # time.sleep(2)
    print("\nRunning DFS...")
    dfs_path = play_instance.dfs()
    if dfs_path:
        print("DFS Solution Path:", dfs_path)
        for move in dfs_path:
            play_instance.h_move(move)
            plt.pause(1.5) 

    plt.ioff()  
    plt.close()


if __name__ == "__main__":
    levels = get_levels()
    for level_name, mattrix in levels.items():
        run_game(level_name, mattrix)
        time.sleep(3) 
        plt.close()