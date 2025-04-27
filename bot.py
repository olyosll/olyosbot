import discord
from discord.ext import commands
from discord import app_commands

# On configure les intents
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True
intents.guilds = True
intents.message_content = True

# On initialise le bot
bot = commands.Bot(command_prefix="!", intents=intents)


# Classe pour l'interface Among Us
class AmongUsPanel(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🔴 Démarrer Partie",
                       style=discord.ButtonStyle.danger)
    async def start_game(self, interaction: discord.Interaction,
                         button: discord.ui.Button):
        if interaction.user.voice and interaction.user.voice.channel:
            for member in interaction.user.voice.channel.members:
                await member.edit(mute=True)
            await interaction.response.send_message(
                "Tout le monde est mute ! 🎮", ephemeral=True)
        else:
            await interaction.response.send_message(
                "Va dans un vocal d'abord 😅", ephemeral=True)

    @discord.ui.button(label="🟢 Réunion", style=discord.ButtonStyle.success)
    async def meeting(self, interaction: discord.Interaction,
                      button: discord.ui.Button):
        if interaction.user.voice and interaction.user.voice.channel:
            for member in interaction.user.voice.channel.members:
                await member.edit(mute=False)
            await interaction.response.send_message("Réunion démarrée ! 🗳️",
                                                    ephemeral=True)
        else:
            await interaction.response.send_message(
                "Va dans un vocal d'abord 😅", ephemeral=True)

    @discord.ui.button(label="🔵 Fin de Réunion",
                       style=discord.ButtonStyle.primary)
    async def end_meeting(self, interaction: discord.Interaction,
                          button: discord.ui.Button):
        if interaction.user.voice and interaction.user.voice.channel:
            for member in interaction.user.voice.channel.members:
                await member.edit(mute=True)
            await interaction.response.send_message(
                "Fin de la réunion, tout le monde re-mute ! 🤫", ephemeral=True)
        else:
            await interaction.response.send_message(
                "Va dans un vocal d'abord 😅", ephemeral=True)

    @discord.ui.button(label="⚪ Fin de Partie",
                       style=discord.ButtonStyle.secondary)
    async def end_game(self, interaction: discord.Interaction,
                       button: discord.ui.Button):
        if interaction.user.voice and interaction.user.voice.channel:
            for member in interaction.user.voice.channel.members:
                await member.edit(mute=False)
            await interaction.response.send_message(
                "Fin de la partie, tout le monde démute ! 🎉", ephemeral=True)
        else:
            await interaction.response.send_message(
                "Va dans un vocal d'abord 😅", ephemeral=True)


# Slash command pour afficher l'embed avec les boutons
@bot.tree.command(name="panel",
                  description="Affiche le panneau Among Us avec des boutons")
async def panel(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Among Us Panel 🎮",
        description="Utilise les boutons ci-dessous pour contrôler la partie :",
        color=discord.Color.blurple())
    await interaction.response.send_message(embed=embed, view=AmongUsPanel())


# Quand le bot est prêt
@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    # Synchroniser les commandes de slash
    await bot.tree.sync()


# On récupère le TOKEN de l'environnement
TOKEN = ""  # Remplace ceci par ton token réel

bot.run(TOKEN)
