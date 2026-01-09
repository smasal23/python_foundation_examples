# Let "A" be a string. Remove all the whitespaces and find its length.

A = input()

def remove_all_spaces(string):
    Output = "".join(string.split()) # .join will join all elements together with "" meaning no space in between
                                     # where .split() separates string wherever space occurs
    return Output

print(len(remove_all_spaces(A)))