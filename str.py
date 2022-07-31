# Creator Or Dev @HYPER_AD13 | @ShiningOff <Found On telegram>
# Found on github < https://github.com/ItsmeHyper13 >

import asyncio

from pyrogram import Client as cl

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

si = cl(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await si.start()
    ss = await si.export_session_string()
    print(f"\n{ss}\n")


asyncio.run(main())
