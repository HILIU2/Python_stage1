item = ['December 23, 2015', 'Bread Gloves', 8.15]

# make sure that the number of variables equals to the number of items in the []
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.15]  # Unpack the list

print(name)


# Unpack items of different length

def drop_first_last(grades):
    first, *middle, last = grades    # take all of items into middle
    average = sum(middle) / len(middle)
    print("average of middle", average)
    print("first", first)
    print("last", last)

drop_first_last([65, 76, 98, 54, 21])

