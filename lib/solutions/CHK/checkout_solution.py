price_dct = {

| A | 50 | 3Afor 130, 5A for 200 |
| B | 30 | 2B for 45 |
| C | 20 | |
| D | 15 | |
| E | 40 | 2E get one B free |
| F | 10 | 2F get one F free |
| G | 20 | |
| H | 10 | 5H for 45, 10H for 80 |
| I | 35 | |
| J | 60 | |
| K | 80 | 2K for 150 |
| L | 90 | |
| M | 15 | |
| N | 40 | 3N get one M free |
| O | 10 | |
| P | 50 | 5P for 200 |
| Q | 30 | 3Q for 80 |
| R | 50 | 3R get one Q free |
| S | 30 | |
| T | 20 | |
| U | 40 | 3U get one U free |
| V | 50 | 2V for 90, 3V for 130 |
| W | 20 | |
| X | 90 | |
| Y | 10 | |
| Z | 50 | |

}


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
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
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
        elif item == 'F':
            # Every 3F bundle counts as 2 of the og price
            summ += (item_counter[item] // 3 * (price_dct[item]*2)) + (item_counter[item] % 3 * price_dct[item])
        else:
            summ += item_counter[item] * price_dct[item]

    return summ

