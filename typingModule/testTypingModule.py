from typing import List, Dict , Tuple , Optional, Union, Callable, Iterator

#基本的な使い方
a: List[int] = [1,2]
b: Dict[str,int] = ["a", 1]
#Noneの許容
x: Optional[str] = None
# 2つのいずれかの型を許容する場合
x: Union[int, str] = 2



# 基本的な関数の引数、返り値への型ヒント
def f(num1: int, num2: float) -> float:
    return num1 + num2
# 関数型の場合
x: Callable[[int, float], float] = f

def g(n:int) -> Iterator:
    for i in range(n):
        yield i
     
