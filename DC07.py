# Daily Coding 7
# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it # can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.
# Time: 1h, need a revision

def decode(number):
    return number >= 1 and number <= 26

def scrumble_string(len):
    if len == 0:
        return []
    if len == 1:
        return [[1]]
    if len == 2:
        return [[1, 1], [2]]
    list_of_lists = []
    for i in range(1, 3):
        if len >= i:
            for elem in scrumble_string(len - i):
                list_of_lists.append([i] + elem)
    return list_of_lists

def number_of_decodes(number):
    string = str(number)
    counter = 0
    list_of_decodes = []
    possible_scrumbles = scrumble_string(len(string))
    for way in possible_scrumbles:
        index = 0
        count = 0
        for move in way:
            temp = int(string[index:index + move])
            if decode(temp):
                count += move
                index += move
                continue
            else:
                break
        if count == len(string):
            counter += 1
        else:
            continue
    return counter

def main():
    print("Number of decode ways for", 1111 ,":", number_of_decodes(1111))
    print("Number of decode ways for", 2627 ,":", number_of_decodes(2627))

if __name__ == "__main__":
    main()