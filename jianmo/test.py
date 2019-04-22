#测试算法,运行时间大于kmpAgr

def kmp_match(s, p):            #s母串
    m = len(s); n = len(p)
    cur = 0#起始指针cur
    table = partial_table(p)
    while cur<=m-n:
        for i in range(n):
            if s[i+cur]!=p[i]:
                cur += max(i - table[i-1], 1)#有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return cur
    return False
 
#部分匹配表
def partial_table(p):
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1,len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i+1] for j in range(1,i+1)}
        ret.append(len((prefix&postfix or {''}).pop()))
    return ret
# 测试
if __name__ == "__main__":
    print(partial_table("ABddCEABD"))
    print (kmp_match("BBCABCDABABCDABCDABDE", "ABCDABD"))

