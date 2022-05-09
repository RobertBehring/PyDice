import unittest
import yahtzeeScoreCard as ScoreCard


class MyTestCase(unittest.TestCase):
    def test_scoreboards(self):
        four_player_cards = ScoreCard.YahtzeeScoreCard(4)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
