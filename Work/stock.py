# from dataclasses import dataclass
from typedproperty import String, Integer, Float


class Stock:
    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"

    # @property
    # def cost(self):
    #     return self.shares * self.price
    #
    # def sell(self, amt):
    #     self.shares = max(0, self.shares - amt)

    # @property
    # def shares(self):
    #     return self._shares
    #
    # @shares.setter
    # def shares(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError('Expected int')
    #     self._shares = value


# @dataclass
# class Stock:
#     name: str
#     shares: int
#     price: float
#
#     def cost(self):
#         return self.shares * self.price
#
#     def sell(self, amt):
#         self.shares = max(0, self.shares - amt)
