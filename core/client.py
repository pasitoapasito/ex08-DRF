import aiohttp, time, asyncio


async def async_fetcher(session, url):
    async with session.get(url) as response:
        return await response.json()

async def async_func():
    urls = ['http://localhost:8000/api'] * 150

    """
    aiohttp: 비동기적 요청 라이브러리 활용(비동기적 요청을 동시성으로 처리)
    """
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[async_fetcher(session, url) for url in urls])

        print(result)
        return result


if __name__ == "__main__":
    async_start = time.time()
    asyncio.run(async_func())
    async_end = time.time()

    print(f"쿠폰 이벤트 결과: {async_end - async_start}")
