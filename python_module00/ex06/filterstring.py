# since we already imlimented our ft_filter we will use it to solve this exercise itself 

from ft_filter import ft_filter
import sys

if len(sys.argv) == 3:
    str  = sys.argv[1]
    num = sys.argv[2]

    try:
        num = int(num)
    except:
        raise AssertionError("not int")
    result = ft_filter(lambda w: len(w) > num, str.split())
    print(result)
else:
    print("bad args")