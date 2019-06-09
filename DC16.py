# Daily Coding 16
# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

# Circular List
class LogRecoder:
    def __init__(self, N):
        self.memory = [None] * N
        self.counter = 0
    
    def to_string(self):
        return str(self.memory)

    def record(self, order_id):
        self.memory[self.counter] = order_id
        self.counter += 1
        if self.counter == len(self.memory):
            self.counter = 0

    def get_last(self, i):
        if i >= len(self.memory) or i < -len(self.memory):
            return None
        return self.memory[-i]
    
    def get_i_last(self, i):
        return self.memory[-i:]

def main():
    log = LogRecoder(10)
    for i in range(1, 20, 2):
        log.record(i)
    print("Log:", log.to_string())
    print("3rd last element:", log.get_last(3))
    print("3 last elements:", log.get_i_last(3))
    for i in range(1, 11):
        log.record(i)
    print("Log:",log.to_string())
    print("5th last element:",log.get_last(5))
    print("5 last elements:", log.get_i_last(5))

if __name__ == "__main__":
    main()