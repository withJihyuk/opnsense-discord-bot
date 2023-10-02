import discord
import opnsence
import config

# 편의를 위해 모두 허용 하였으나, 필요시 수정 후 사용하시면 됩니다.
intents = discord.Intents.all()
client = discord.Client(intents= intents)

@client.event
async def on_ready():
  print("(사명) | 방화벽 관리용 봇이 정상적으로 실행 되었습니다.")
  await client.wait_until_ready()

@client.event
async def on_message(message: discord.Message):

  if message.content.startswith("!port"):
    vm_ip = message.content.split()[1]
    inport = message.content.split()[2]   
    with open("port.txt", "r") as f:
       number = str(f.read())
       f.close()

    with open("port.txt", "w") as f:
       new_number = int(number) + 1
       f.write(str(new_number))

    try:
      opnsence.AddRule(str(vm_ip), int(number), int(inport), str("bot"))
    except Exception as e:
       print(e)
       await message.channel.send("처리 중 오류가 발생했습니다. (오류: 예외적인 오류가 발생 하였습니다.)")
       return
    await message.channel.send(f"내부 {inport} 포트 -> 외부 %s 포트")
  

# 봇을 실행합니다.
client.run(config.token)
