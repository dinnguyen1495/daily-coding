# Daily Coding 30
# You are given an array of non-negative integers that represents a two-dimensional
# elevation map where each element is unit-width wall and the integer is the height.
# Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1)
# space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in
# the second, and 3 in the fourth index (we cannot hold 5 since it would run off
# to the left), so we can trap 8 units of water.

def trapped_water(walls):
    N = len(walls)
    first, last, result = 0, N - 1, 0
    for i, j in zip(range(1, N), range(N - 2, -1, -1)):
        if walls[i] >= walls[first]:
            if i - first > 1:
                result += (i - first - 1) * min(walls[i], walls[first]) - sum(walls[first + 1 : i])
            first = i
        if walls[j] > walls[last]:
            if last - j > 1:
                result += (last - j - 1) * min(walls[j], walls[last]) - sum(walls[j + 1 : last])
            last = j
    return result

def main():
    def testing(walls):
        print("Number of trapped water units with input", walls, ":", trapped_water(walls))
        walls.reverse()
        print("Number of trapped water units with input", walls, ":", trapped_water(walls))
    testing([3, 0, 1, 3, 0, 5])
    testing([3, 0, 1, 5, 0, 3])
    testing([1, 0])
    testing([2, 1, 2])
    testing([1, 3, 1, 3])

if __name__ == "__main__":
    main()