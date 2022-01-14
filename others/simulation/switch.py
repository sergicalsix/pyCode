from icecream import ic  # 変数表示用ライブラリ
from typing import List
import sympy
import copy
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def eq1(k1, k2, k3, k4, s0, g) -> float:
    return k1*s0 - k2*g + k3*g**2 / (k4**2 + g**2)


def simulation(k1, k2, k3, k4, s0, g0, delta_time, iteration, comment='sim1') -> List[float]:
    # パラメータ条件の表示
    ic(k1, k2, k3, k4, s0, g0, delta_time, iteration, comment)

    g = g0
    g_list = [0] * iteration
    for i in range(iteration):
        delta_g = eq1(k1, k2, k3, k4, s0, g)
        g += delta_g * delta_time
        if g < 0:
            g = 0
        g_list[i] = g
    return g_list


def plot_simulation(time_list, value_list, fig_name='sim1') -> None:
    plt.scatter(time_list, value_list)
    plt.xlabel('time')
    plt.ylabel('g')
    plt.savefig(fig_name + '.pdf')
    plt.close()


def multi_simulation(k1, k2, k3, k4, s0, g0, delta_time, iteration, comment='multi_sim1') -> List[List[float]]:
    """
    k1,k2,k3,k4,s0,g0の6つのパラメータのうち、リスト形式で入力されたものを検出して全ての場合でシミュレーションを行う。
    今回複雑度の観点から、リスト型で取得できるパラメータを1種類までと限定する(2種類以上のリスト型のパラメータが入力された場合はエラー)
    """
    param_list = [k1, k2, k3, k4, s0, g0]
    # 実際にシミュレーションで参照するパラメータリスト: sim_param_list
    sim_param_list = copy.deepcopy(param_list)
    for i, params in enumerate(param_list):
        if type(params) == list:
            list_index = i
            break
    g_multi_list = [None] * len(params)
    # シミュレーション
    for i, param in enumerate(params):
        sim_param_list[list_index] = param
        g_multi_list[i] = simulation(
            *sim_param_list, delta_time, iteration, comment=comment + '_' + str(param))
        ic(g_multi_list[i][-1])

        #plot_simulation(time_list,g_list,fig_name = 'sim1_hoge')
    return g_multi_list


def plot_multi_simulation(time_list, value_multi_list, param_list, param_label='g0', fig_name='multi_sim1') -> None:
    for param, value_list in zip(param_list, value_multi_list):
        plt.scatter(time_list, value_list,
                    label=param_label + '=' + str(param))
    plt.xlabel('time')
    plt.ylabel('g')
    if param_label != "all":
        plt.legend()
    plt.savefig(fig_name + '.pdf')
    plt.close()


def all_simulation(k1_list, k2_list, k3_list, k4_list, s0_list, g0_list, delta_time, iteration, comment='all_sim1') -> List[List[float]]:
    """
    k1,k2,k3,k4,s0,g0の6つのパラメータを全てリストとして入力し、全通り試す
    """
    param_list = [k1_list, k2_list, k3_list, k4_list, s0_list, g0_list]
    g_multi_list = [None] * 16
    # シミュレーション
    for i, param in enumerate(params):
        sim_param_list[list_index] = param
        g_multi_list[i] = simulation(
            *sim_param_list, delta_time, iteration, comment=comment + '_' + str(param))
        ic(g_multi_list[i][-1])

        #plot_simulation(time_list,g_list,fig_name = 'sim1_hoge')
    return g_multi_list


def plot_curve(g_list, dgdt_list, fig_name='curve1') -> None:
    plt.scatter(g_list, dgdt_list)
    plt.xlabel('g')
    plt.ylabel('dg/dt')
    plt.savefig(fig_name + '.pdf')
    plt.close()


def solve_eq(k1, k2, k3, k4, s0) -> None:
    sympy.var('k1,k2,k3,k4,s0,g')
    solve = sympy.solve(k1*s0 - k2*g + k3*g**2 / (k4**2 + g**2), g)
    sympy.init_printing()
    ic(solve)
    print("(gの解の個数)=", sum(1 if v >= 0 else 0 for v in solve))


def main():
    # パラメータの設定(論文の値)
    k1, k2, k3, k4 = 1, 0.4, 1, 1
    # 初期条件の設定
    s0, g0 = 0, 1
    # dg/dt = 0の時の曲線 <- 論文の曲線と値を合わせるため
    g_list = [i * 0.01 for i in range(250)]
    dgdt_list = [eq1(k1, k2, k3, k4, s0, g) for g in g_list]
    plot_curve(g_list, dgdt_list)
    # 解の個数を出力
    solve_eq(k1, k2, k3, k4, s0)

    # シミュレーションの条件の設定
    delta_time, total_time = 0.01, 10
    iteration = round(total_time / delta_time)
    time_list = [i * delta_time for i in range(iteration)]

    # 単一シミュレーション
    g_list = simulation(k1, k2, k3, k4, s0, g0, delta_time,
                        iteration, comment='sim1')
    plot_simulation(time_list, g_list, fig_name='sim1')

    # gの初期値を変更してシミュレーション
    g0_list = [1, 5, 10, 20]
    g_multi_list = multi_simulation(
        k1, k2, k3, k4, s0, g0_list, delta_time, iteration, comment='multi_sim_g0')
    plot_multi_simulation(time_list, g_multi_list, g0_list,
                          param_label='g0', fig_name='multi_sim_g0')

    # k1を変更してシミュレーション
    k1_list = [1, 5, 10, 20]
    g_multi_list = multi_simulation(
        k1_list, k2, k3, k4, s0, g0, delta_time, iteration, comment='multi_sim_k1')
    plot_multi_simulation(time_list, g_multi_list, k1_list,
                          param_label='k1', fig_name='multi_sim_k1')

    # k2を変更してシミュレーション
    k2_list = [1, 5, 10, 20]
    g_multi_list = multi_simulation(
        k1, k2_list, k3, k4, s0, g0, delta_time, iteration, comment='multi_sim_k2')
    plot_multi_simulation(time_list, g_multi_list, k2_list,
                          param_label='k2', fig_name='multi_sim_k2')

    # k3を変更してシミュレーション
    k3_list = [1, 5, 10, 20]
    g_multi_list = multi_simulation(
        k1, k2, k3_list, k4, s0, g0, delta_time, iteration, comment='multi_sim_k3')
    plot_multi_simulation(time_list, g_multi_list, k3_list,
                          param_label='k3', fig_name='multi_sim_k3')

    # k4を変更してシミュレーション
    k4_list = [1, 5, 10, 20]
    g_multi_list = multi_simulation(
        k1, k2, k3, k4_list, s0, g0, delta_time, iteration, comment='multi_sim_k4')
    plot_multi_simulation(time_list, g_multi_list, k4_list,
                          param_label='k4', fig_name='multi_sim_k4')

    # 全パラメータをバラバラに動かして検証
    """
    k1_list,k2_list,k3_list,k4_list,g0_list = [1,5],[1,5],[1,5],[1,5],[1,5]
    g_all_list = all_simulation(k1_list,k2_list,k3_list,k4_list,list(s0),g0_list,delta_time,iteration,comment = 'multi_sim_all')
    plot_multi_simulation(time_list,g_all_list,[i in range(32)],param_label = 'all' ,fig_name = 'multi_sim_all')
    """


if __name__ == '__main__':
    main()
