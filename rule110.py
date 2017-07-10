def run_rules(x):
    next_x = np.zeros(len(x))
    for i in range(len(x)):
        if i == 0:
            current_pattern = [x[-1]] + list(x[:2])
        elif i == len(x)-1:
            current_pattern = list(x[-2:]) + [x[0]]
        else:
            current_pattern = list(x[i-1:i+2])
        #if current_pattern == [0, 1, 1]:
        #    current_pattern = [0, 1, 0]
        if current_pattern in [[1, 1, 1], [1, 0, 0], [0, 0, 0]]:
            next_cell = 0
        else:
            next_cell = 1
        next_x[i] = next_cell
        
    return next_x

x = np.zeros(50)
x[25]=1

for i in range(100):
    print(x)
    x = run_rules(x)
