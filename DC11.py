# Daily Coding 11
# Implement an autocomplete system. That is, given a query string s and a set of all possible query 
# strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

def autocomplete(list, query):
    for string in list:
        if string[0:len(query)] != query:
            list.remove(string)
    return list

def main():
    print(autocomplete(["dog", "deer", "deal"], "de"))

if __name__ == "__main__":
    main()