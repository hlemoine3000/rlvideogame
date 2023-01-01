import argparse

from rlvideogame import game


def argument_parser():
    """
    Create a parser for main rlvideogame.

    Returns:
        argparse.ArgumentParser:
    """
    parser = argparse.ArgumentParser(description='Evaluate model predictions.')
    parser.add_argument('-g',
                        '--game',
                        help='Launch the game.',
                        action='store_true')
    return parser


def main():
    args = argument_parser().parse_args()

    if args.game:
        game.game()


main()
