
# 18th Mechanized Brigade Discord Bot — `/online` Only

Minimal Discord bot for the 18th Mech Foxhole server with exactly one slash command: **/online**.

## 1) Discord Developer Portal
- Create an application → **Add Bot**.
- Copy the token and save it for later.
- Enable **Privileged Gateway Intents**: Presence + Server Members.
- OAuth2 → URL Generator:
  - Scopes: `bot`, `applications.commands`
  - Permissions: `Send Messages`, `Read Message History`
  - Use the generated link to invite the bot to your server.

## 2) Environment Variables
Set these in Replit (Secrets) or locally:
- `DISCORD_TOKEN` — your bot token
- `GUILD_ID` — your server ID (for instant slash sync; optional but recommended)
- `KEEP_ALIVE` — set to `1` on Replit if you want the tiny web server running

## 3) Run
```bash
python3 -m pip install -r requirements.txt
python3 bot.py
```

## 4) Notes
- If `GUILD_ID` is unset, global slash sync can take ~1 hour.
- Presence counts rely on Discord presence data; make sure intents are enabled.
- This bot intentionally has only one command.
