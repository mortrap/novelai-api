from sys import version_info, path
from os.path import join, abspath, dirname
path.insert(0, abspath(join(dirname(__file__), '..')))

from novelai_api import NovelAI_API
from novelai_api.utils import get_encryption_key, decrypt_user_data
from aiohttp import ClientSession

from logging import Logger
from asyncio import run

filename = join("credentials", "creds_example.txt")
with open(filename) as f:
	username, password = f.read().split(',')

logger = Logger("NovelAI")

async def main():
	async with ClientSession() as session:
		api = NovelAI_API(session, logger = logger)

		login = await api.high_level.login(username, password)
		print(login)

		key = get_encryption_key(username, password)
		keystore = await api.high_level.get_keystore(key)
		print(keystore)

		stories = await api.high_level.download_user_stories()
		decrypt_user_data(stories, keystore)
		print(stories)


run(main())