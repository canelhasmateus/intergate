import requests
from requests import Response

from .domain import Environment, Message


class DiscordApi:

	def __init__(self, environment: Environment):
		self.environment: Environment = environment

	def send_message(self, message: Message) -> Response:
		return requests.post( self.environment.URL, json = message.dict() )
