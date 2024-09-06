import asyncio
import aiohttp

async def fetch_example_com(session):
    url = 'http://example.com'
    async with session.get(url) as response:
        return await response.text()

async def fetch_example_org(session):
    url = 'http://example.org'
    async with session.get(url) as response:
        data = await response.text()
        return data

async def fetch_example_net(session):
    url = 'http://example.net'
    async with session.get(url) as response:
        data = await response.text()
        return data
    # POST
    # async with session.post(url, data={'key': 'value'}) as response:
    #     return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_example_com(session),
            fetch_example_org(session),
            fetch_example_net(session)
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for func, result in zip([fetch_example_com, fetch_example_org, fetch_example_net], results):
            if isinstance(result, Exception):
                print(f"Error in {func.__name__}: {result}")
            else:
                print(f"Result from {func.__name__}: {result[:50]}...")

if __name__ == '__main__':
    asyncio.run(main())