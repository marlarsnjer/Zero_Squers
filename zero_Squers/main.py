from state import State
from play import Play
import matplotlib.pyplot as plt
#ثبتت اكتر من رقعة من مستويات مختلفة
#Easy
# mattrix=[
#     [0, 0, 0, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 'M', 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 'R', 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1]
# ]
#Medium
# mattrix = [
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
mattrix=[
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
# mattrix = [
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
# mattrix = [
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
# mattrix = [
#     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 'O', 1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 0, 'A', 0, 'L', 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 'M', 0, 'B', 0, 1, 1],
#     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# ]

state_ins = State(mattrix)
play_instance = Play(state_ins)

plt.show()



