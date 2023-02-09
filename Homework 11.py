# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
import mathlotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30
limit = 10
step = 0.01
step_acr = 0.0000001
line_stily ='--'
color = 'b'
direct_up = True

def switch_line():
    global line_stily
    if line_stily =='-':
        line_stily = '--'
    else:
        line_stily = '-'
    return line_stily    

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


def func(x):
    f = a*x**4*np.sin(np.cos(x))+ b*x**3 + c*x**2 + d*x + e
    return f

x = np.arange(-limit,limit + step, step)


x_change = [(-limit, 'limit')]

for i in range(len(x) - 1):
    if func(x[i])> 0 and func(x[i+1])< 0 or func(x[i])< 0 and func(x[i+1])> 0:
        x_acr = np.arange(x[i], x[i+1] + step_acr, step_acr)
        for j in range(len(x_acr) - 1):
            if func(x_acr[j])> 0 and func(x_acr[j+1])< 0 or func(x_acr[j])< 0 and func(x_acr[j+1])> 0:
                x_change.append((x_acr[i], 'zero'))
    if direct_up:
        if func(x[i])> func(x[i+1]):
            direct_up = False
            x_change.append((x[i], 'dir'))
    else:
        if func(x[i]) < func(x[i+1]):
            direct_up = True
            x_change.append((x[i], 'dir'))   
       
x_change.append((limit, 'limit'))


for i in range(len(x_change) - 1):
    cur_x = np.arrange(x_change[i][0], x_change[i+1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], func(x_change[i][0]), 'go')
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())