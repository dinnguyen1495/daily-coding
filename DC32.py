# Daily Coding 32
# Suppose you are given a table of currency exchange rates, represented as a 2D
# array. Determine whether there is a possible arbitrage: that is, whether there
# is some sequence of trades you can make, starting with some amount A of any
# currency, so that you can end up with some amount greater than A of that
# currency.
# There are no transaction costs and you can trade fractional quantities.
# Idea: Bellman-Ford Algorithm + negative logarithm costs

from math import log

def arbitrage_possible(exchange_rate_table):
    neg_log_table = [[-log(y) for y in x] for x in exchange_rate_table]
    n = len(neg_log_table)

    source = 0
    dist = [float('inf')] * n
    dist[source] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if dist[u] + neg_log_table[u][v] < dist[v]:
                    dist[v] = dist[u] + neg_log_table[u][v]
    
    for u in range(n):
        for v in range(n):
            if dist[u] + neg_log_table[u][v] < dist[v]:
                return True
    
    return False

def main():
    print(arbitrage_possible([[1, 2], [2, 1]]))
    print(arbitrage_possible([[1, 1], [1, 1]]))

if __name__ == "__main__":
    main()