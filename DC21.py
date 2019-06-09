# Daily Coding 21
# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the
# minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def classrooms_arrange(scheduler):
    if len(scheduler) == 0:
        return 0
    sorted_scheduler = sorted(scheduler, key = lambda x: x[0])
    print("Scheduler (sorted):",sorted_scheduler)
    used_rooms = 1
    unfinished_lectures = [sorted_scheduler[0][1]]
    if len(scheduler) == 1:
        return used_rooms
    for i in range(1, len(scheduler)):
        count = 0
        for end in unfinished_lectures:
            if sorted_scheduler[i][0] < end:
                count += 1
            else:
                unfinished_lectures.remove(end)
        if count == len(unfinished_lectures) and count != 0:
            used_rooms += 1
        unfinished_lectures.append(sorted_scheduler[i][1])
    return used_rooms

def main():
    scheduler = [(0, 50), (60, 150), (140, 180), (120, 190)]
    print("Scheduler:", scheduler)
    print("Number of needed rooms:", classrooms_arrange(scheduler))

if __name__ == "__main__":
    main()