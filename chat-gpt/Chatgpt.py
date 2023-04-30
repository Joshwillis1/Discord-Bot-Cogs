# Chat-gpt
from redbot.core import commands
import openai
import discord
from discord.ext import commands
import asyncio

class chatgpt(commands.Cog):
    """Chat-gpt"""

    def __init__(self, bot):
        self.bot = bot

    #main function
    class ChatCog(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            openai.api_key = "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" # Replace with your OpenAI API key

    @commands.command()
    async def chat(self, ctx, *, message):
        response = self.get_response(message)
        await ctx.send(response)

    def get_response(self, message):
        model_engine = "text-davinci-002" # Replace with the OpenAI model engine you want to use
        prompt = f"Conversation with ChatGPT:\nUser: {message}\nChatGPT:"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
    
