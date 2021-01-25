from __future__ import annotations

from enum import Enum
from typing import Optional, List
import pydantic
from pydantic.main import BaseModel
import requests

from intergate.types.alias import String, URL, Integer, Boolean, Isotime, HexColor
from intergate.types.data import Immutable
from intergate.types.functional import Function


class Footer( Immutable ):
	text: String
	icon_url: Optional[ URL ]


class Image( Immutable ):
	url: Optional[ String ]
	height: Optional[ Integer ]
	width: Optional[ Integer ]


class Field( Immutable ):
	name: String
	value: Optional[String]
	inline: Optional[ Boolean ] = True


class Author( Immutable ):
	name: Optional[ String ]
	icon_url: Optional[ URL ]


class EmbedTypes( Enum ):
	RICH = "rich"


class Embed( BaseModel ):
	title: Optional[ String ] = None
	description: Optional[ String ] = None
	type: Optional[ String ] = EmbedTypes.RICH.value
	url: Optional[ URL ] = None

	timestamp: Optional[ Isotime ] = None
	color: Optional[ HexColor ] = None

	footer: Optional[ Footer ] = None
	image: Optional[ Image ] = None
	thumbnail: Optional[ Image ] = None
	author: Optional[ Author ] = None
	fieldList: List[ Field ] = pydantic.Field

class DiscordMessage( Immutable ):
	content: Optional[ String ] = None
	embeds: List[ Embed ] = [ ]


DiscordMessager = Function[ DiscordMessage, requests.Response ]
