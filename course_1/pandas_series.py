import pandas as pd

### Custom index
s1 = pd.Series([1, 2, 3, 4], index=['foo','bar','foobar','barfoo'])
s2 = pd.Series([5, 6, 7, 8], index=['bar','foobar','barfoo','foofoo'])

### When addition, it will be added per index "string"
s = s1+s2

print(s)

