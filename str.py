import asyncio

from pyrogram import Client as Yonebot


print("Enter your app information from my.telegram.org/apps below.")


async def main():
    async with Yonebot(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
