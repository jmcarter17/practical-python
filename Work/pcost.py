# pcost.py
#
# Exercise 1.27

import sys
import report


def portfolio_cost(filename):
    return sum(row.cost for row in report.read_portfolio(filename))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f"Total cost: ${cost}")


if __name__ == "__main__":
    main()
