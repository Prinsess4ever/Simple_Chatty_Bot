integer = input().split()
result_list = []
result_list.append(integer[-1])
result_list.remove(integer[-1])
last_integer = integer[0]
result_list.remove(integer[0])
result_list.append(integer)
result_list.append(last_integer)
