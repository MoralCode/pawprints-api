# PawPrints WebSockets API

The PawPrints frontend communicates with the backend over WebSockets.

The WebSockets URL for PawPrints is `wss://pawprints.rit.edu/ws/`

This is primarily used to fetch PawPrint data and receive near-realtime updates on votes, responses, and new petitions.

<!-- ## Authentication -->

## Message Format

WebSockets messages are formatted as JSON objects.

These messages (both requests and responses) generally contain at least a top-level "command" key that specifies what action should be (or was) taken. Here is an example of an outgoing "all" command.

`{"command":"all"}`


These messages often (but dont always) contain additional data depending on the type of command being used, for example, the response to the command above returns data that looks something like this:

`{"petitions": [<...>], "map": {...}}`


## Requests
There are a few kinds of requests that are able to be sent by clients

### paginate
This is used on initial page load to fetch the first (and subsequent) pages of PawPrints data as you scroll. 

The data that gets sent when this happens is `{"command":"paginate","sort":"most recent","filter":"all","page":1}`

### all

sending:
`{"command":"all"}`

returns EVERYTHING

### get
fetches a pawprint 
`{'command': 'get', 'id': petition_id}`


## Responses
possible commands handled by the UI

### update-sigs
`{'command': 'update-sigs', 'sigs': 20, 'petition_id': 3806}`

### new-update

### new-response
`{'command': 'new-response', 'response': {'description': '[...]', 'timestamp': 'March 07, 2023', 'author': 'Trishelle Hoopes', 'petition_id': 3629}}`

### get



### new-petition
`{'command': 'new-petition', 'petition': {'petition_id': '3846'}}`

### remove-petition
### mark-in-progress
`{'command': 'mark-in-progress', 'petition': {'petition_id': '3665'}}`
this was reveived before the new-update was received
### refresh-petition
### paginate
### all

`{"petitions": [<...>], "map": {...}}`