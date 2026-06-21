"""Example: ultra-scraper with Anthropic tool use."""

import anthropic
import json
from ultra_scraper import get_anthropic_tools, handle_anthropic_tool_use

client = anthropic.Anthropic()
tools = get_anthropic_tools()

messages = [
    {"role": "user", "content": "Scrape https://news.ycombinator.com and give me the top 5 story titles."}
]

# Agentic loop
while True:
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        tools=tools,
        messages=messages,
    )

    if response.stop_reason == "end_turn":
        for block in response.content:
            if hasattr(block, "text"):
                print(block.text)
        break

    if response.stop_reason == "tool_use":
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = handle_anthropic_tool_use(block)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })
        messages.append({"role": "user", "content": tool_results})
