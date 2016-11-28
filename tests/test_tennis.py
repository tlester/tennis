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
                'p1name': 'Player 1',
                'mode': 'set',
                'p1wins': 5,
                'p2wins': 0}
        self.assertNotEqual(validate_args(args), None)
        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Forty',
                'p1name': 'Player 1',
                'mode': 'set',
                'p1wins': 5,
                'p2wins': 0}
        self.assertEqual(validate_args(args), None)
        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Thirty',
                'p1name': 'Player 1',
                'mode': 'set',
                'p1wins': 5,
                'p2wins': 0}
        self.assertNotEqual(validate_args(args), None)
        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Thirty',
                'p1name': 'Player 1',
                'mode': 'set',
                'p1wins': 6,
                'p2wins': 0}
        self.assertNotEqual(validate_args(args), None)


    def test_record_point(self):

        score = {'p1score': 0, 'p2score': 0}
        score = record_point(score, 'p1')
        self.assertEqual(score['p1score'], 1)

        score = {'p1score': 4, 'p2score': 3}
        score = record_point(score, 'p1')
        self.assertEqual(score['p1score'], 5)

        score = {'p1score': 4, 'p2score': 3}
        score = record_point(score, 'p2')
        self.assertEqual(score['p1score'], 3)

    def test_report_score(self):
        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        score = {'p1score': 0,
                 'p2score': 0}
        game_standing = report_score(args, score)
        self.assertFalse(game_standing[0])
        self.assertEqual(game_standing[2], 'Love-Love')

        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        score = {'p1score': 4,
                 'p2score': 3}
        game_standing = report_score(args, score)
        self.assertFalse(game_standing[0])
        self.assertEqual(game_standing[2], 'Advantage Player 1!')

        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        score = {'p1score': 3,
                 'p2score': 3}
        game_standing = report_score(args, score)
        self.assertFalse(game_standing[0])
        self.assertEqual(game_standing[2], 'Deuce!')

        args = {'p2name': 'Player 2',
                'p1score': 'Advantage',
                'p2score': 'Advantage',
                'p1name': 'Player 1'}
        score = {'p1score': 5,
                 'p2score': 3}
        game_standing = report_score(args, score)
        self.assertTrue(game_standing[0])
        self.assertEqual(game_standing[2], 'Player 1 wins the game')

if __name__ == '__main__':
    unittest.main()
