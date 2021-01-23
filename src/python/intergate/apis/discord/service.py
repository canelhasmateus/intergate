from __future__ import annotations

import requests

from intergate.apis.discord import Message
from intergate.types import URL


class Sender:

	def __init__( self, url: URL ):
		self._url = url

	def __call__( self, message: Message ) -> requests.Response:
		return requests.post( self._url, json = message.dict() )
