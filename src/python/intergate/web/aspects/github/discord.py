from __future__ import annotations

from typing import List, Optional

from intergate.apis import github, discord
from intergate.types import URL, String, Integer


class Assets:
	LOGO_GITHUB: URL = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
	ICON_BRANCH: URL = "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png"


class MessageFactory( discord.pointcut.MessageFactory[ github.Event ] ):

	def to_title( self, payload: github.Event ) -> Optional[ String ]:
		return f"[Github] {payload.action}"

	def to_thumbnail( self, payload: github.Event ) -> Optional[ discord.Image ]:
		return discord.Image( url = Assets.LOGO_GITHUB )

	def to_description( self, payload: github.Event ) -> Optional[ String ]:
		return None

	def to_author( self, payload: github.Event ) -> Optional[ discord.Author ]:
		return None

	def to_url( self, payload ) -> Optional[ URL ]:
		return None

	def to_color( self, payload ) -> Optional[ Integer ]:
		return None

	def to_content( self, payload ) -> Optional[ String ]:
		return None

	def to_footer( self, payload ) -> Optional[ discord.Footer ]:
		return None

	def to_field_list( self, payload ) -> List[ discord.Field ]:
		return [ ]
