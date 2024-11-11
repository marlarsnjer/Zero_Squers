import matplotlib.pyplot as plt
from state import State

class Play:
    def __init__(self, state_ins):
        self.state_ins = state_ins
        self.fig, self.ax = plt.subplots(5, 1, figsize=(2, 20))#جزئت الواجهة لارع محاور ليمثل الحالة الحلية يلي عم بلعب فيها و الاربع حالات المتوقعة
        self.fig.canvas.mpl_connect('key_press_event', self.press)#ربطت حدث الضغط على ازرار الحركة
        self.state_ins.print(self.state_ins.mattrix, self.ax[0])
        self.pre_mattrix = None  
        self.last_dir = None 

    def press(self, event):
        if event.key == 'up':
            self.h_move('up')
        elif event.key == 'right':
            self.h_move('right')
        elif event.key == 'down':
            self.h_move('down')
        elif event.key == 'left':
            self.h_move('left')
        self.next_state()

    def next_state(self):
        dir = ['right',
                    'left', 
                    'up', 
                    'down']
        s_obj = []
        for idx, dir in enumerate(dir, start=1):
            n_state = self.state_ins.move1(self.state_ins, dir)
            s_obj.append(n_state)
            n_state.print(n_state.mattrix, self.ax[idx])
        plt.draw()
        return s_obj

    
    def h_move(self, dir):
        self.pre_mattrix = [row[:] for row in self.state_ins.mattrix]#نسخت المصفوفة القديمة سطر سطر لحتى قارنها لما اتحرك بتابع التساوي يلي تحت
        n_state_ins = self.state_ins.move1(self.state_ins, dir)
        
        for row in n_state_ins.mattrix:
            print(row)
        print(f"mattrix after moved to {dir}")
        
        if self.last_dir == dir and equalll(self.pre_mattrix, n_state_ins.mattrix):
            print(f"You moved {dir} twice without changing the state!")
        
        self.state_ins = n_state_ins
        self.last_dir = dir  
        self.state_ins.print(self.state_ins.mattrix, self.ax[0])
        plt.draw()

def equalll(mattrix1, mattrix2):
    return mattrix1 == mattrix2
