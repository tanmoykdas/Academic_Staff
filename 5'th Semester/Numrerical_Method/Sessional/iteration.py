def iteration_method(x0, itrr):
    for i in range(itrr):
        x1 = f(x0)
        if abs(x1 - x0) < 0.0001:
            return x1
        x0 = x1
    return x1

x0 = float(input("initial guess: "))
itr = int(input("give max_iteration: "))

f = lambda x : 0.5*x**2 + 0.25
root = iteration_method(x0, itr)
print("root:", root)

# intial guess: 1
# max_iteration: 10