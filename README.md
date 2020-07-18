Async Ipify api\
site: https://api.ipify.org/
# support
```
python 3.7.3 +
aiohttp 3.0 +
```

# use:
```python
from ipify_api import Ipify
import asyncio
async def main():

        f = Ipify(loop= asyncio.get_event_loop())
        print(await f.get_ip())
        # {"ip":"255:255:255:255"}
        f.close()
asyncio.run(main())
```