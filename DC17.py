# Daily Coding 17
#
# Suppose we represent our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
#
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file
# file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" # represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
#
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext
# and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory
# subsubdir2 containing a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file
# system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2
# file2.ext", and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest
# absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
# Note:
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.

def max_length_of_link(link):
    directory = link.split("\n")
    if len(directory) < 1:
        return 0
    if len(directory) == 1:
        if "." in directory[0]:
            return len(directory[0])
        else:
            return 0
    if "." in directory[0]:
        return 0
    return len(directory[0]) + 1 + max_length_of_link_rec(directory[1:])

def max_length_of_link_rec(dir):
    # if this directory has only sub-directories, then the result is not in this directory
    if all(not "." in elem for elem in dir):
        return -99999
    
    # Analyze all sub-directories and files
    contents = []    
    files = []
    sub_dirs = []
    index_sub_dirs = []
    for elem in dir:
        if "." in elem and "\t" not in elem[1:]:
            files.append(elem[1:])
        if elem[0] == "\t":
            contents.append(elem[1:])
            if not "." in elem and not "\t" in elem[1:]:
                sub_dirs.append(elem[1:])
    for elem in sub_dirs:
        index_sub_dirs.append(contents.index(elem))
    
    # File links test
    arg1 = 0
    for file in files:
        temp = len(file)
        if arg1 < temp:
            arg1 = temp
    
    # Sub-directory links test
    arg2 = 0
    for i in range(len(sub_dirs)):
        temp = []
        if i == len(sub_dirs) - 1:
            temp = contents[index_sub_dirs[i] + 1 :]
        else:
            temp = contents[index_sub_dirs[i] + 1 : index_sub_dirs[i + 1]]
        length = len(sub_dirs[i]) + 1 + max_length_of_link_rec(temp)
        if length > arg2:
            arg2 = length
    return max(arg1, arg2)

def main():
    print("Test_1: " + str(max_length_of_link("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")))
    print("Test_2: " + str(max_length_of_link("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")))
    print("Test_3: " + str(max_length_of_link('dir\n\tfile1.ext\n\tsubdir\n\t\tsubsubdir\n\t\t\ttsubsubsubdir')))

if __name__ == "__main__":
    main()