price_dct = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+
    """
    skus_arr = list(skus)
    item_counter = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for item in skus_arr:
        # Invalid item
        if item not in item_counter:
            return -1
        # Increment the item_counter
        item_counter[item] += 1

    summ = 0
    for item in item_counter:
        if item == 'A':
            a_5_price = item_counter[item] // 5 * 200
            summ += a_5_price
            item_counter[item] %= 5
            summ += (item_counter[item] // 3 * 130) + (item_counter[item] % 3 * price_dct[item])
        elif item == 'B':
            free_b_cnt = item_counter['E'] // 2
            item_counter[item] = max(0, item_counter[item] - free_b_cnt)
            summ += (item_counter[item] // 2 * 45) + (item_counter[item] % 2 * price_dct[item])
        else:
            summ += item_counter[item] * price_dct[item]

    return summ

