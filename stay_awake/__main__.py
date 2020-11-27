import logging
import argparse
import time

from pynput.keyboard import Key, Controller


def stay_awake(interval):
    keyboard = Controller()

    logging.info("Staying awake.")
    while True:
        time.sleep(interval)
        keyboard.press(Key.shift)
        logging.debug("The shift key was pressed.")


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--interval',
                        type=int,
                        default=30,
                        help='Interval between keypress')
    parser.add_argument("-v", "--verbose",
                        help="Increase output verbosity",
                        action="store_true")

    args = parser.parse_args()

    logging.basicConfig(format="%(asctime)s: %(message)s",
                        level=logging.DEBUG if args.verbose else logging.INFO,
                        datefmt="%H:%M:%S")

    stay_awake(args.interval)


if __name__ == '__main__':
    main()

