def compare_versions(version1, version2):
    v1_list = list(map(int, version1.split(".")))
    v2_list = list(map(int, version2.split(".")))
    max_length = max(len(v1_list), len(v2_list))
    v1_list = v1_list + [0] * (max_length - len(v1_list))
    v2_list = v2_list + [0] * (max_length - len(v2_list))
    if v1_list < v2_list:
        return -1
    elif v1_list == v2_list:
        return 0
    else:
        return 1


# def compare_versions(version1, version2):
#     # convert the input string into a list of integers
#     version1_parts = list(map(int, version1.split(".")))
#     version2_parts = list(map(int, version2.split(".")))
    
#     # find the length of the two version lists
#     version1_len = len(version1_parts)
#     version2_len = len(version2_parts)
    
#     # get the minimum length of the two version lists
#     min_len = min(version1_len, version2_len)
    
#     # loop through the two lists and compare each part
#     for i in range(min_len):
#         if version1_parts[i] > version2_parts[i]:
#             return 1 # version1 is greater
#         elif version1_parts[i] < version2_parts[i]:
#             return -1 # version2 is greater
    
#     # if all parts of the two lists are equal
#     if version1_len < version2_len:
#         return 0 # both versions are equal 
#     elif version1_len > version2_len:
#         return 1 # version1 is greater
#     else:
#         return -1 # version2 is greater


print(compare_versions("1.5", "2.12.4.0.6")) # returns -1
print(compare_versions("1.0.0", "1.0.0")) # returns 0
print(compare_versions("2", "2.0.0.1")) # returns 1