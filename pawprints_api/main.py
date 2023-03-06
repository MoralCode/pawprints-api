import json
import websockets

WEBSOCKET_URL = 'wss://pawprints.rit.edu/ws/'
# WEBSOCKET_URL = 'ws://localhost:8000/ws/'

class PawPrints:
    def __init__(self, endpoint_url=WEBSOCKET_URL, auth_token=None):
        self.endpoint_url = endpoint_url
        self.auth_token = auth_token
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect(self.endpoint_url)
        if self.auth_token is not None:
            await self.websocket.send(json.dumps({'auth': self.auth_token}))

    async def disconnect(self):
        await self.websocket.close()

    async def send_request(self, request):
        await self.websocket.send(json.dumps(request))
        response = await self.websocket.recv()
        return json.loads(response)

    async def get_ticker(self, symbol):
        request = {
            'method': 'ticker',
            'params': {
                'symbol': symbol
            }
        }
        return await self.send_request(request)

    async def get_order_book(self, symbol, limit):
        request = {
            'method': 'orderbook',
            'params': {
                'symbol': symbol,
                'limit': limit
            }
        }
        return await self.send_request(request)

