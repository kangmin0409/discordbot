import discord
from discord import app_commands
import requests
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user}이 시작되었습니다')  #  봇이 시작하였을때 터미널에 뜨는 말
        game = discord.Game('봇')          # ~~ 하는중
        await self.change_presence(status=discord.Status.online, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name = '안녕', description='인사를 합니다!')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"안녕하세요!", ephemeral = False)

@tree.command(name='날씨', description='세계의 날씨를 알려줍니다!')
async def slash3(interaction: discord.Interaction, *, location: str):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=token&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        message = f'현재 {location}의 날씨 정보:\n' \
                  f'날씨: {weather_description}\n' \
                  f'온도: {temperature}°C\n' \
                  f'습도: {humidity}%\n' \
                  f'풍속: {wind_speed} m/s'
    else:
        message = f'{location}의 날씨 정보를 가져오지 못했습니다. 영어만 지원합니다.'

    await interaction.response.send_message(message, ephemeral = False)

@tree.error
async def slash3(ctx,error):
    await ctx.response.send_message(f"오류가 발생했습니다!", ephemeral = True)


client.run('token')
