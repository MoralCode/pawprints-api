import asyncio
import json
import websockets

WEBSOCKET_URL = 'wss://pawprints.rit.edu/ws/'
# WEBSOCKET_URL = 'ws://localhost:8000/ws/'

class PawPrints:
	def __init__(self, endpoint_url=WEBSOCKET_URL):
		self.endpoint_url = endpoint_url
		self.websocket = None

	async def connect(self):
		self.websocket = await websockets.connect(self.endpoint_url)

	async def disconnect(self):
		await self.websocket.close()

	async def send_request(self, request):
		await self.websocket.send(json.dumps(request))
		response = await self.websocket.recv()
		return json.loads(response)

	async def get_petition(self, petition_id):
		request = {'command': 'get', 'id': petition_id}

		response = await self.send_request(request)
		
		return response.get("petition")

	async def listen(self):
		async for message in self.websocket:
			response = json.loads(message)
			# Handle the response as needed, such as for caching
			# maybe turn it into an object
			yield response
