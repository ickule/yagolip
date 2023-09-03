import argparse
import os

from board import Board

MESSAGE = "After {} generations, here is the state of your board:"


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")  # noqa: S605 We are only cleaning stdout


def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="yagolip",
        description="This program is a simple command-line based game of life.",
        epilog="=====",
    )
    parser.add_argument(
        "--width",
        "-x",
        help="Width of the board",
        type=int,
    )
    parser.add_argument(
        "--height",
        "-y",
        help="Height of the board",
        type=int,
    )
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    if args.height is None:
        args.height = int(input("How tall shall your board be ?\n"))
    if args.width is None:
        args.width = int(input("How wide shall your board be ?\n"))
    generation = 0
    board = Board.random(args.width, args.height)
    clear()
    print(MESSAGE.format(generation))
    print(board)
    while input("Press ENTER to continue or q to quit.\n").lower() != "q":
        board.spread_life()
        generation += 1
        clear()
        print(MESSAGE.format(generation))
        print(board)


if __name__ == "__main__":
    main(argument_parser())
