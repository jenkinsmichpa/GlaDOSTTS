# Home Assistant Component for a GLaDOSTTS installation.

This is a component for Home Assistant which integrates the TTS engine from https://github.com/R2D2FISH/glados-tts.

# Installation

## Manual way
To use it, copy the `gladostts` folder inside your `config/custom_components` folder on your home assistant installation first.

# Configuration

Add following config to your yaml if you are running the GLaDOSTTS engine on the same machine

```yaml
tts:
  - platform: gladostts

```
The integration will connect to GlaDOSTTS after an Home Assistant restart.

## Other host

For setting an external host and specified port:

```yaml
tts:
  - platform: gladostts_remote
    host: <host>
    port: <port>

```
