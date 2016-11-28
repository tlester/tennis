# -*- coding: utf-8 -*-
""" tennis scoring program
"""

import argparse
import sys

# I hate the idea of this being a global variable...  smelly, but works.
POINT_TABLE = {'Love': 0,
               'Fifteen': 1,
               'Thirty': 2,
               'Forty': 3,
               'Advantage': 4,
               'Game': 5}

def validate_args(args):
    """ This function validates arguments for the set up of the game.

        Inputs:
            args - the key/value hash table for argument values.

        Returns:
            args_result - String, error message.
    """

    if args['mode'] == 'set':
        if  args['p1wins'] == 6 and args['p2wins'] < 5:
            args_result = ('Invalid Input.  '
                           '{} has already won'.format(args['p1name']))
            return args_result
        if  args['p2wins'] == 6 and args['p1wins'] < 5:
            args_result = ('Invalid Input.  '
                           '{} has already won'.format(args['p2name']))
            return args_result

    if args['p1score'] == 'Advantage' and args['p2score'] == 'Advantage':
        args_result = 'Only one player can have Advantage'
        return args_result

    if args['p1score'] == 'Advantage' and args['p2score'] != 'Forty':
        args_result = ('If {} has the Advantage, then {}\'s score must '
                       'be Forty.').format(args['p1name'], args['p2name'])
        return args_result

    if args['p2score'] == 'Advantage' and args['p1score'] != 'Forty':
        args_result = ('If {} has the Advantage, then {}\'s score must '
                       'be Forty.').format(args['p2name'], args['p1name'])
        return args_result


def play_game(args, score):
    """ Plays the game until complete.  Then returns the game standing.

        Inputs:
            args - the key/value hash table for argument values.
            score - key/value hash table for score by player.

        Returns:
            game_standing - list,
                Frist elemnt is boolean expressing if the game is complete
                    (True) or not-complete (False).
                Second element is a string indicating who won the game.
                Thirt element is a string reporting the status of the game.
    """

    # As long as game_complete is not True, keep playing.
    game_complete = False
    while game_complete is False:
        scored = prompt_for_score(args)
        score = record_point(score, scored)
        game_standing = report_score(args, score)
        game_complete = game_standing[0]
        if game_standing[0]:
            return game_standing
        if scored != None:
            print game_standing[2]


def play_set(args, score):
    """ Playst the set by calling play_game until the enough games have been
        played to complete a winning set.

        Inputs:
            args - the key/value hash table for argument values.
            score - key/value hash table for score by player.

        Returns:
            string - Game standing or who won the set and score.
    """

    while True:
        game_standing = play_game(args, score)
        score = record_game(score, game_standing[1])
        if score['p1wins'] == 7:
            return '{} wins the game and set {}-{}'.format(args['p1name'],
                                                           score['p1wins'],
                                                           score['p2wins'])
        elif score['p2wins'] == 7:
            return '{} wins the game and set {}-{}'.format(args['p2name'],
                                                           score['p2wins'],
                                                           score['p1wins'])
        elif score['p1wins'] == 6 and (score['p1wins'] - score['p2wins']) > 1:
            return '{} wins the game and set {}-{}'.format(args['p1name'],
                                                           score['p1wins'],
                                                           score['p2wins'])
        elif score['p2wins'] == 6 and (score['p2wins'] - score['p1wins']) > 1:
            return '{} wins the game and set {}-{}'.format(args['p2name'],
                                                           score['p2wins'],
                                                           score['p1wins'])
        else:
            print game_standing[2]



def record_game(score, who_won):
    """ Calculates the new score after a game is won.

        Inputs:
            score - Dict, the key/value pair of the current state of game.
            who_scored - String, The player (p1|p2) who made the point.

        Returns:
            score - Dict, the key/value pair of the current state of game.
    """

    score['p1score'] = 0
    score['p2score'] = 0
    if who_won == 'p1':
        score['p1wins'] += 1
        return score
    else:
        score['p2wins'] += 1
        return score


def record_point(score, who_scored):
    """ Calculates the new score after a point is made.  If the play is
        ad after duece, then if the trailing player scores, the leading player
        drops a point back to duece.  Otherwise, a point is just added to the
        player who scored the point.

        Inputs:
            score - Dict, the key/value pair of the current state of game.
            who_scored - String, The player (p1|p2) who made the point.

        Returns:
            score - Dict, the updated key/value pair of current state of
            game.
    """

    if who_scored == 'p1' and score['p2score'] < 4:
        score['p1score'] += 1
    if who_scored == 'p1' and score['p2score'] == 4:
        score['p2score'] -= 1
    if who_scored == 'p2' and score['p1score'] < 4:
        score['p2score'] += 1
    if who_scored == 'p2' and score['p1score'] == 4:
        score['p1score'] -= 1
    return score

