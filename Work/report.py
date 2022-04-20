# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from portfolio import Portfolio

import tableformat


def read_prices(filename):
    with open(filename, "rt") as f:
        return dict(parse_csv(f, types=[str, float], has_headers=False))


def read_portfolio(filename, **opts):
    with open(filename, "rt") as f:
        return Portfolio.from_csv(f)


def make_report(portfolio, prices):
    return [
        (p.name, p.shares, prices[p.name], prices[p.name] - p.price)
        for p in portfolio
    ]


def print_report(report, formatter):
    headers = ("Name", "Shares", "Price", "Change")
    formatter.headings(headers)

    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'${price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    # if len(argv) < 3:
    #     raise SystemExit(f'Usage: {argv[0]} ' 'portfolio_file price_file')
    # portfile = argv[1]
    # pricefile = argv[2]
    # fmt = argv[3] if len(argv) >= 4 else "txt"
    # portfolio_report(portfile, pricefile, fmt)
    portfolio_report("Data/portfolio.csv", "Data/prices.csv", "txt")


if __name__ == "__main__":
    import sys
    import logging
    logging.basicConfig(
        filename="report.log",
        filemode="w",
        level=0
    )
    main(sys.argv)
