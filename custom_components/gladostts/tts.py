"""Support for the GLaDOSTTS speech service."""
import logging

import asyncio
import aiohttp
import re
import async_timeout
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from urllib.parse import quote


_LOGGER = logging.getLogger(__name__)

SUPPORT_LANGUAGES = ["en-US"]

DEFAULT_LANG = "en-US"
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8124

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORT_LANGUAGES),
        vol.Optional(CONF_HOST, default=DEFAULT_HOST): cv.string,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port
    }
)


def get_engine(hass, config, discovery_info=None):
    """Set up GLaDOSTTS speech component."""
    return GLaDOSTTSProvider(hass, config[CONF_LANG], config[CONF_HOST], config[CONF_PORT])


class GLaDOSTTSProvider(Provider):
    """The GLaDOSTTS API provider."""

    def __init__(self, hass, lang, host, port):
        """Initialize GLaDOSTTS provider."""
        self._hass = hass
        self._lang = lang
        self._host = host
        self._port = port
        self.name = "GLaDOSTTS"

    @property
    def default_language(self):
        """Return the default language."""
        return self._lang

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES

    async def async_get_tts_audio(self, message, language, options=None):
        """Load TTS using a GLaDOSTTS server."""
        websession = async_get_clientsession(self._hass)

        try:
            with async_timeout.timeout(30):
                encoded_message = quote(message)
                url = "http://{}:{}/synthesize/{}".format(self._host, self._port, encoded_message)

                request = await websession.get(url)

                if request.status != 200:
                    _LOGGER.error(
                        "Error %d on load url %s", request.status, request.url
                    )
                    return (None, None)
                data = await request.read()

        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Timeout for GLaDOSTTS API")
            return (None, None)

        if data:
            return ("wav", data)
        return (None, None)
