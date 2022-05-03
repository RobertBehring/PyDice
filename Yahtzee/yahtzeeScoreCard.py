class YahtzeeScoreCard:

    def __init__(self, player_count):
        """

        :param player_count:
        """
        self._player_count = player_count
        self._player_cards = []
        for player in range(player_count):
            self._player_cards.append({
                # Player Details
                'player number': player + 1
            })
            self._player_cards.append({
                # Upper Scores *If sum >= 63 -> Total Score += 35
                'aces': None,
                'twos': None,
                'threes': None,
                'fours': None,
                'fives': None,
                'sixes': None,
                'bonus': False
            })
            self._player_cards.append({
                # Lower Scores
                'match three': None,
                'match four': None,
                'match five': None,
                'full house': None,
                'small straight': None,
                'large straight': None,
                'choice': None
            })

    def get_upper_score(self, player_number: int) -> int:
        """
        Returns the total upper score for the indicated player number
        :param player_number:
        :return: player_number upper score
        """
        pass

    def get_lower_score(self, player_number: int) -> int:
        """
        Returns the total lower score for the indicated player number
        :param player_number:
        :return: player_number lower score
        """
        pass

    def check_bonus(self, player_number: int) -> bool:
        """
        Returns a bool whether a player has >= 63 points in the upper
        section of their scorecard.
        :param player_number:
        :return:
        """
        pass

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

    def set_score(self, player_number: int, section: int, score: int) -> None:
        """
        Sets the score for a section in the respective player_number's
        scorecard.
        :param player_number:
        :param section:
        :param score:
        :return: None
        """
        pass

    def display_score_card(self, player_number: int) -> None:
        """
        Displays player_number's respective scorecard
        :param player_number:
        :return: None
        """
        pass

    def display_all_cards(self) -> None:
        """
        Displays all players scorecards
        :return: None
        """
        pass
