# coding=utf-8
"""Download audio."""
import argparse
import sys

from . import soundcloud, youtube


def download(query, include=None, exclude=None, quiet=False, overwrite=False):
    """Scrape various websites for audio."""
    youtube.scrape(query, include, exclude, quiet, overwrite)
    soundcloud.scrape(query, include, exclude, quiet, overwrite)


def main(args=None):
    """CLI for scraping audio."""
    if args is None:
        args = sys.argv[1:]

    # Parse program arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'query', default="Cerulean Crayons", nargs='?', help="search terms")
    parser.add_argument(
        '-i',
        '--include',
        default=[],
        action='append',
        help="only download audio with this tag (this flag can be used multiple times)"
    )
    parser.add_argument(
        '-e',
        '--exclude',
        default=[],
        action='append',
        help="ignore results with this tag (this flag can be used multiple times)"
    )
    parser.add_argument(
        '-q',
        '--quiet',
        default=False,
        action='store_true',
        help="hide progress reporting")
    parser.add_argument(
        '-o',
        '--overwrite',
        default=False,
        action='store_true',
        help="overwrite existing files")
    args = parser.parse_args()

    # Search YouTube and download audio from videos.
    if not args.quiet:
        print('Downloading audio from "{}" videos tagged {} and not {}.'.
              format(args.query, args.include, args.exclude))
    download(args.query, args.include, args.exclude, args.quiet,
             args.overwrite)
    if not args.quiet:
        print("Finished downloading audio.")


if __name__ == "__main__":
    main()
