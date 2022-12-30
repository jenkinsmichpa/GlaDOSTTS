# Home Assistant Component for a GLaDOSTTS installation.

This is a component for Home Assistant which integrates the TTS engine from https://github.com/R2D2FISH/glados-tts.

# Installation

## HACS
Navigate to the "Integrations" page of HACS on Home Assistant. Click the triple dots and select "Custom repositories". Paste in the GlaDOSTTS repository URL and select the "Integration" category before clicking "ADD". Click the newly shown GLaDOSTTS repository and then "Download". Finally, restart the Home Assistant instance.

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
  - platform: gladostts
    host: <host>
    port: <port>

```
