"""import numpy as np
import random

def main():
    total_time = 1000
    n_metronome = 100
    T = 5
    eps = 1

    state = [0] * n_metronome

    random.seed(2021)
    for i in range(n_firefly):
        each_state = random.randint(-1 * T + eps,T-eps)
        state[i]  = each_state


    model_metronome =  Metronomes(T = T ,eps = eps ,state = state)

    for t in range(total_time):
        model_metronome()
        if t % 10:
            print(model_metronome.state)

def rand_ints_nodup(a, b, k):
     ns = []
     while len(ns) < k:
         n = random.randint(a, b)
         if not n in ns:
             ns.append(n)
         return ns


class Metronomes():
    def __init__(self,T,eps,state:list,network:list):

        self.T = T
        self.eps = eps
        self.state = np.array(state)

    def __call__(self):
        for s in enumerate(self.state):

        self.state += self.eps
        self.synchro()

    def checker(self):
        state_full_flies = []
        for i,s in enumerate(self.state):
            if s == self.T:
                state_full_flies.append(i)

        for idx in state_full_flies:
            self.state[idx] = 0
            self.synchro(idx)

    def synchro(self,idx):
        from_n_move =  self.n_move[idx]
        state_sign = 0
        for i in self.network[idx]:
            to_n_move = self.n_move[i]
            if from_n_move > to_n_move:#早い
                state_sign += -1
            elif from_n_move < to_n_move:
                state_sign += 1

        self.state[idx] += np.sign(state_sign) * self.eps



if __name__ == '__main__':
    main()
    """
