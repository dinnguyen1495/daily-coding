# Daily Coding 5:
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element 
# of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    return f(lambda x, y: x)    

def cdr(f):
    return f(lambda x, y: y)

def main():
    print("First: " + str(car(cons("a", "b"))) + "\nLast: " + str(cdr(cons("a", "b"))))

if __name__ == "__main__":
    main()