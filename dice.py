def rec(cnt, total):
    # print("cnt: " + str(cnt) + " total: " + str(total))
    if cnt == 1 and total <= 6 and total >= 1:
        return 1
    elif cnt == 1:
        return 0
    else:
        if table[cnt - 1][total - 1] == -1:
            sum = 0
            for i in range(1, 7):
                if total - i > 0:
                    sum += rec(cnt - 1, total - i)
            table[cnt - 1][total - 1] = sum
        return table[cnt - 1][total - 1]


def main():
    dice_cnt = input("How many dice? ")
    dice_cnt = int(dice_cnt)

    for i in range(dice_cnt, dice_cnt * 6 + 1):
        global table
        table = [[-1 for x in range(i)] for y in range(dice_cnt)]
        # print(table)
        
        print("total of " + str(i) + ": " + str(rec(dice_cnt, i) / 6 ** dice_cnt * 100) + "%")
        # print(table)


if __name__ == "__main__":
    main()