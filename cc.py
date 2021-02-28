Gs = 1.1
Gc = 0.07

def get_principal_growth(i, Cs):
    return Cs * pow(Gs, i)

def get_compound_growth(now_n, total_n, Cs):
    total_cash = 0
    for n in range(now_n-now_n, total_n-now_n):
        total_cash += Cs * Gc * pow(Gs, n)
    return total_cash

#def acc():


def main():
    N = 3
    total = 0
    cost = 0
    for i in range(N):
        Cs = 4.3*1
        cost += Cs/Gc
        principal_growth = get_principal_growth(i, Cs)
        compound_growth = get_compound_growth(i, N, Cs)
        sum_growth = principal_growth+compound_growth
        total += sum_growth
        invest_rate = pow(1+(total/cost), 1/i) if i != 0 else 0
        print(f'the profit in {i}st year stock, we can get: {round(principal_growth, 2)} + {round(compound_growth, 2)} = {round(sum_growth, 2)}, total={round(total, 2)}, cost={round(cost, 2)}, invest_rate={round(invest_rate, 2)}')

if __name__ == '__main__':
    main()