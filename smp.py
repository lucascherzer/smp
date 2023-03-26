import logging
import argparse
from usp.tree import sitemap_tree_for_homepage

PARSER = argparse.ArgumentParser(
    prog="smp",
    description="Sitemap Parser"
    )

PARSER.add_argument("target",
                    help="Target URL"
                    )

PARSER.add_argument("-l",
                    "--loglevel",
                    required=False,
                    nargs=1,
                    choices=["debug","info", "warn", "error", "critical"],
                    help="The log level for USP. Default is 'critical'",
                    default=["critical"]
                    )
ARGS = PARSER.parse_args()


LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}

# Change logger config according to args 
level = LOG_LEVELS[ARGS.loglevel[0]] # ARGS.loglevel is a list but only holds one value
logging.getLogger("usp.fetch_parse").setLevel(level)
logging.getLogger("usp.helpers").setLevel(level)
logging.getLogger("usp.tree").setLevel(level)


tree = sitemap_tree_for_homepage(ARGS.target)
for page in tree.all_pages():
    print(page.url)