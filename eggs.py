#!/usr/bin/env python3

if __name__ == "__main__":
    number_of_eggs: int = 854

    boxes_of_twelve = number_of_eggs // 12
    eggs_after_twelve = number_of_eggs % 12
    boxes_of_six = eggs_after_twelve // 6
    left_over = eggs_after_twelve % 6

    print(
        f"With {number_of_eggs} eggs, we can fill {boxes_of_twelve} boxes of twelve, "
        f"{boxes_of_six} boxes of six, and have {left_over} eggs left over."
    )
