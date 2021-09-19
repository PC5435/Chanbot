import discord, asyncio, pytz, datetime

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("봇이 정상적으로 실행 되었습니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("시스템 작동중 .."))

@client.event
async def on_message(message):
    if message.content == "별빛이형": # 메세지 감지
        await message.channel.send ("{} | {}, 일해".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, 빨리 일해".format(message.author, message.author.mention))

    if message.content.startswith (">공지"):
        await message.delete()
        if message.author.guild_permissions.administrator:
            notice = message.content[4:]
            channel = client.get_channel(884768806126374912)
            embed = discord.Embed(title="**공지사항**", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="유찬이#4197 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/815575609785843732/889131152831565834/976dfc828e50279e65798001ce25ca49.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/815575609785843732/889131152831565834/976dfc828e50279e65798001ce25ca49.png")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        else:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODg4ODIyOTY2MDkwMDc2MTcx.YUYS5A.Oi1aIcHxMKvRUVgeag2KGk4Y1uU')
