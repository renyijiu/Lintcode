'''
单例 是最为最常见的设计模式之一。对于任何时刻，如果某个类只存在且最多存在一个具体的实例，那么我们称这种设计模式为单例。例如，对于 class Mouse (不是动物的mouse哦)，我们应将其设计为 singleton 模式。
你的任务是设计一个 getInstance 方法，对于给定的类，每次调用 getInstance 时，都可得到同一个实例。

思路：这道题其实并不是很难，主要是传达一种思想。当有实例已经在运行时，返回实例；若没有则创建一个实例并返回，只允许单个实例在运行。
'''


class Solution:
    # @return: The same instance of this class every time
    obj = None
    @classmethod
    def getInstance(cls):
        # write your code here
        if not Solution.obj:
            Solution.obj = cls()
        return Solution.obj
