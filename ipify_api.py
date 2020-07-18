from typing import Optional, Dict
from aiohttp_socks import SocksConnector

import asyncio
import aiohttp


class Ipify:
    def __init__(self, loop: asyncio.AbstractEventLoop, session: Optional[aiohttp.ClientSession] = None) -> None:
        """

        @param loop:
        @param session:
        """
        self.loop = loop
        self.session = session if session is not None else self.loop.run_until_complete(self.open_session())
        self.url: str = "https://api.ipify.org/?format=json"

    async def open_session(self, proxy: str = None) -> aiohttp.ClientSession:
        """
        @param proxy:
        @return:
        """
        if proxy is None:
            session = aiohttp.ClientSession()
            return session
        connector = SocksConnector.from_url(proxy)
        session = aiohttp.ClientSession(connector=connector)
        return session

    def close(self):
        """

        @return:
        """
        self.loop.run_until_complete(self.session.close())

    async def get_ip(self) -> Dict[str, str]:
        """

        @return:
        """
        async with self.session.get(self.url) as response:
            return await response.json()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    test = Ipify(loop=loop)
    loop.run_until_complete(test.get_ip())
    test.close()
