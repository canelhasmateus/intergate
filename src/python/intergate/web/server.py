from __future__ import annotations

from typing import Dict

import flask
import requests

from intergate.apis import discord, github, jira
from intergate.types import Integer, URL, HttpMethods, Function
from intergate.web import aspects


class Webserver:

	def __call__( self ):
		self.app.run( port = self.port )

	# TODO  23/01/2021 remove these URL arguments
	def __init__( self, port: Integer, discordUrl: URL = None, jiraDomain: URL = None ):
		self.port = port
		self.app = flask.Flask( __name__ )
		self.jiraDomain = jiraDomain
		self.discordUrl = discordUrl

		# TODO  23/01/2021 make these methods easily over-rideable
		self.send_message: discord.Messager = discord.Sender( self.discordUrl )
		self.to_github_message: Function[ Dict, discord.Message ] = aspects.github.discord.MessageFactory()
		self.to_jira_message: Function[ Dict, discord.Message ] = aspects.jira.discord.MessageFactory()

		@self.app.route( '/github', methods = [ HttpMethods.POST.value ] )
		def github_listen() -> flask.Response:
			response: requests.Response = (
					self.send_message(
							self.to_github_message(
									github.ReleaseEvent( **flask.request.json ) ) )
			)

			return flask.Response( response )

		@self.app.route( "/jira", methods = [ HttpMethods.POST.value ] )
		def jira_listen() -> flask.Response:
			response: requests.Response = (
					self.send_message(
							self.to_jira_message(
									jira.Event( **flask.request.json ) ) )
			)
			return flask.Response( response )


if __name__ == "__main__":
	Webserver( 80, "", "" )()
