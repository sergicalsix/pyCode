"""
GとSの関係をプロットするための
"""
from icecream import ic  # 変数表示用ライブラリ
import sympy
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def main():
    k1, k2, k3, k4 = 1, 1, 1, 0.4
    # 初期条件の設定
    delta = 0.001
    fig_name = "g_s"
    s_list = [i * delta for i in range(30)]
    s_list.extend([i * delta * 0.1 + 0.03 for i in range(200)])
    s_list.extend([i * delta + 0.05 for i in range(50)])

    #s_list = [0.02]
    for s_ in s_list:
        sympy.var('k1,k2,k3,k4,s,g')
        solve = sympy.solve(k1*s_ - k4*g + k2*g**2 / (k3**2 + g**2), g)
        sympy.init_printing()
        for sol in solve:
            # sympy のバグ対応
            if 1e-20 > sympy.Abs(sympy.im(sol)):
                sol = sympy.re(sol)
            try:
                if sol > 0:
                    plt.scatter(sol, s_, color='black')
            except:
                pass

    plt.xlabel('g')
    plt.ylabel('s')
    plt.savefig(fig_name + '.pdf')
    plt.close()


if __name__ == '__main__':
    main()
