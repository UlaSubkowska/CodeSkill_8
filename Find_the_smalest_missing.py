def find_the_smallest_missing (unsorted_list):
    if min(unsorted_list)<=0:
        the_smallest_missing=1
    else:
        the_smallest_missing=min(unsorted_list)
    while True:
        if the_smallest_missing in unsorted_list:
            unsorted_list.remove(the_smallest_missing)
            the_smallest_missing+=1
        else:
            print(the_smallest_missing)
            break

Find_the_smallest_missing([2,3,4])
