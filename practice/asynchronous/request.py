import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['http://example.com', 'http://example.org', 'http://example.net']
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for url, response in zip(urls, responses):
            print(f"Response from {url}: {response[:50]}...")

if __name__ == '__main__':
    asyncio.run(main())