# PawPrints API

A python wrapper for the pawprints WebSockets API

## Usage

```python
from pawprints_api import PawPrints

pawprints = PawPrints()

# connect
await pawprints.connect()


try:
	async for data in pawprints.listen():
		# Handle the message as needed
		print(data)
except Exception:
	print('Stopping...')
	await api.disconnect()



petition_id = 3456				
petition_data = pawprints.get_petition(petition_id)

print(petition_data)

await api.disconnect()

```