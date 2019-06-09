# Daily Coding 12
# There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function 
# that returns the number of unique ways you can climb the staircase. The order of the steps matters. 

def number_of_unique_ways(n, list):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - elem] for elem in list if i - elem >= 0)
    return cache[n]

def main():
    print(number_of_unique_ways(10, [1, 3, 5]))

if __name__ == "__main__":
    main()