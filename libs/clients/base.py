from motor.motor_asyncio import AsyncIOMotorClient

from config.api_config import ApiConfig


class BaseClient:
	def __init__(self, loop):
		self.client = AsyncIOMotorClient(
			ApiConfig.MOTOR_URI,
			io_loop=loop
		)

	def __call__(self, *args, **kwargs):
		return self.client
