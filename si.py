import sys
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = int(sys.argv[1])
    r = int(sys.argv[2])
    t = int(sys.argv[3])

    si = simple_interest(p, r, t)
    print("Simple Interest:", si)