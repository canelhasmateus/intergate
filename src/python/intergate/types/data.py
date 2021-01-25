from __future__ import annotations

from pydantic.main import BaseModel


class Immutable( BaseModel ):
	pass

class Mutable( BaseModel ):
	pass
