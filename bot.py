
import os
import logging
import discord
from discord import app_commands

# ---- Config ----
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", "0")) or None

# Minimal logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# Intents: required for presence/member status
intents = discord.Intents.default()
intents.members = True       # Server Members Intent (enable in Dev Portal)
intents.presences = True     # Presence Intent (enable in Dev Portal)
intents.message_content = False

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user} (ID: {client.user.id})")
    try:
        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            await tree.sync(guild=guild)
            logging.info(f"Synced commands to guild {GUILD_ID}")
        else:
            await tree.sync()
            logging.info("Synced commands globally (may take up to ~1h)")
    except Exception as e:
        logging.exception(f"Failed to sync commands: {e}")

@tree.command(name="online", description="Show how many members are online in this server.")
@app_commands.checks.cooldown(1, 5.0)
async def online(interaction: discord.Interaction):
    guild = interaction.guild
    if guild is None:
        await interaction.response.send_message(
            "Use this command in a server.", ephemeral=True
        )
        return

    online = idle = dnd = offline = 0
    for member in guild.members:
        status = member.status
        if status is discord.Status.online:
            online += 1
        elif status is discord.Status.idle:
            idle += 1
        elif status is discord.Status.dnd:
            dnd += 1
        else:
            offline += 1

    total = guild.member_count or (online + idle + dnd + offline)

    msg = (
        f"**{guild.name}** status:\n"
        f"🟢 Online: {online}\n"
        f"🌙 Idle: {idle}\n"
        f"⛔ DND: {dnd}\n"
        f"⚫ Offline: {offline}\n"
        f"**Total:** {total}"
    )

    await interaction.response.send_message(msg)

# Optional tiny web server for Replit uptime pings
if os.getenv("KEEP_ALIVE", "0") == "1":
    from keep_alive import keep_alive  # type: ignore
    keep_alive()

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set. Add it as a secret.")

client.run(TOKEN)
