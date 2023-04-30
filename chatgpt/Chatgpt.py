# Chat-gpt
import discord
from redbot.core import commands
from redbot.core.bot import Red
import openai
import os
import asyncio
import logging


class TalkToChatGPTCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.prev_ai_message = None
        self.logger = logging.getLogger("chat_gpt_logger")

        # set the logger level
        self.logger.setLevel(logging.DEBUG)

        # create a file handler
        handler = logging.FileHandler("chat_gpt.log")

        # set the formatter for the handler
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)

        # add the handler to the logger
        self.logger.addHandler(handler)

    @commands.command()
    async def talk(self, ctx, *, message):
        response = self.get_response(message, self.prev_ai_message)
        if isinstance(response, tuple):
            error_message = response[1]
            await ctx.send(error_message)
            self.logger.error(error_message)
        else:
            await ctx.send(response)
            self.logger.info(f"User: {message}\nAI: {response}")
            self.prev_ai_message = response

    def get_response(self, message, prev_ai_message=None):
        user_prompt = f"User: {message}"
        ai_prompt = f"AI: {prev_ai_message}\n" if prev_ai_message else "AI:"
        prompt = f"{ai_prompt}\n{user_prompt}"
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.7,
            )
            ai_message = response.choices[0].text.strip()

            return ai_message
        except Exception as e:
            self.logger.error(str(e))
            return e

    @commands.command()
    async def chat(self, ctx):
        await ctx.send("Hi! I'm ChatGPT, a language model trained by OpenAI. Let's chat! Type 'exit' to end the chat.")
        prev_ai_message = None
        while True:
            try:
                user_input = await self.bot.wait_for(
                    "message",
                    check=lambda message: message.author == ctx.author and message.channel == ctx.channel,
                    timeout=60.0,
                )
                if user_input.content.lower() == "exit":
                    await ctx.send("Goodbye!")
                    self.logger.info("User: exit\nAI: Goodbye!")
                    break
                response = self.get_response(user_input.content, prev_ai_message)
                prev_ai_message = response.split("\n")[-1].strip()  # get last AI message
                await ctx.send(f"AI: {response}")
                self.logger.info(f"User: {user_input.content}\nAI: {response}")
            except asyncio.TimeoutError:
                await ctx.send("Sorry, I didn't receive any message in the last 60 seconds. The chat has ended.")
                self.logger.info("TimeoutError: The chat has ended.")
                break

def setup(bot):
    cog = TalkToChatGPTCog(bot)