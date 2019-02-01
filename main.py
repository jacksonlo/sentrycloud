import argparse
import os
from config import cache_file_name, token, sentry_url
from data import get_data, create_word_cloud, count
from log import logger
import logging


def main():
    if token is None:
        logger.error('Missing env variable "sentrycloudtoken"')
        return

    if sentry_url is None:
        logger.error('Missing env variable "sentryurl"')
        return

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--field',
        help='Field name to pull from sentry. [culprit, filename, title, type]',
        default='title',
    )
    parser.add_argument('--file', help='File path to export to. Ie. result.png', default='result.png')
    parser.add_argument(
        '--cache',
        help='Utilize cache result from the last Sentry API query. False will delete the previous cache.',
        default=False,
    )
    parser.add_argument('--verbose', help='Verbose to stdout', default=False)
    args = parser.parse_args()

    logger.info('Running with args: {}'.format(args))
    if args.verbose is False:
        logger.setLevel(logging.DEBUG)

    if parser.cache is False:
        os.remove(cache_file_name)

    dataMap = get_data()
    counts = count(dataMap, args.field)
    create_word_cloud(counts, args.file)

    if parser.cache is False:
        os.remove(cache_file_name)


if __name__ == "__main__":
    main()
