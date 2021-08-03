def convert(num:str, option:int = 1) -> str:
    """
    option 1: more than 0
    option 2:
    """
    nums_0_19 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight',"Nine",'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    nums_20_90 = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    nums_dict = {100: 'hundred',1_000:'thousand', 1_000_000:'million', 1_000_000_000:'billion'}

    def minus(num:str, minus_flag:bool = False):
        if minus_flag != True:
            return num
        return "Minus " + num


    if option == 1:
        num:int = int(num)
        minus_flag:bool = False
        if num < 0:
            minus_flag = True
            num *= -1

        if num < 20:
            return minus(nums_0_19[num], minus_flag)

        elif num < 100:
            return minus(nums_20_90[num // 10 - 2 ]  + " " + nums_0_19[num % 10], minus_flag)

        max_key:int = max([key for key in nums_dict.keys() if key <= num])


        return convert(num // max_key, 1) + ' ' + nums_dict[max_key] + ('' if num % max_key == 0 else ' ' + convert(num % max_key))


    elif option == 2:
        ans = ""
        for i in num:
            ans += nums_0_19[int(i)] + " "
        return ans #space 多い
    else:
        print("usage error")
        exit(-1)


def erorr():
    print("usage error")
    exit(-1)

def main():
    #入力
    num:str = input()

    #例外処理
    if num[0] == "0" and num[1] != ".":
        error()
    try:
        _ = float(num)
    except:
        erorr()


    num:list = num.split('.')
    #小数ではない場合
    if len(num) == 1:
        ans:str = convert(int(num[0]), 1)
        print(ans)

    elif len(num) == 2:
        ans1:str = convert(num[0], 1)
        ans2:str = convert(num[1], 2)

        print(ans1 + " point " + ans2)


    else:
        print("usage error")

if __name__ == '__main__':
    main()
