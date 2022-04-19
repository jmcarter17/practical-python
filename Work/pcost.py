# pcost.py
#
# Exercise 1.27

import sys
import report


def portfolio_cost(filename):
    return report.read_portfolio(filename).total_cost


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f"Total cost: ${cost}")


if __name__ == "__main__":
    main()
