#działa tylko jeśli brakuje tylko jednej pomiędzy, żeby działało tak że może być więcej braków pomiedzy trzeba by 
#new_list wygenerowac miedzy min a max wartościa z listy

def find_the_smallest_missing_empty_index (unsorted_list):
    min_in_unsorted_list=min(unsorted_list)
    new_list = []

    if min_in_unsorted_list<0: min_value=1
    else: min_value=min_in_unsorted_list

    for item in range(len(unsorted_list)+1): new_list.append(False)

    for value in unsorted_list:
        if value>=0:
            index_in_new_list=value-min_value
            new_list[index_in_new_list]=True
    the_smallest_missing=new_list.index(False)+min_value
    return the_smallest_missing
