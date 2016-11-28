#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
test_tennis
----------------------------------

Tests for `tennis.py` module.
"""

import unittest
from tennis import *

class Testtennis(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_args(self):

        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        self.assertNotEqual(validate_args(args), None)
        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Forty',
                'p1name': 'Player 1'}
        self.assertEqual(validate_args(args), None)
        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Thirty',
                'p1name': 'Player 1'}
        self.assertNotEqual(validate_args(args), None)


    def test_record_point(self):

        game_score = {'p1score': 0, 'p2score': 0}
        game_score = record_point(game_score, 'p1')
        self.assertEqual(game_score['p1score'], 1)

        game_score = {'p1score': 4, 'p2score': 3}
        game_score = record_point(game_score, 'p1')
        self.assertEqual(game_score['p1score'], 5)

        game_score = {'p1score': 4, 'p2score': 3}
        game_score = record_point(game_score, 'p2')
        self.assertEqual(game_score['p1score'], 3)

    def test_report_score(self):
        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        game_score = {'p1score': 0,
                      'p2score': 0}
        game_standing = report_score(args, game_score)
        self.assertFalse(game_standing[0])
        self.assertEqual(game_standing[1], 'Love-Love')

        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        game_score = {'p1score': 4,
                      'p2score': 3}
        game_standing = report_score(args, game_score)
        self.assertFalse(game_standing[0])
        self.assertEqual(game_standing[1], 'Advantage Player 1!')

        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        game_score = {'p1score': 3,
                      'p2score': 3}
        game_standing = report_score(args, game_score)
        self.assertFalse(game_standing[0])
        self.assertEqual(game_standing[1], 'Deuce!')

        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        game_score = {'p1score': 5,
                      'p2score': 3}
        game_standing = report_score(args, game_score)
        self.assertTrue(game_standing[0])
        self.assertEqual(game_standing[1], 'Player 1 wins the game')

if __name__ == '__main__':
    unittest.main()
