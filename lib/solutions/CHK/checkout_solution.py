price_dct = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+
    """
    # TODO: check if the input is split by space
    skus_arr = skus.split(" ")
    item_counter = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for item in skus_arr:
        # Invalid item
        if item not in item_counter:
            return -1
        # Increment the item_counter
        item_counter[item] += 1

    # Take cnt of A//3*130 + A%3*50 to get sum for A
    # Ex: A cnt is 5, then 5//3*130=1*130=130 + 5%3*50=2*50=100 = 230
    # For B cnt do the same: B//2*45 + B%2*30
    # C: C*20
    # D: D*15
    summ = 0
    for item in item_counter:
        if item == 'A':
            summ += (item_counter[item] // 3 * 130) + (item_counter[item] % 3 * price_dct[item])
        elif item == 'B':
            summ += (item_counter[item] // 2 * 45) + (item_counter[item] % 3 * price_dct[item])
        else:
            summ += item_counter[item] * price_dct[item]

    return summ



