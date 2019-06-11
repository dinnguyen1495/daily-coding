# Daily Coding 29
# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
# repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA"
# would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and
# consists solely of alphabetic characters. You can assume the string to be decoded is valid.

def encode(string):
    stack = []
    for c in string:
        if len(stack) == 0 or c != stack[-1][1]:
            stack.append([str(1), c])
            continue
        old_number = stack.pop(-1)[0]
        stack.append([str(int(old_number) + 1), c])
    return "".join("".join(elem) for elem in stack)

def decode(string):
    decode_result = ""
    j = 0
    for i in range(len(string)):
        try:
            val = int(string[i])
        except ValueError:
            decode_result += int(string[j:i]) * string[i]
            j = i + 1
    return decode_result

def main():
    encode_string = "AAAAAAAAAABBBCCDAA"
    print("Encode result for \"" + encode_string + "\": " + encode(encode_string))
    decode_string = "4A10B2C1D2A"
    print("Decode result for \"" + decode_string + "\": " + decode(decode_string))

if __name__ == "__main__":
    main()