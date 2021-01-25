from __future__ import annotations

from typing import List, Optional

from intergate.apis.discord.domain import Author, Image, Footer, Field
from intergate.apis.discord.pointcut import DiscordMessageFunction
from intergate.apis.github.domain import GithubEvent
from intergate.types.alias import URL, String, Integer


class GithubAssets:
	LOGO_GITHUB: URL = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
	ICON_BRANCH: URL = "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png"


class GithubMessageFunction( DiscordMessageFunction[ GithubEvent ] ):

	def to_title( self, payload: GithubEvent ) -> Optional[ String ]:
		return f"{payload.action}"

	def to_thumbnail( self, payload: GithubEvent ) -> Optional[ Image ]:
		return Image( url = GithubAssets.LOGO_GITHUB )

	def to_description( self, payload: GithubEvent ) -> Optional[ String ]:
		return None

	def to_author( self, payload: GithubEvent ) -> Optional[ Author ]:
		return None

	def to_url( self, payload ) -> Optional[ URL ]:
		return None

	def to_color( self, payload ) -> Optional[ Integer ]:
		return None

	def to_content( self, payload ) -> Optional[ String ]:
		return None

	def to_footer( self, payload ) -> Optional[ Footer ]:
		return None

	def to_field_list( self, payload ) -> List[ Field ]:
		return [ ]
