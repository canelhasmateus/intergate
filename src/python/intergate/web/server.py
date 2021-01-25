from __future__ import annotations

from typing import Dict

import flask
import requests

from intergate.apis.discord.domain import DiscordMessager, DiscordMessage
from intergate.apis.discord.service import DiscordSenderClosure
from intergate.apis.github.domain import ReleaseEvent
from intergate.apis.jira.domain import JiraEvent, CommentEvent, TransitionEvent
from intergate.types.alias import Integer, URL
from intergate.types.functional import Function
from intergate.types.http import HttpMethods
from intergate.web.aspects.github.discord import GithubMessageClosure
from intergate.web.aspects.jira.discord import JiraMessageClosure


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
		self.send_message: DiscordMessager = DiscordSenderClosure( self.discordUrl )
		self.to_github_message: Function[ Dict, DiscordMessage ] = GithubMessageClosure()
		self.to_jira_message: Function[ Dict, DiscordMessage ] = JiraMessageClosure()

		@self.app.route( '/github', methods = [ HttpMethods.POST.value ] )
		def github_listen() -> flask.Response:
			response: requests.Response = (
					self.send_message(
							self.to_github_message(
									ReleaseEvent( **flask.request.json ) ) )
			)

			return flask.Response( response )

		@self.app.route( "/jira", methods = [ HttpMethods.POST.value ] )
		def jira_listen() -> flask.Response:
			response: requests.Response = (
					self.send_message(
							self.to_jira_message(
									JiraEvent( **flask.request.json ) ) )
			)
			return flask.Response( response )

		@self.app.route( "/jira/comment", methods = [ HttpMethods.POST.value ] )
		def jira_comment() -> flask.Response:
			response: requests.Response = (
					self.send_message(
							self.to_jira_message(
									CommentEvent( **flask.request.json ) ) )
			)
			return flask.Response( response )

		@self.app.route( "/jira/transition", methods = [ HttpMethods.POST.value ] )
		def jira_transition() -> flask.Response:
			response: requests.Response = (
					self.send_message(
							self.to_jira_message(
									TransitionEvent( **flask.request.json ) ) )
			)
			return flask.Response( response )



if __name__ == "__main__":
	Webserver( 80, "", "" )()
