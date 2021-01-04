my_list = [0, 55, 77, 78, 59, 36, 43, 90, 45, 24]

page_num = 2
page_size = 3
pivot = 45

def getPage(page_num, page_size, pivot):
   
    # length of the list
    size = len(my_list)
    # total number of pages
    num_pages = int(size/page_size) + size % page_size

    # return empty if page_num is greater than total number of pages
    if page_num > num_pages:
        return []
    
    # acquire the index of the pivot
    pivot_index = my_list.index(pivot)
    
    # loop over the list
    for i in range(size):
        if i > pivot_index - 1:
            current_page = int((i - pivot_index)/page_size)
            if current_page == page_num:
                if i > (size - page_size):
                    # handle wrapping around the list
                    extra = ((i + page_size) - size)
                    return ([n for n in my_list[i:]] + [n for n in my_list[0:extra]])
                else:
                    return [n for n in my_list[i:i+page_size]]
                    
        else:
            current_page = int((size + i - pivot_index)/page_size)
            if current_page == page_num:
                # only handle pages that don't need to be wrapped around
                if ((size - pivot_index + i)%page_size) == 0:
                    if i > (pivot_index - page_size):
                        # handle the edge cases near the pivot/end of the pages
                        return([n for n in my_list[i:pivot_index]])
                    else:
                        return([n for n in my_list[i:i+page_size]])

print(getPage(page_num, page_size, pivot))

