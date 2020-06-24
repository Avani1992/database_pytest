"""Read a given string, change the character at a given index and then print the modified string."""

s='abcd2fg'
def mutate_string(string, position, character):
    string=string[0:position]+character+string[position+1:]
    return string

result=mutate_string(s,4,'e')
print(result)