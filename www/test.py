import orm
import asyncio
from models import User

async def test(loop):
	await orm.create_pool(user='root', password='gayboysql', db='awesome', loop=loop)

	u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank')

	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))