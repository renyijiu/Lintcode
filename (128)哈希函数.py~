'''
在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数，比如：
hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE 
                              = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
                              = 3595978 % HASH_SIZE
其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。
给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。

思路：这道题目其实并不难，但是就是需要一点方法优化，若如果直接按照题目的公式进行计算，当字符串很长时，会直接超时；所以需要在计算时用数学进行优化,从小值进行取模减小计算量，加快循环速度。
'''


class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        num = 0
        w = 1
        for i in xrange(len(key)-1, -1, -1):
            num =(num + (ord(key[i])*w)) % HASH_SIZE
            w = (w * 33) % HASH_SIZE
        return num
        
#超时代码
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        num = 0
        if key == "":
            return False
        else:
            for i in range(0, len(key)):
                num += ord(key[i]) * (33**(len(key)-1-i))
            return (num % HASH_SIZE)     
