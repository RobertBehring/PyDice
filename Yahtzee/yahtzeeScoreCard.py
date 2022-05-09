class YahtzeeScoreCard:

    def __init__(self, player_count):
        """

        :param player_count:
        """
        self._player_count = player_count
        self._score_cards = []

        # append a player card onto the _score_cards list, for the number of
        # players indicated by the user.
        for player in range(player_count):
            player_card = [{
                # Player Details
                'player number': player + 1
            }, {
                # Upper Scores *If sum >= 63 -> Total Score += 35
                'aces': None,
                'twos': None,
                'threes': None,
                'fours': None,
                'fives': None,
                'sixes': None,
                'bonus': False
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
            self._score_cards.append(player_card)

    def determine_player_card(self, player_number: int) -> object:
        """
        Returns the player_card dictionary object when given a player's number
        :param player_number:
        :return:
        """
        for player in range(self._player_count):
            player_card = self._score_cards[player]
            if player_card[0]['player number'] == player_number:
                return player_card

    def get_upper_score(self, player_number: int) -> int:
        """
        Returns the total upper score for the indicated player number
        :param player_number:
        :return: player_number upper score
        """
        player_card = self.determine_player_card(player_number)
        upper_section_scores = player_card[1].values()

        upper_score = 0
        for score in upper_section_scores:
            if score is not None:
                upper_score += score
        return upper_score

    def get_lower_score(self, player_number: int) -> int:
        """
        Returns the total lower score for the indicated player number
        :param player_number:
        :return: player_number lower score
        """
        player_card = self.determine_player_card(player_number)
        lower_section_scores = player_card[2].values()

        lower_score = 0
        for score in lower_section_scores:
            if score is not None:
                lower_score += score
        return lower_score

    def check_bonus(self, player_number: int) -> bool:
        """
        Returns a bool whether a player has >= 63 points in the upper
        section of their scorecard.
        :param player_number:
        :return:
        """
        if self.get_upper_score(player_number) >= 63:
            return True
        return False

    def get_grand_total(self, player_number: int) -> int:
        """
        Returns the grand total (upper + bonus + lower scores) for
        respective player_number
        :param player_number:
        :return:
        """
        bonus = 0
        if self.check_bonus(player_number) is True:
            bonus = 35

        return self.get_upper_score(player_number) + bonus + \
            self.get_lower_score(player_number)

    def set_score(self, player_number: int, section: str, score: int) -> None:
        """
        Sets the score for a section in the respective player_number's
        scorecard.
        :param player_number:
        :param section:
        :param score:
        :return: None
        """
        player_card = self.determine_player_card(player_number)

        if section in player_card[1]:
            player_card[1][section] = score
        elif section in player_card[2]:
            player_card[2][section] = score

    def display_score_card(self, player_number: int) -> None:
        """
        Displays player_number's respective scorecard
        :param player_number:
        :return: None
        """
        player_card = self.determine_player_card(player_number)
        for section in player_card:
            for item in section:
                print("{} : {}".format(item, section[item]))

    def display_all_cards(self) -> None:
        """
        Displays all players scorecards
        :return: None
        """
        for player in range(1, self._player_count+1):
            self.display_score_card(player)
            print('')


if __name__ == '__main__':
    scores = YahtzeeScoreCard(4)
    scores.display_all_cards()
