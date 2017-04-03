"""An asnycio-based wrapper for `https://newton.now.sh`"""

import inspect
from urllib.parse import quote

import aiohttp


class AioNewton:
    @staticmethod
    async def make_request(expression):
        """Internal function to request a page by using a given string"""

        operation = inspect.stack()[1][3]
        encoded_expression = quote(expression, safe='')
        url = f"https://newton.now.sh/{operation}/{encoded_expression}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as req:
                assert isinstance(req, aiohttp.ClientResponse)

                return await req.json()

    # Every function returns a dict containing the `operation`,
    # provided `expression` and the `result`.

    async def simplify(self, expression: str) -> dict:
        """Simplify 2^2+2(2) -> 8"""
        return await self.make_request(expression)

    async def factor(self, expression: str) -> dict:
        """Factor x^2 + 2x -> x (x + 2) """
        return await self.make_request(expression)

    async def derive(self, expression: str) -> dict:
        """Derive x^2+2x -> 2 x + 2"""
        return await self.make_request(expression)

    async def integrate(self, expression: str) -> dict:
        """Integrate x^2+2x -> 1/3 x^3 + x^2 + C"""
        return await self.make_request(expression)

    async def zeroes(self, expression: str) -> dict:
        """Find 0's x^2+2x -> [-2, 0]"""
        return await self.make_request(expression)

    async def tangent(self, expression: str) -> dict:
        """Find Tangent 2lx^3 -> 12 x + -16"""
        return await self.make_request(expression)

    async def area(self, expression: str) -> dict:
        """Area Under Curve 2:4lx^3 -> 60"""
        return await self.make_request(expression)

    async def arccos(self, expression: str) -> dict:
        """Cosine pi -> -1"""
        return await self.make_request(expression)

    async def arcsin(self, expression: str) -> dict:
        """Inverse Sine 0 -> 0"""
        return await self.make_request(expression)

    async def arctan(self, expression: str) -> dict:
        """Inverse Tangent 0 -> 0"""
        return await self.make_request(expression)

    async def abs(self, expression: str) -> dict:
        """Absolute Value -1 -> 1"""
        return await self.make_request(expression)

    async def log(self, expression: str) -> dict:
        """Logarithm 2l8 -> 3"""
        return await self.make_request(expression)
