import numpy as np
import random

def main():
    total_time = 1000
    n_firefly = 20
    T = 10
    eps = 1
    #stateとnetworkの作成
    state = [0] * n_firefly
    network = [0] * n_firefly
    max_edge_num = 5

    random.seed(2021)
    for i in range(n_firefly):
        each_state = random.randint(0,T-eps)
        state[i]  = each_state

        edge_num = random.randint(1,max_edge_num)
        network[i] = rand_ints_nodup(0,n_firefly-1, edge_num)



def rand_ints_nodup(a, b, k):
     ns = []
     while len(ns) < k:
         n = random.randint(a, b)
         if not n in ns:
             ns.append(n)
         return ns


class FireFlies():
    def __init__(self,T,eps,state:list,network:list):
        """
        :param:
        T:周期
        eps:待ち時間
        state: 最初の周期の状態
        network:
        """
        self.T = T
        self.eps = eps
        self.state = np.array(state)
        self.n_move:list = np.array([0] * len(state))


    def run(self):
        state += self.eps
        self.checker()

    def checker(self):
        state_full_flies = []
        for i,s in enumerate(self.state):
            if s == 1:
                self.n_move[i] += 1
                state_full_flies.append(i)

        for idx in state_full_flies:
            self.state[idx] = 0
            self.synchro(idx)

    def synchro(self,idx):
        each_n_move =  self.n_move
        for i in self.network[idx]:




if '__name__'== main:
    main()
