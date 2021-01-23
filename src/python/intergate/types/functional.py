from __future__ import annotations

from typing import Any, TypeVar, Callable

Arg = TypeVar( "Arg" )
Ret = TypeVar( "Ret" )

Thunk = Callable[ [ None ], Ret ]
Function = Callable[ [ Arg ], Ret ]
Closure = Function[ Any, Function[ Arg, Ret ] ]
