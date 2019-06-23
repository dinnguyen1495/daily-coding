# Daily Coding 41
# Given an unordered list of flights taken by someone, each represented as (origin, destination)
# pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return
# null. If there are multiple possible itineraries, return the lexicographically smallest one. All
# flights must be used in the itinerary.
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO',
# 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should
# return null.
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport
# 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is
# also a valid itinerary. However, the first one is lexicographically smaller.

def get_neighbours(flights, start):
    neighbours = []
    for flight in flights:
        if flight[0] == start:
            neighbours.append(flight[1])
    return sorted(neighbours)

def itinerary(flights, start):
    def helper(flights, start):
        neighbours = get_neighbours(flights, start)
        if len(flights) == 0:
            return [start]
        for neighbour in neighbours:
            new_flights = [x for x in flights if x != (start, neighbour)]
            result = [start] + helper(new_flights, neighbour)
            if len(result) - 1 == len(flights):
                return result
        return []
    result = helper(flights, start)
    return result if result else None

def main():
    print(itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))
    print(itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
    print(itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))

if __name__ == '__main__':
    main()