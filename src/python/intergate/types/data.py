from __future__ import annotations

from pydantic.main import BaseModel


class Immutable( BaseModel ):
	class Config:
		arbitrary_types_allowed = True


class Mutable( BaseModel ):
	class Config:
		arbitrary_types_allowed = True
