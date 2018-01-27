## aionewton

An `asnycio`-based  wrapper for [Newton](https://newton.now.sh).
The Github project can be found [here.](https://github.com/aunyks/newton-api)

## Installation
```
pip install aionewton
```
For the latest development version:
```
pip install git+https://github.com/ilevn/aionewton
```

## Example

```py
import asyncio
from aionewton import AioNewton

# Create a new instance of the API wrapper.
calculate = Aionewton()
loop = asyncio.get_event_loop()

async def main():
    to_calculate = input("Expression: ") # 2^2+2(2)
    # Get calculation for `to_calculate`.
    result = await calculate.simplify(to_calculate)
    # Return a Result object with `operation`, `expression`
    # and `result` as attributes.
    print(result)

loop.run_until_complete(main())
```