# Challenge
Implement a program that keeps track of tennis game scoring.

# Tennis Scoring Summary
A tennis game is won by the first player to score four points in total and at
least two points more than the opponent. The words used to describe scores in
tennis are unusual:

| Point value | Word    |
| ----------- | ------- |
| 0           | Love    |
| 1           | Fifteen |
| 2           | Thirty  |
| 3           | Forty   |

A set is won by winning at least six games and at least two games more than the
opponent. Special case: if the set score is 6-5 and the trailing player
wins--making the set score 6-6--the next game wins the set.

# Summary

Implement a console program according to the specifications below. You should
have one commit for iteration one and a separate commit for iteration two. Your
program will be evaluated by a set of automated tests upon submission. Don't
worry, failing tests will not imply immediate disqualification. Also, don't
worry if you only satisfy the requirements of iteration one. Not all candidates
have time to accomplish both tasks, but it looks better if you do. If you do
finish both iterations, we will diff commits one and two to see how you
approached the exercise iteratively.

# Technical Details

* The program should accept the optional arguments described in Usage Description
  and set initial state accordingly
* The program should validate the passed arguments and print the Usage
  Description if an invalid argument is passed
    * Note: setting both --p1score and --p2score to "Advantage" for initial state
      is invalid since only one player may hold the advantage
      at a time
* Your program should block for additional user input until the game or set has
  been won (depending on mode) and then exit
* Valid input strings include:
    * "<Player 1> scores!" - where <Player 1> could be any name
    * "<Player 2> scores!" - where <Player 2> could be any name
* Your program should validate input strings and return a message of "Invalid
  Input" if the user inputs an invalid string

# Usage Description

    --p1name        Player 1's name
    --p2name        Player 2's name
    --p1score       The initial score for player 1 - (one of Love, Fifteen, Thirty, Forty, Advantage - default is Love)
    --p2score       The initial score for player 2 - (one of Love, Fifteen, Thirty, Forty, Advantage - default is Love)
    --p1wins        The initial # of wins for player 1 - (an integer between 0 and 6 - default is 0)
    --p2wins        The initial # of wins for player 2 (an integer between 0 and 6 - default is 0)
    --mode          Whether to run the program in game mode or set mode (one of game or set - default is set)

# Iteration One

## Feature: Game scoring

### Scenario Outline:  Player scores
Given The current score is <player1score> to <player2score> When The system receives <scoreEvent>
Then The system outputs <result>

Examples:
| player1score | player2score | scoreEvent | result |
| --- | --- | --- | --- |
| Fifteen | Thirty | Player 1 scores! | Thirty-Thirty |
| Forty | Thirty | Player 1 scores! | Player 1 wins the game |
| Love | Love | Player 2 scores! | Love-Fiftee |
| Forty | Thirty | Player 2 scores! |  Deuce! |
| Forty | Forty | Player 1 scores! | Advantage Player 1! |
| Advantage | | Player 1 scores! | Player 1 wins the game |
| Advantage | | PLayer 2 scores! | Deuce! |

