"""Example: ultra-scraper with OpenAI function calling."""

from openai import OpenAI
import json
from ultra_scraper import get_openai_tools, handle_openai_tool_call

client = OpenAI()
tools = get_openai_tools()

messages = [
    {"role": "user", "content": "Scrape https://news.ycombinator.com and give me the top 5 story titles."}
]

# First call — let agent decide to use the tool
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
)

# Handle tool call
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    result = handle_openai_tool_call(tool_call)

    messages.append(response.choices[0].message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    })

    # Final response
    final = client.chat.completions.create(model="gpt-4o", messages=messages)
    print(final.choices[0].message.content)
