from __future__ import annotations

from intergate.apis import discord, jira
from intergate.types import URL


class Assets:
	LOGO_JIRA: URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLT_6JKK6ca5KZEg2BwsBXMZdggGvHEFFB3g&usqp=CAU"
	ICON_ATLASSIAN: URL = "https://symbols.getvecta.com/stencil_85/33_jira-icon.6a60be29f8.png"


class MessageFactory( discord.pointcut.MessageFactory[ jira.Event ] ):

	def to_content( self, payload: jira.Event ):
		return None

	def to_author( self, payload: jira.Event ):
		return None

	def to_thumbnail( self, payload: jira.Event ):
		return discord.Image( url = Assets.LOGO_JIRA )

	def to_field_list( self, payload: jira.Event ):
		# TODO  22/01/2021 mentions
		return [ ]

	def to_footer( self, payload: jira.Event ):
		return discord.Footer(
				text = f" [{payload.fieldDict.status.name}] {payload.key} ",
				icon_url = Assets.ICON_ATLASSIAN
				)

	def to_title( self, payload: jira.Event ):
		return f"[JIRA] {payload.fieldDict.project.name}"

	def to_url( self, payload: jira.Event ):
		return None

	def to_color( self, payload: jira.Event ):
		return None

	def to_description( self, payload: jira.Event ):
		return None
