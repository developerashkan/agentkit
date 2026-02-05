from agentkit.connectors.ingestion import chunk_text
from agentkit.connectors.webhooks import slack_message


def test_slack_payload_format():
    payload = slack_message("alerts", "hello").payload()
    assert payload["platform"] == "slack"


def test_chunk_text_non_empty():
    chunks = chunk_text("abcdefghij", chunk_size=3)
    assert chunks == ["abc", "def", "ghi", "j"]
