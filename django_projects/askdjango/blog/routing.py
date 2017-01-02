from channels import route
from blog import consumers

url_pattern = r'^(?P<post_pk>\d+)/stream/$'

channel_routing = [
    route('websocket.connect', consumers.ws_connect, path=url_pattern),
    route('websocket.receive', consumers.ws_message, path=url_pattern),
    route('websocket.disconnect', consumers.ws_disconnect, path=url_pattern),
]
