#function d les x lol

def ft_filter(f_de_x, les_x):
    return [x for x in les_x if f_de_x(x)]

xx = [1, -2, -3, 4]
xr = ft_filter(lambda x: x < 0, xx)

#print(xr)