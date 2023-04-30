# Chat-gpt
import discord
from redbot.core import commands
from redbot.core.bot import Red
import openai
import os
import asyncio


class TalkToChatGPTCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.api_key

    @commands.command()
    async def talk(self, ctx, *, message):
        response = self.get_response(message)
        if isinstance(response, tuple):
            error_message = response[1]
            await ctx.send(error_message)
        else:
            await ctx.send(response)

    def get_response(self, message, prev_ai_message=None):
        user_prompt = f"User: {message}"
        ai_prompt = f"AI: {prev_ai_message}\n" if prev_ai_message else "AI:"
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=user_prompt,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.7,
            )
            ai_message = response.choices[0].text.strip()

            response = openai.Completion.create(
                engine="davinci",
                prompt=ai_prompt,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.7,
            )
            ai_message += "\n" + response.choices[0].text.strip()

            return ai_message
        except Exception as e:
            print(e)
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
                    break
                response = self.get_response(user_input.content, prev_ai_message)
                prev_ai_message = response.split("\n")[-1].strip()  # get last AI message
                await ctx.send(f"AI: {response}")
            except asyncio.TimeoutError:
                await ctx.send("Sorry, I didn't receive any message in the last 60 seconds. The chat has ended.")
                break

def setup(bot):
    cog = TalkToChatGPTCog(bot)
    
