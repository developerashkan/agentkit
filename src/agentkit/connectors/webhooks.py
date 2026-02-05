"""Pre-built webhook connector payload builders."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class WebhookMessage:
    platform: str
    channel: str
    text: str

    def payload(self) -> dict[str, str]:
        return {"platform": self.platform, "channel": self.channel, "text": self.text}


def slack_message(channel: str, text: str) -> WebhookMessage:
    return WebhookMessage(platform="slack", channel=channel, text=text)


def teams_message(channel: str, text: str) -> WebhookMessage:
    return WebhookMessage(platform="teams", channel=channel, text=text)


def discord_message(channel: str, text: str) -> WebhookMessage:
    return WebhookMessage(platform="discord", channel=channel, text=text)
