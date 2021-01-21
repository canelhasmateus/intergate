from __future__ import annotations

from abc import abstractmethod
# noinspection PyUnresolvedReferences
from typing import Protocol, Optional, T

from pydantic.main import BaseModel

String = str


class Serializable( Protocol[ T ] ):

	@staticmethod
	def get_contents(value: Optional[ Serializable[ T ] ]) -> Optional[ T ]:
		if not value:
			return None

		if isinstance( value, T ):
			return value

		return value.contents

	@property
	@abstractmethod
	def contents(self) -> T:
		raise NotImplemented()


class ImmutableSerializable( BaseModel ):
	class Config:
		arbitrary_types_allowed = True


class MutableSerializable( BaseModel ):
	class Config:
		arbitrary_types_allowed = True


class HttpMethods:
	GET: String = "GET"
	POST: String = "POST"
	HEAD: String = "HEAD"
	OPTIONS: String = "OPTIONS"
	PUT: String = "PUT"
	PATCH: String = "PATCH"
