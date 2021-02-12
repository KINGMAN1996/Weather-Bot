################
#استدعاء المكتبات #
###############
import discord
import aiohttp
import json
import requests
from discord.ext.commands import Bot
from discord.ext import commands
################
#استدعاء المكتبات #
###############

##################
#البريفكس مع الريدي #
##################
clinet = commands.Bot(command_prefix = ".")
@clinet.event
async def on_ready():
    print("KM Codes")
##################
#البريفكس مع الريدي #
##################


####################
#الامر الخاص بالحالةالجوية#
####################
@clinet.command()
async def w(ctx, arg1):
    async with aiohttp.ClientSession() as session:
        apiurl = f"http://api.weatherstack.com/current?access_key=82658b49a57b43e125c050225d48c55c&query={arg1}"#<==ضع api الخاص بالطقس هنا
        r = requests.get(apiurl)
        kingman = json.loads(r.text)
        city = kingman['request']['query']
        localtime = kingman['current']['observation_time']#كود استخراج الوقت
        wind_speed = kingman['current']['wind_speed']#كود سرعة الرياح
        wind_degree = kingman['current']['wind_degree']#كود درجة الرياح
        temperature = kingman['current']['temperature']#كود درجة الحرارة
        weather_icons = kingman['current']['weather_icons'][0]#كود الايقونة
        weather_descriptions = kingman['current']['weather_descriptions'][0]#كود وصف الحالة الجوية
        humidity = kingman['current']['humidity']#كود درجة الرطوبة
        print(city)
        print(localtime)
        print(wind_speed)
        print(wind_degree)
        print(temperature)
        print(weather_icons)
        print(weather_descriptions)
        print(humidity)
        ##############
        #كود رسالة الامبد#
        ##############
        embed=discord.Embed(title="درجة الحرارة", description=f"{temperature}", color=0x31364c)
        embed.set_author(name="Weather Bot By KM Codes", icon_url=f"{weather_icons}")
        embed.add_field(name="سرعة الرياح", value=f"{wind_speed}", inline=True)
        embed.add_field(name="درجة الرياح ", value=f"{wind_degree}", inline=True)
        embed.add_field(name="وصف الحالة الجوية ", value=f"{weather_descriptions}", inline=True)
        embed.add_field(name="معدل الرطوية ", value=f"{humidity}", inline=True)
        embed.set_footer(text=f"Time Now in this city is {localtime}")
        await ctx.send(embed=embed)
####################
#الامر الخاص بالحالةالجوية#
####################

#####################
#امر تسجيل الدخول     #
#####################
clinet.run("YourBotTokenHere")
