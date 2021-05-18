import asyncio
import random

async def call_web_api(url):
    print(f'send a request: {url}')
    await asyncio.sleep(random.random())
    print(f'got a response: {url}')
    return url

async def async_download(url):
    response = await call_web_api(url)
    return response

async def main():
    task = asyncio.gather(
        async_download('https://twitter.com/'),
        async_download('https://facebook.com/'),
        async_download('https://instagram.com/'),
    )
    return await task
    # result = asyncio.run(task)
    # print(f'result={result}')

if __name__ == "__main__":
   result = asyncio.run(main())