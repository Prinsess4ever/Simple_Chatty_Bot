string = input().split()
result = ''
result += string[0].lower()
string.remove(string[0])
for i in string:
    result += i.capitalize()
print(result)