def prompt_for_score(args):
    """ Prompts user for scoring input.

        Returns:  String - player who scored (p1|p2)
    """

    point_winner = raw_input('Who scored: ')
    if point_winner == '{} scores!'.format(args['p1name']):
        return 'p1'
    elif point_winner == '{} scores!'.format(args['p2name']):
        return 'p2'
    else:
        print('Who???   Valid responses are "{} scores!" or '
              '"{} scores!"').format(args['p1name'], args['p2name'])
        return None


def report_score(args, score):
    """ This function takes the current score and evaluates it for reporting
        purposes.

        Inputs:
            args - the key/value hash table for argument values.
            score - key/value hash table for score by player.

        Returns:
            list - three element list.
                    Frist elemnt is boolean expressing if the game is complete
                        (True) or not-complete (False).
                    Second element is a string indicating who won the game.
                    Thirt element is a string reporting the status of the game.
    """

    terms = {0: 'Love',
             1: 'Fifteen',
             2: 'Thirty',
             3: 'Forty',
             4: 'Advantage',
             5: 'Game'}

    if score['p1score'] >= 4 and score['p1score'] - score['p2score'] > 1:
        return [True, 'p1', '{} wins the game'.format(args['p1name'])]

    if score['p2score'] >= 4 and score['p2score'] - score['p1score'] > 1:
        return [True, 'p2', '{} wins the game'.format(args['p2name'])]

    if score['p1score'] == 4 and score['p2score'] == 3:
        return [False, '', 'Advantage {}!'.format(args['p1name'])]

    if score['p2score'] == 4 and score['p1score'] == 3:
        return [False, '', 'Advantage {}!'.format(args['p2name'])]

    if score['p1score'] == 3 and score['p2score'] == 3:
        return [False, '', 'Deuce!']

    return [False, '', '{}-{}'.format(terms[score['p1score']],
                                      terms[score['p2score']])]

def main():
    """ This is the main driver of the application.
    """

    # Get initialization arguments from the command line and format usage
    description = ('A tennis game is won by the first player to score four '
                   'points in total and at least two points more than the '
                   'opponent. The words used to describe scores in tennis are: '
                   'Love, Fifteen, Thirty, and Forty.  This program keeps '
                   'track of scoring.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--p1name', default='Player 1', help="Player 1's name")
    parser.add_argument('--p2name', default='Player 2', help="Player 2's name")
    parser.add_argument('--p1score', default='Love',
                        help=('Initial score for player 1 - One of Love, '
                              'Fifteen, Thirty, Forty, Advantage.  '
                              'Default is Love.'),
                        choices=['Love', 'Fifteen', 'Thirty', 'Forty',
                                 'Advantage'])
    parser.add_argument('--p2score', default='Love',
                        help=('Initial score for player 2 - One of Love, '
                              'Fifteen, Thirty, Forty, Advantage.  '
                              'Default is Love.'),
                        choices=['Love', 'Fifteen', 'Thirty', 'Forty',
                                 'Advantage'])
    parser.add_argument('--p1wins', default=0, type=int,
                        choices=[0, 1, 2, 3, 4, 5, 6],
                        help=('The initial number of wins for player 1 - '
                              '(an integer between 0 and 6 - default is 0)'))
    parser.add_argument('--p2wins', default=0, type=int,
                        choices=[0, 1, 2, 3, 4, 5, 6],
                        help=('The initial number of wins for player 2 - '
                              '(an integer between 0 and 6 - default is 0)'))
    parser.add_argument('--mode', default='set', choices=['game', 'set'],
                        help=('Whether to run the program in game mode or set '
                              'mode (one of game or set - default is set.'))
    args = vars(parser.parse_args())

    # Validate arguments and exit on error.
    args_error = validate_args(args)
    if args_error != None:
        sys.exit(args_error)

    score = {'p1score': int(POINT_TABLE[args['p1score']]),
             'p2score': int(POINT_TABLE[args['p2score']]),
             'p1wins': args['p1wins'],
             'p2wins': args['p2wins']}

    if args['mode'] == 'game':
        play_game(args, score)
    else:
        print play_set(args, score)




if __name__ == "__main__":
    sys.exit(main())
