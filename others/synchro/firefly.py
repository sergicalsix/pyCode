import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt




def main():
    total_time = 1000
    n_firefly = 10
    T = 10
    eps = 1
    #stateとnetworkの作成
    state = [0] * n_firefly
    network = [0] * n_firefly
    max_edge_num = 10

    G = nx.DiGraph()  # 有向グラフ (Directed Graph)
    random.seed(2021)
    for i in range(n_firefly):
        each_state = random.randint(0,T-eps)
        state[i]  = each_state

        #network[i] = [(i+1)% n_firefly, (i+2)% n_firefly , (i+3)% n_firefly]

        #ランダムにエッジをはる ->　全ノードが結合されていないとうまくいかない
        edge_num = random.randint(8,max_edge_num)
        network[i] = rand_ints_nodup(0,n_firefly-1, edge_num)
        for j in network[i]:
            G.add_edge(i,j)
    nx.draw_networkx(G)
    #plt.show()
    plt.savefig('random_network.pdf')
    plt.close()

    model_firefly =  FireFlies(T = T ,eps = eps ,state = state ,network = network)

    for t in range(total_time):
        model_firefly()
        if t % 10:
            print(model_firefly.state)

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
        self.network = network

        self.n_move:list = np.array([0] * len(state))


    def __call__(self):
        self.state += self.eps
        self.checker()

    def checker(self):
        state_full_flies = []
        for i,s in enumerate(self.state):
            if s == self.T:
                self.n_move[i] += 1
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
