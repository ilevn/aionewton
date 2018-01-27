"""An asnycio-based wrapper for `https://newton.now.sh`"""

import inspect
from urllib.parse import quote

import aiohttp


class Result:
    def __init__(self, **kwargs):
        self.operation = kwargs.get("operation", None)
        self.expression = kwargs.get("expression", None)
        self.result = kwargs.get("result", None)
        self.dict = kwargs

    def __str__(self):
        return self.result

    __repr__ = __str__


async def _make_request(expression):
    """Internal function to request a page by using a given string"""

    operation = inspect.stack()[1][3]
    encoded_expression = quote(expression, safe='')
    url = f"https://newton.now.sh/{operation}/{encoded_expression}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as req:
            assert isinstance(req, aiohttp.ClientResponse)

            res = await req.json()
            return Result(**res)


class AioNewton:

    # Every function returns a Result object containing the `operation`,
    # provided `expression` and the `result` as exposed attributes.

    async def simplify(self, expression: str) -> Result:
        """Simplify 2^2+2(2) -> 8"""
        return await _make_request(expression)

    async def factor(self, expression: str) -> Result:
        """Factor x^2 + 2x -> x (x + 2) """
        return await _make_request(expression)

    async def derive(self, expression: str) -> Result:
        """Derive x^2+2x -> 2 x + 2"""
        return await _make_request(expression)

    async def integrate(self, expression: str) -> Result:
        """Integrate x^2+2x -> 1/3 x^3 + x^2 + C"""
        return await _make_request(expression)

    async def zeroes(self, expression: str) -> Result:
        """Find 0's x^2+2x -> [-2, 0]"""
        return await _make_request(expression)

    async def tangent(self, expression: str) -> Result:
        """Find Tangent 2lx^3 -> 12 x + -16"""
        return await _make_request(expression)

    async def area(self, expression: str) -> Result:
        """Area Under Curve 2:4lx^3 -> 60"""
        return await _make_request(expression)

    async def cos(self, expression: str) -> Result:
        """Cosine pi -> -1"""
        return await _make_request(expression)

    async def sin(self, expression: str) -> Result:
        """Sine 0 -> 0"""
        return await _make_request(expression)

    async def tan(self, expression: str) -> Result:
        """Tangent 0 -> 0"""
        return await _make_request(expression)

    async def arccos(self, expression: str) -> Result:
        """Inverse Cosine 1 -> 0"""
        return await _make_request(expression)

    async def arcsin(self, expression: str) -> Result:
        """Inverse Sine 0 -> 0"""
        return await _make_request(expression)

    async def arctan(self, expression: str) -> Result:
        """Inverse Tangent 0 -> 0"""
        return await _make_request(expression)

    async def abs(self, expression: str) -> Result:
        """Absolute Value -1 -> 1"""
        return await _make_request(expression)

    async def log(self, expression: str) -> Result:
        """Logarithm 2l8 -> 3"""
        return await _make_request(expression)
