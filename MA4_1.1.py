import random
import matplotlib.pyplot as plt
import math

def approximate_pi(n):
    nc = 0

    x_in_c = []
    y_in_c = []
    x_not_in_c = []
    y_not_in_c = []

    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1: # Check if inside circle
            nc += 1
            x_in_c.append(x)
            y_in_c.append(y)
        else: 
            x_not_in_c.append(x)
            y_not_in_c.append(y)

    print("\n----------------------")
    print(f"Number of points: {n}")
    print(f"Number of points in circle: {nc}")
    print(f"Approximation of pi: {4*nc/n}")
    print(f"math.pi: {math.pi}")
    print("----------------------")

    # Do the plotting
    fig = plt.figure()
    axs = fig.gca()
    plt.scatter(x_in_c, y_in_c, c="r")
    plt.scatter(x_not_in_c, y_not_in_c, c="b")
    axs.set_aspect('equal', 'box')
    plt.savefig(f'MA4_1.1_files/pi_approx_{n}.png')

def main():
    for n in [1000, 10000, 100000]:
        approximate_pi(n)

if __name__ == "__main__":
    main()

# ----------------------
# Number of points: 1000
# Number of points in circle: 785
# Approximation of pi: 3.14
# math.pi: 3.141592653589793
# ----------------------

# ----------------------
# Number of points: 10000
# Number of points in circle: 7767
# Approximation of pi: 3.1068
# math.pi: 3.141592653589793
# ----------------------

# ----------------------
# Number of points: 100000
# Number of points in circle: 78638
# Approximation of pi: 3.14552
# math.pi: 3.141592653589793
# ----------------------