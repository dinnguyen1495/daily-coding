# Daily Coding 10
# Implement a job scheduler which takes in a function f and an integer n, and
# calls f after n milliseconds.

import logging
import time

def f():
    print("Hello World")

def task_scheduler(f, n=0):
    while True:
        time.sleep(n/1000)
        f()

def main():
    task_scheduler(f, 1000)

if __name__ == "__main__":
    main()