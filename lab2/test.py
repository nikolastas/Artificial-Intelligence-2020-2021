import pandas as pd 
import os

ans ={ }


print(ans)

query=['nikos', 'natalie', 'natalie']

def prolog_queries(query, ans, s) :
    for sol in query:
        m= sol
        if m not in s:
            s.add(m)
            ans[m]=1
        else:
            tmp = ans[m]
            del ans[m]
            ans[m]=tmp+1
    return ans
s = set()
ans = prolog_queries(query, ans, s)


ans=sorted(ans.items(), key=lambda x: x[1], reverse=True)
print(ans)
print(s)