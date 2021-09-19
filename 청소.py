import discord, asyncio

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("구사회 채팅청소 시스템 작동완료")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("구사회 시스템"))

@client.event
async def on_message(message):
    if message.content.startswith (">청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="구사회", icon_url="https://cdn.discordapp.com/attachments/885555549041750027/887357915290292254/092a0089f0eb55e8.gif")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODg4ODIyOTY2MDkwMDc2MTcx.YUYS5A.Oi1aIcHxMKvRUVgeag2KGk4Y1uU')