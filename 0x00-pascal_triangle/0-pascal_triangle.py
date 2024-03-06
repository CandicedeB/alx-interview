#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal triangle
    Args:
      n (int): Number of rows of the triangle
    Returns:
      List of integers representing the Pascal triangle
    '''
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists
