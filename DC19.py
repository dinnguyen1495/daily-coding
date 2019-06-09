# Daily Coding 19
# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of
# minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with
# kth color, return the minimum cost which achieves this goal.

def minimum_cost_coloring(matrix):
    all_costs = [matrix[0]]
    for i in range(1, len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            temp.append(matrix[i][j] + min(all_costs[i - 1][:j] + all_costs[i - 1][j + 1:]))
        all_costs.append(temp)
    return min(all_costs[len(matrix) - 1])

def main():
    cost_matrix = \
        [[7, 3, 8, 6, 1, 2],
        [5, 6, 7, 2, 4, 3],
        [10, 1, 4, 9, 7, 6],
        [10, 1, 4, 9, 7, 6]]
    print("Cost matrix:",cost_matrix)
    print("Minimum Cost:", minimum_cost_coloring(cost_matrix))

if __name__ == "__main__":
    main()