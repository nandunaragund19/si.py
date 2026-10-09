def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = int(input("Enter principal amount: "))
    r = int(input("Enter annual interest rate: "))
    t = int(input("Enter time in years: "))

    si = simple_interest(p, r, t)
    print("Simple Interest:", si)