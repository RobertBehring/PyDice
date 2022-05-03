class YahtzeeRules:

    def __init__(self, dice_list):
        self._dice_list = dice_list

    def calc_aces(self) -> int:
        """
        Count and add only aces
        :return:
        """
        total = 0
        value = 1
        for die in self._dice_list:
            if die == value:
                total += value

        return total

    def calc_twos(self) -> int:
        """
        Count and add only twos
        :return:
        """
        total = 0
        value = 2
        for die in self._dice_list:
            if die == value:
                total += value

        return total

    def calc_threes(self) -> int:
        """
        Count and add only threes
        :return:
        """
        total = 0
        value = 3
        for die in self._dice_list:
            if die == value:
                total += value

        return total

    def calc_fours(self) -> int:
        """
        Count and add only fours
        :return:
        """
        total = 0
        value = 4
        for die in self._dice_list:
            if die == value:
                total += value

        return total

    def calc_fives(self) -> int:
        """
        Count and add only fives
        :return:
        """
        total = 0
        value = 5
        for die in self._dice_list:
            if die == value:
                total += value

        return total

    def calc_sixes(self) -> int:
        """
        Count and add only sixes
        :return:
        """
        total_aces = 0
        value = 6
        for die in self._dice_list:
            if die == value:
                total_aces += value

        return total_aces

    def calc_match_three(self) -> int:
        """
        Add total of all three dice
        :return:
        """
        value_range = set()
        for die in self._dice_list:
            value_range.add(die)

        count_dict = {}
        count = 0
        for value in value_range:
            for die in self._dice_list:
                if value == die:
                    count += 1
            count_dict[value] = count
            count = 0

        for value in count_dict:
            if count_dict[value] >= 3:
                return 3 * value

        return 0

    def calc_match_four(self) -> int:
        """
        Add total of all four dice
        :return:
        """
        value_range = set()
        for die in self._dice_list:
            value_range.add(die)

        count_dict = {}
        count = 0
        for value in value_range:
            for die in self._dice_list:
                if value == die:
                    count += 1
            count_dict[value] = count
            count = 0

        for value in count_dict:
            if count_dict[value] >= 4:
                return 4 * value

        return 0

    def calc_match_five(self) -> int:
        """
        Yahtzee: Set 50 points
        :return:
        """
        value_range = set()
        for die in self._dice_list:
            value_range.add(die)

        count_dict = {}
        count = 0
        for value in value_range:
            for die in self._dice_list:
                if value == die:
                    count += 1
            count_dict[value] = count
            count = 0

        for value in count_dict:
            if count_dict[value] >= 5:
                return 50

        return 0

    def calc_full_house(self) -> int:
        """
        Set 25 points
        :return:
        """
        if self.calc_match_four(self._dice_list) > 0:
            return 0

        value_range = set()
        for die in self._dice_list:
            value_range.add(die)

        # check set: if only two values in set then they must be a match 3
        # and match 2, therefore full house
        if len(value_range) == 2:
            return 25

        return 0

    def calc_straight_small(self) -> int:
        """
        Set 30 points
        :return:
        """
        sort_dice = sorted(self._dice_list)
        prev_die = sort_dice[0]
        straight_count = 1
        for die_index in range(1, len(sort_dice)):
            die = sort_dice[die_index]
            if prev_die == die-1:
                straight_count += 1
            prev_die = die

        if straight_count >= 4:
            return 30
        return 0

    def calc_straight_large(self) -> int:
        """
        Set 40 points
        :return:
        """
        sort_dice = sorted(self._dice_list)
        prev_die = sort_dice[0]
        straight_count = 1
        for die_index in range(1, len(sort_dice)):
            die = sort_dice[die_index]
            if prev_die == die-1:
                straight_count += 1
            prev_die = die

        if straight_count >= 5:
            return 40
        return 0

    def calc_choice(self) -> int:
        """
        Total of all five dice regardless of number
        :return:
        """
        choice = 0
        for die in self._dice_list:
            choice += die

        return choice
