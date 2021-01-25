from __future__ import annotations

import requests

from intergate.apis.discord.domain import DiscordMessage
from intergate.types.alias import URL


class DiscordSenderClosure:

	def __init__( self, url: URL ):
		self._url = url

	def __call__( self, message: DiscordMessage ) -> requests.Response:
		return requests.post( self._url, json = message.dict() )
