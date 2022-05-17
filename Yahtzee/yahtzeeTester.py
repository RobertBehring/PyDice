import unittest
import yahtzeeScoreCard as ScoreCard


class MyTestCase(unittest.TestCase):
    def test_scoreboards(self):
        yahtzee_score_cards = ScoreCard.YahtzeeScoreCard(4)
        player1_card = yahtzee_score_cards.determine_player_card(1)
        player2_card = yahtzee_score_cards.determine_player_card(2)
        player3_card = yahtzee_score_cards.determine_player_card(3)
        player4_card = yahtzee_score_cards.determine_player_card(4)
        self.assertEqual(player1_card[0]['player number'], 1)
        self.assertEqual(player2_card[0]['player number'], 2)
        self.assertEqual(player3_card[0]['player number'], 3)
        self.assertEqual(player4_card[0]['player number'], 4)


if __name__ == '__main__':
    unittest.main()
