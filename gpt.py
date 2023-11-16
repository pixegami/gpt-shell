#!/usr/bin/env python

"""
A quick and dirty Python script to ask GPT-3 for a prompt and print the response.
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import argparse

SYSTEM_MESSAGE = """
Provide short, concise answers to the user's questions.
"""


def main():
    print("Starting GPT Shell Client ✨")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "prompt", nargs="+", type=str, help="Prompt for GPT-3 to complete"
    )

    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    print(f"Q: {prompt}")

    chat_history = []
    ask_gpt(prompt, chat_history, SYSTEM_MESSAGE)

    user_input = input(">_: ")
    while user_input != "":
        ask_gpt(user_input, chat_history, SYSTEM_MESSAGE)
        user_input = input(">_: ")

    print("Ending Session 👋")


def ask_gpt(prompt: str, chat_history: list, system_message: str):


    user_prompt = {"role": "user", "content": prompt}
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        *chat_history,
        user_prompt,
    ])
    content = response.choices[0].message.content
    chat_history.append(user_prompt)
    chat_history.append({"role": "assistant", "content": content})

    # Print the text in a green color.
    print("\033[92m" + content + "\033[0m")
    return content


if __name__ == "__main__":
    main()
