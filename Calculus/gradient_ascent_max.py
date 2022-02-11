from sympy import Derivative, Symbol, sympify
from sympy.core.sympify import SympifyError
'''
단일 변수 함수에 대한 최대값을 계산하기 위해 그레디언트 상승을 사용한다.
'''


def grad_ascent(x0, flx, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*flx.subs({x:x_old}).evalf()

    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*flx.subs({x:x_old}).evalf()

    return x_new


if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable to differentiate with respect to: ')
    var0 = float(input('Enter the initial value of the variable: '))

    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit()
        var_max = grad_ascent(var0, d, var)
        print('{0}: {1}'.format(var.name, var_max))
        print('Maximum value: {0}'.format(f.subs({var:var_max})))