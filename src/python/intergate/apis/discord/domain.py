from __future__ import annotations

from enum import Enum
from typing import Optional, List

import requests

from intergate.types import (Immutable, URL,
                             Integer, String, Boolean, Isotime, HexColor, Function,
                             )


class Footer( Immutable ):
	text: String
	icon_url: Optional[ URL ]


class Image( Immutable ):
	url: Optional[ String ]
	height: Optional[ Integer ]
	width: Optional[ Integer ]


class Field( Immutable ):
	name: String
	value: String
	inline: Optional[ Boolean ]


class Author( Immutable ):
	name: Optional[ String ]
	icon_url: Optional[ URL ]


class EmbedTypes( Enum ):
	RICH = "rich"


class Embed( Immutable ):
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
	fieldList: Optional[ List[ Field ] ] = None

	class Config:
		fields = { "fieldList": "field" }


class Message( Immutable ):
	content: Optional[ String ] = None
	embeds: List[ Embed ] = [ ]


Messager = Function[ Message, requests.Response ]