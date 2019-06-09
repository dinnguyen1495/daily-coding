# Daily Coding 13:
# Given an integer k and a string s, find the length of the longest substring that contains at most k 
# distinct characters
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"

def number_of_distinct_characters(s):
    return len(set(s[0:len(s)]))

def longest_substring(s, k):
    n = number_of_distinct_characters(s)
    if k > n:
        return 0
    if k == n:
        return len(s)
    start, end, max_length = 0, k, k
    while end < len(s):
        end += 1
        while True:
            distinct_chars = number_of_distinct_characters(s[start:end])
            if distinct_chars <= k:
                break
            start += 1
        max_length = max(max_length, end - start)
    return max_length

def main():
    print("Longest substring of \"{0}\" with {1} distinct characters: {2}".format("bavasd", 2, longest_substring("bavasd", 2)))

if __name__ == "__main__":
    main()