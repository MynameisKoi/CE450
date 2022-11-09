def mrg(list1, list2):
    # merges 2 sorted list recursively
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    elif list1[0] < list2[0]:
        return [list1[0]] + mrg(list1[1:], list2)
    else:
        return [list2[0]] + mrg(list1, list2[1:])

print("mrg([1,3,5],[2,4,6]):", mrg([1,3,5],[2,4,6]))
print("mrg([],[2,4,6]):", mrg([],[2,4,6]))
print("mrg([1,3,5],[]):", mrg([1,3,5],[]))
print("mrg([5,7],[2,4,6]):", mrg([5,7],[2,4,6]))
