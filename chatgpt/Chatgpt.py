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

    def get_response(self, message):
        prompt = f"User: {message}\nAI:"
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=10,
                n=1,
                stop=None,
                temperature=0.7,
            )
            message = response.choices[0].text.strip()
            return message
        except Exception as e:
            print(e)
            return e
            #return "Oops! Something went wrong."

def setup(bot):
    cog = TalkToChatGPTCog(bot)
    
