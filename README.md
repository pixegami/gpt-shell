# GPT Python Shell Wrapper

This is a Python script that interacts with ChatGPT's API to generate responses based on user inputs.

The script allows you to specify prompts for GPT-3 and receive responses from the model. Additionally, the script can be configured to add system prompts, such as formatting responses as Markdown, keeping responses short and concise, and responding sarcastically to user prompts.

## Setting Up

Before running the script, make sure that you have installed the required dependencies, including `argparse` and `openai`.

You will also need an OpenAI API key to use the API. Once you have your API key, export it as an environment variable in your terminal using the following command:

```sh
export OPENAI_API_KEY="sk-XXXX"
```

## Usage

To use the script, navigate to the directory containing the script in your terminal and run it using the following command:

```sh
./gpt.py "prompt"
```

Replace "prompt" with the prompt you want to ask GPT-3. You can also include multiple prompts by separating them with spaces.

The script also supports optional flags for formatting responses as Markdown and enabling verbose mode. To format responses as Markdown, use the "-md" flag. To enable verbose mode, use the "-v" flag.

Once the script is running, you can enter additional prompts to continue chatting with GPT-3. To end the session, enter an empty string.

## Create a Shell Shortcut

To create a shell shortcut for the script, make the script executable using the following command:

```sh
chmod +x gpt.py
```

Then, create an alias in your shell configuration file (e.g. ~/.bashrc or ~/.zshrc) using the following command:

```sh
alias gpt="/path/to/gpt.py"
```

Replace "/path/to" with the path to the directory containing the script.

## References

- [OpenAI API documentation](https://platform.openai.com/docs/guides/chat)
- [Python argparse tutorial](https://docs.python.org/3/howto/argparse.html)
