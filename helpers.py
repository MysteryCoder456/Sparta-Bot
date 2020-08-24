import discord


async def create_mute_role(guild):
    perms = discord.Permissions(send_messages=False)
    mute_role = await guild.create_role(name="Muted", color=discord.Color.dark_gray(), permissions=perms)

    for channel in guild.channels:
        await channel.set_permissions(mute_role, send_messages=False)

    return mute_role


def create_new_whitelist():
    whitelist_entry = {
        "active": False,
        "users": [],
        "urls": [],
        "channels": []
    }
    return whitelist_entry