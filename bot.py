import discord
import google
from google import genai
from google.genai import types
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
import os
import dotenv

# there is environment variables for docker and ease of use
dotenv.load_dotenv()
# You need a discord app api key and a gemini api key (both are free, gemini api has limits on free tier)
tool = os.getenv("DISCORD_TOKEN") 
client = os.getenv("GEMINI_TOKEN")
sys_string = os.getenv("SYS_INS")

system_instruction_combined_string="""

        """
# you can add sys instructions for gemini here (recommended: Keep all responses 1500 characters or less)

bot = commands.Bot()

@bot.slash_command(name='text', description='Ask Gemini whatever')# slash command
async def ai(ctx: discord.ApplicationContext, question: str = Option(str, description="Ask Gemini whatever")):# defines function, description and input box
   gtool = types.Tool(
    google_search=types.GoogleSearch()
   )# this is a config allowing gemini to connect to google when needed (base gemini is outdated)
   await ctx.defer() # required as discord requires a 3 second reponse time without this
   resp = client.models.generate_content(
    model="gemini-2.5-flash", contents=question, # uses 2.5-flash, contents are the "question" inout box above
    config=genai.types.GenerateContentConfig(
        system_instruction=system_instruction_combined_string, # connects to the sys instruction variable at line 12
        tools=[gtool] # connects to the config variable above in this function
    )
   )
   outs = f"You asked: {question}\n {resp.text}" # returns user's question and ai response
   await ctx.respond(outs) # prints above


bot.run(tool) # runs bot with discord api key in the 'tool' var at line 8
