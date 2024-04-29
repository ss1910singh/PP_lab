def search_element(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1

list = [1,2,3,4,5]

print(search_element(list, 3)) # 2
print(search_element(list, 6)) # -1
print(search_element(list, 1)) # 0
print(search_element(list, 5)) # 4