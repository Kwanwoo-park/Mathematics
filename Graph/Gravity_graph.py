import matplotlib.pyplot as plt
from pylab import savefig
'''
두 물체 간 거리와 인장력 간 관계
'''


#그래프 그리기
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational forces ans distance')
    savefig('Gravity.png')
    plt.show()


def generate_F_r():
    r = range(100, 1001, 50)
    F = []

    G = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5

    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)

    draw_graph(r, F)


if __name__ == '__main__':
    generate_F_r()
