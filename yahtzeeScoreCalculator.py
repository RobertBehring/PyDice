# Description: Yahtzee Score Calculator is a program that calculates scores
# in the game of Yahtzee for any # of players. Scores are calculated using
# standard yahtzee scoring algorithms and are generated via user given die
# values.

"""
                            !!! KNOWN BUGS !!!
1. Program will quit if invalid integer value is input during player or
die entry

2.
"""
import random

class PlayerScore:
    """
    Holds player score and contains methods to calculate score based on
    given die values
    """

    def __init__(self):
        self._player_scores = [{
            # Upper Scores *If sum >= 63 -> Total Score += 35
            'aces': None,
            'twos': None,
            'threes': None,
            'fours': None,
            'fives': None,
            'sixes': None,
        }, {
            # Lower Scores
            'match three': None,
            'match four': None,
            'match five': None,
            'full house': None,
            'small straight': None,
            'large straight': None,
            'choice': None
        }]

    def calc_aces(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Count and add only aces
        :param dice_list:
        :return:
        """
        total_aces = 0
        value = 1
        for die in dice_list:
            if die == value:
                total_aces += value

        return total_aces

    def calc_twos(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Count and add only twos
        :param dice_list:
        :return:
        """
        total_aces = 0
        value = 2
        for die in dice_list:
            if die == value:
                total_aces += value

        return total_aces

    def calc_threes(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Count and add only threes
        :param dice_list:
        :return:
        """
        total_aces = 0
        value = 3
        for die in dice_list:
            if die == value:
                total_aces += value

        return total_aces

    def calc_fours(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Count and add only fours
        :param dice_list:
        :return:
        """
        total_aces = 0
        value = 4
        for die in dice_list:
            if die == value:
                total_aces += value

        return total_aces

    def calc_fives(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Count and add only fives
        :param dice_list:
        :return:
        """
        total_aces = 0
        value = 5
        for die in dice_list:
            if die == value:
                total_aces += value

        return total_aces

    def calc_sixes(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Count and add only sixes
        :param dice_list:
        :return:
        """
        total_aces = 0
        value = 6
        for die in dice_list:
            if die == value:
                total_aces += value

        return total_aces

    def calc_match_three(self, dice_list: list[int]) -> int:
        """
        TODO: docstring
        Add total of all three dice
        :param dice_list:
        :return:
        """
        value_range = set()
        for die in dice_list:
            value_range.add(die)

        count_dict = {}
        count = 0
        for value in value_range:
            for die in dice_list:
                if value == die:
                    count += 1
            count_dict[value] = count
            count = 0

        for value in count_dict:
            if count_dict[value] >= 3:
                return 3 * value

        return 0

    def calc_match_four(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Add total of all four dice
        :param dice_list:
        :return:
        """
        value_range = set()
        for die in dice_list:
            value_range.add(die)

        count_dict = {}
        count = 0
        for value in value_range:
            for die in dice_list:
                if value == die:
                    count += 1
            count_dict[value] = count
            count = 0

        for value in count_dict:
            if count_dict[value] >= 4:
                return 4 * value

        return 0

    def calc_match_five(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Yahtzee: Set 50 points
        :param dice_list:
        :return:
        """
        value_range = set()
        for die in dice_list:
            value_range.add(die)

        count_dict = {}
        count = 0
        for value in value_range:
            for die in dice_list:
                if value == die:
                    count += 1
            count_dict[value] = count
            count = 0

        for value in count_dict:
            if count_dict[value] >= 5:
                return 50

        return 0

    def calc_full_house(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Set 25 points
        :param dice_list:
        :return:
        """
        if self.calc_match_four(dice_list) > 0:
            return 0

        value_range = set()
        for die in dice_list:
            value_range.add(die)

        # check set: if only two values in set then they must be a match 3
        # and match 2, therefore full house
        if len(value_range) == 2:
            return 25

        return 0

    def calc_straight_small(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Set 30 points
        :param dice_list:
        :return:
        """
        sort_dice = sorted(dice_list)
        prev_die = sort_dice[0]
        straight_count = 0
        for die_index in range(1, len(sort_dice)):
            die = sort_dice[die_index]
            if prev_die == die-1:
                straight_count += 1
            prev_die = die

        if straight_count >= 4:
            return 30
        return 0

    def calc_straight_large(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Set 40 points
        :param dice_list:
        :return:
        """
        sort_dice = sorted(dice_list)
        prev_die = sort_dice[0]
        straight_count = 0
        for die_index in range(1, len(sort_dice)):
            die = sort_dice[die_index]
            if prev_die == die-1:
                straight_count += 1
            prev_die = die

        if straight_count >= 5:
            return 40
        return 0

    def calc_choice(self, dice_list: list[int]) -> int:
        """
        TODO: Implement
        Total of all five dice regardless of number
        :param dice_list:
        :return:
        """
        choice = 0
        for die in dice_list:
            choice += die

        return choice

    def display_choices(self, dice_list: list[int]) -> None:
        """
        Todo: Implement
        Based on user input dic_tup prints score calculations in a numbered
        list format. Asks for user input and adds score value to total score
        (upper and lower score as appropriate). Returns None.
        :param dice_list:
        :return:
        """
        # upper_list = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes']
        score_dict = [{
            # upper scores
            'aces': self.calc_aces(dice_list),
            'twos': self.calc_twos(dice_list),
            'threes': self.calc_threes(dice_list),
            'fours': self.calc_fours(dice_list),
            'fives': self.calc_fives(dice_list),
            'sixes': self.calc_sixes(dice_list),
        },{
            # lower scores
            'match three': self.calc_match_three(dice_list),
            'match four': self.calc_match_four(dice_list),
            'match five': self.calc_match_five(dice_list),
            'full house': self.calc_full_house(dice_list),
            'small straight': self.calc_straight_small(dice_list),
            'large straight': self.calc_straight_large(dice_list),
            'choice': self.calc_choice(dice_list)
        }]
        score_choices = []
        section_index = 0
        for section in score_dict:
            for score in section:
                if self._player_scores[section_index][score] is None:
                    print(f'{score}: {section[score]}')
                    score_choices.append(score)
            section_index += 1

        # NEED TO REPEAT WHEN SCORE_CHOICE HAS ALREADY BEEN TAKEN
        print('')
        score_choice = str(input('Which score would you like to add: '
                                     '')).lower()
        while score_choice not in score_choices:
            score_choice = str(input('Selection not displayed, please '
                                     're-enter which score you would like '
                                     'to add: ')).lower()

        # add chosen score to total score
        section_index = 0
        for section in self._player_scores:
            for score in section:
                if score == score_choice:
                    section[score_choice] = score_dict[section_index][score_choice]
            section_index += 1

    def display_total_score(self) -> int:
        """
        Todo: implement
        :return:
        """
        total_score = 0
        for section in self._player_scores:
            for score in section:
                if section[score] is not None:
                    total_score += section[score]
            # add bonus if score in upper list is >= 63
            if total_score >= 63:
                total_score += 35

        return total_score


if __name__ == '__main__':
    print('\nWelcome to Yahtzee Score Calculator\n')

    number_of_players = int(input('Enter # of Players: '))
    player_list = []
    for player in range(number_of_players):
        player_list.append(PlayerScore())

    turns_left = len(player_list)*13
    player_turn = 0

    print(
        '------------------------------------------------------------------')
    print('1  2  3  4  5  6            GAME START            6  5  4  3  2  1')
    print(
        '------------------------------------------------------------------')

    while turns_left > 0:
        ############################ START OF TURN ##########################

        print(f'\n------------------------------------------------------------------\n'
              f'                        PLAYER #{player_turn+1} TURN START\n'
            '------------------------------------------------------------------')
        # DICE ROLL INPUT
        # redo = 'y'
        # while redo == 'y':
        #     dice_roll = []
        #     for die in range(1, 6):
        #         die_input = int(input(f'Enter die # {die}: '))
        #         while die_input <= 0 or die_input >= 7:
        #             die_input = int(input(f'Invalid Entry Please Enter die #'
        #                                   f' {die}: '))
        #         dice_roll.append(die_input)
        #     redo = str(input('\nWould you like to enter dice again? [y/n]: '
        #                      '')).lower()

        # RANDOM DICE ROLL FOR PLAYER
        dice_roll = []
        for die in range(5):
            roll = random.randint(1, 6)
            dice_roll.append(roll)
        print(dice_roll)

        print(
            f'------------------------------------------------------------------\n'
              f'                       PLAYER {player_turn+1} SCORE '
            f'CHOICE\n'
              '------------------------------------------------------------------')
        # SCORE CALCULATIONS AND CHOICE
        player_list[player_turn].display_choices(dice_roll)
        print('')
        for player in range(len(player_list)):
            print(f'PLAYER #{player+1} TOTAL SCORE: ',
              player_list[player].display_total_score())
        print(f'\n------------------------------------------------------------------\n'
              f'                        PLAYER #{player_turn+1} TURN END\n'
            '------------------------------------------------------------------')

        # Decrement turns left
        turns_left -= 1
        # Change player turn
        player_turn+= 1
        if player_turn >= len(player_list):
            player_turn = 0

        ############################# END OF TURN ###########################

    # WINNER/TIE DECLARATION
    winner = []
    winner_score = 0
    for player in range(len(player_list)):
        if player_list[player].display_total_score() > winner_score:
            winner = [player+1]
            winner_score = player_list[player].display_total_score()
        elif player_list[player].display_total_score() == winner_score:
            winner_score = player_list[player].display_total_score()
            winner.append(player+1)

    if len(winner) > 1:
        print('Players ')
        for player in winner:
            print('#',player, ', ')
        print('TIE')
        print(f'Total Score = {winner_score}')
    else:
        print(f'Player #{winner[0]} WINS')
        print(f'Player #{winner[0]} Score: {winner_score}')

