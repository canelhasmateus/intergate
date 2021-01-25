from __future__ import annotations

import requests

from intergate.apis.discord.domain import DiscordMessage
from intergate.types.alias import URL


class DiscordSenderClosure:

	def __init__( self, url: URL ):
		self._url = url

	def __call__( self, message: DiscordMessage ) -> requests.Response:
		req = message.dict()
		#TODO  25/01/2021 deal with this migué
		req['embeds'][0]['fields'] = req['embeds'][0]['fieldList']
		return requests.post( self._url, json = req )
