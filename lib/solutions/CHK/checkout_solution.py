price_dct = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}


def bundle_and_reduce_inventory(item, bundle_cnt, bundle_price, item_counter):
    '''
    Takes in cnt of items and bundle price
    Updates the inventory cnt and returns price of bundled items (that were removed from inventory)
    Pls note the side effect of inventory update
    '''
    full_bundle_price = (item_counter[item] // bundle_cnt) * bundle_price
    item_counter[item] %= bundle_cnt
    return full_bundle_price


def bundle_and_get_free_cnt(buy_item, bundle_thresh, free_item, item_counter):
    """
    Given a buy_item and the bundle_thresh, deducts the item_counter accordingly based on the free_item
    """
    free_item_cnt = item_counter[buy_item] // bundle_thresh
    item_counter[free_item] = max(0, item_counter[free_item] - free_item_cnt)
    return


def checkout(skus):
    """
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+
    """
    skus_arr = list(skus)

    item_counter = dict()
    for k in price_dct.keys():
        item_counter[k] = 0

    for item in skus_arr:
        # Invalid item
        if item not in item_counter:
            return -1
        # Increment the item_counter
        item_counter[item] += 1

    summ = 0
    # Free item discounts
    bundle_and_get_free_cnt('E', 2, 'B', item_counter)
    bundle_and_get_free_cnt('N', 3, 'M', item_counter)
    bundle_and_get_free_cnt('R', 3, 'Q', item_counter)

    # Handle special mixed item discount
    # List is ordered from most to least exp
    special = ['Z', 'Y', 'S', 'T', 'X']
    special_cnt = 0
    for s in special:
        special_cnt += item_counter[s]
    summ += (special_cnt // 3) * 45  # Buy any 3 for 45
    while special_cnt >= 3:
        # Always favour customer, so we should deduct the cnt from the most expensive first
        for s in special:
            if item_counter[s] > 0:
                item_counter[s] -= 1
                break
        special_cnt -= 1

    for item in item_counter:
        if item == 'A':
            summ += bundle_and_reduce_inventory(item, 5, 200, item_counter)
            summ += bundle_and_reduce_inventory(item, 3, 130, item_counter)

        elif item == 'B':
            summ += bundle_and_reduce_inventory(item, 2, 45, item_counter)

        elif item == 'F':
            # Every 3F bundle counts as 2 of the og price
            summ += bundle_and_reduce_inventory(item, 3, price_dct[item] * 2, item_counter)

        elif item == 'H':
            summ += bundle_and_reduce_inventory(item, 10, 80, item_counter)
            summ += bundle_and_reduce_inventory(item, 5, 45, item_counter)

        elif item == 'K':
            summ += bundle_and_reduce_inventory(item, 2, 150, item_counter)

        elif item == 'P':
            summ += bundle_and_reduce_inventory(item, 5, 200, item_counter)

        elif item == 'Q':
            summ += bundle_and_reduce_inventory(item, 3, 80, item_counter)

        elif item == 'U':
            # Every 4U bundle counts as 3 of the og price
            summ += bundle_and_reduce_inventory(item, 4, price_dct[item] * 3, item_counter)

        elif item == 'V':
            summ += bundle_and_reduce_inventory(item, 3, 130, item_counter)
            summ += bundle_and_reduce_inventory(item, 2, 90, item_counter)

        summ += item_counter[item] * price_dct[item]

    return summ


