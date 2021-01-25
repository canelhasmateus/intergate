import abc
from typing import Generic, List, Optional, T

from intergate.apis.discord import domain as discord
from intergate.apis.discord.domain import Embed
from intergate.types.alias import String, URL, Integer


class DiscordMessageClosure( Generic[ T ] ):

	def __call__( self, payload: T ) -> discord.DiscordMessage:
		content = self.to_content( payload )
		embedList = self.to_embed_list( payload )
		return discord.DiscordMessage( content = content,
				embeds = embedList )

	def to_embed_list( self, payload: T ) -> List[ discord.Embed ]:
		title: Optional[ String ] = self.to_title( payload )
		author: Optional[ discord.Author ] = self.to_author( payload )
		thumb: Optional[ discord.Image ] = self.to_thumbnail( payload )
		fieldList: List[ discord.Field ] = self.to_field_list( payload )
		footer: Optional[ discord.Footer ] = self.to_footer( payload )
		url: Optional[ URL ] = self.to_url( payload )
		color: Optional[ Integer ] = self.to_color( payload )
		description: Optional[ String ] = self.to_description( payload )
		embed: Embed = Embed( author = author,
				title = title, url = url, thumbnail = thumb,
				description = description,
				fieldList = fieldList,
				color = color,
				footer = footer
				)
		return [ embed ]

	@abc.abstractmethod
	def to_author( self, payload: T ) -> Optional[ discord.Author ]:
		raise NotImplemented

	@abc.abstractmethod
	def to_thumbnail( self, payload: T ) -> Optional[ discord.Image ]:
		raise NotImplemented

	@abc.abstractmethod
	def to_field_list( self, T ) -> List[ discord.Field ]:
		raise NotImplemented

	@abc.abstractmethod
	def to_footer( self, payload: T ) -> Optional[ discord.Footer ]:
		raise NotImplemented

	@abc.abstractmethod
	def to_title( self, payload: T ) -> Optional[ String ]:
		raise NotImplemented

	@abc.abstractmethod
	def to_url( self, payload: T ) -> Optional[ URL ]:
		raise NotImplemented

	@abc.abstractmethod
	def to_color( self, payload: T ) -> Integer:
		raise NotImplemented

	@abc.abstractmethod
	def to_description( self, payload: T ) -> Optional[ String ]:
		raise NotImplemented

	@abc.abstractmethod
	def to_content( self, payload: T ) -> Optional[ String ]:
		raise NotImplemented
