from __future__ import annotations

import os
from typing import Optional, List

from ..common import ImmutableSerializable, MutableSerializable

String = str
URL = String
Integer = int
Color = Integer
Timestamp = object
Boolean = bool


class EmbedTypes:
	RICH: String = "rich"


class Footer( ImmutableSerializable ):
	text: String
	icon_url: Optional[ URL ]


class Image( ImmutableSerializable ):
	url: Optional[ String ]
	height: Optional[ Integer ]
	width: Optional[ Integer ]


class Thumbnail( ImmutableSerializable ):
	url: Optional[ URL ]
	height: Optional[ Integer ]
	width: Optional[ Integer ]


class Field( ImmutableSerializable ):
	name: String
	value: String
	inline: Optional[ Boolean ]


class Author( ImmutableSerializable ):
	name: Optional[ String ]
	icon_url: Optional[ URL ]


class Embed( ImmutableSerializable ):
	title: Optional[ String ] = None
	description: Optional[ String ] = None
	type: Optional[ String ] = EmbedTypes.RICH
	url: Optional[ URL ] = None
	timestamp: Optional[ Timestamp ] = None
	color: Optional[ Color ] = None

	footer: Optional[ Footer ] = None
	image: Optional[ Image ] = None
	thumbnail: Optional[ Thumbnail ] = None
	author: Optional[ Author ] = None
	fieldList: Optional[ List[ Field ] ] = None

	class Config:
		fields = { "fieldList": "field" }


class Message( MutableSerializable ):
	content: Optional[ String ] = None
	embeds: List[ Embed ] = [ ]


class Environment( ImmutableSerializable ):
	URL: String = os.environ.get( "DISCORD_URL", "" )
