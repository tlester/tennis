import argparse
import sys

def validate_args(args):
    """ This function validates arguments for the set up of the game.

        Inputs:
            args - the key/value hash table for argument values.

        Returns:
            args_result - String, error message.
    """

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


def record_point(game_score, who_scored):
    """ Calculates the new score after a point is made.  If the play is
        ad after duece, then if the trailing player scores, the leading player
        drops a point back to duece.  Otherwise, a point is just added to the
        player who scored the point.

        Inputs:
            game_score - Dict, the key/value pair of the current state of game.
            who_scored - String, The player (p1|p2) who made the point.

        Returns:
            game_score - Dict, the updated key/value pair of current state of
            game.
    """
    if who_scored == 'p1' and game_score['p2score'] < 4:
        game_score['p1score'] += 1
    if who_scored == 'p1' and game_score['p2score'] == 4:
        game_score['p2score'] -= 1
    if who_scored == 'p2' and game_score['p1score'] < 4:
        game_score['p2score'] += 1
    if who_scored == 'p2' and game_score['p1score'] == 4:
        game_score['p1score'] -= 1
    return game_score

def who_scored(args):
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


def report_score(args, game_score):
    """ This function takes the current score and evaluates it for reporting
        purposes.

        Inputs:
            args - the key/value hash table for argument values.
            game_score - key/value hash table for score by player.

        Returns:
            list - two element list.  Frist elemnt is boolean expressing if
                   the game is complete (True) or not-complete (False).
    """

    terms = { 0: 'Love',
              1: 'Fifteen',
              2: 'Thirty',
              3: 'Forty',
              4: 'Advantage',
              5: 'Game'}

    if (game_score['p1score'] >= 4 and
        game_score['p1score'] - game_score['p2score'] > 1):
        return [True, '{} wins the game'.format(args['p1name'])]

    if game_score['p2score'] >= 4 and game_score['p1score'] < 3:
        return [True, '{} wins the game'.format(args['p2name'])]

    if game_score['p1score'] == 4 and game_score['p2score'] == 3:
        return [False, 'Advantage {}!'.format(args['p1name'])]

    if game_score['p2score'] == 4 and game_score['p1score'] == 3:
        return [False, 'Advantage {}!'.format(args['p2name'])]

    if game_score['p1score'] == 3 and game_score['p2score'] == 3:
        return [False, 'Deuce!']

    return [False, '{}-{}'.format(terms[game_score['p1score']],
                          terms[game_score['p2score']])]

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
    # Future feature
    # parser.add_argument('--p1wins', default=0,
    #                     help=('The initial number of wins for player 1 - '
    #                           '(an integer between 0 and 6 - default is 0)'))
    # parser.add_argument('--p2wins', default=0,
    #                     help=('The initial number of wins for player 2 - '
    #                           '(an integer between 0 and 6 - default is 0)'))
    # parser.add_argument('--mode', default='set',
    #                     help=('Whether to run the program in game mode or set '
    #                           'mode (one of game or set - default is set.'))
    args = vars(parser.parse_args())

    # Validate arguments and exit on error.
    args_error = validate_args(args)
    if args_error != None:
        sys.exit(args_error)


    point_table = { 'Love': 0,
                    'Fifteen': 1,
                    'Thirty': 2,
                    'Forty': 3,
                    'Advantage': 4,
                    'Game': 5 }

    game_score = { 'p1score': point_table[args['p1score']],
                   'p2score': point_table[args['p2score']] }


    # As long as game_complete is not True, keep playing.
    game_complete = False
    while game_complete == False:
        scored = who_scored(args)
        game_standing = report_score(args, record_point(game_score, scored))
        game_complete = game_standing[0]
        print game_standing[1]



if __name__ == "__main__":
    sys.exit(main())
