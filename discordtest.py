from logging import debug
import os

from flask import Flask, redirect, url_for
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized

app = Flask(__name__)

app.secret_key = b"random bytes representing flask secret key"
# OAuth2 must make use of HTTPS in production environment.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"      # !! Only in development environment.

app.config["DISCORD_CLIENT_ID"] = 0    # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = "fdsafdsa"                # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "http://localhost:5000/callback"                 # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = "fdasfdsafdasfdsafdsafdsa"                    # Required to access BOT resources.


discord = DiscordOAuth2Session(app)


@app.route("/login/")
def login():
    return discord.create_session()


@app.route("/callback/")
def callback():
    discord.callback()
    return redirect(url_for(".me"))


@app.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for("login"))


@app.route("/me/")
@requires_authorization
def me():
    user = discord.fetch_user()
    print(dir(user))
    return f"""
    <html>
        <head>
            <title>{user.name}</title>
        </head>
        <body>
            <img src='{user.avatar_url}' />
            <ul>
                
            </ul>
        </body>
    </html>"""
"""
'_bot_request', '_guilds', '_payload', '_request', 'add_to_guild', 'avatar_hash', 
'avatar_url', 'bot', 'connections', 'default_avatar_url', 'discriminator', 
'email', 'fetch_connections', 'fetch_from_api', 'fetch_guilds', 'flags', 
'get_from_cache', 'guilds', 'id', 'is_avatar_animated', 'locale', 'mfa_enabled', 
'name', 'premium_type', 'to_json', 'username', 'verified']"""


if __name__ == "__main__":
    app.run(debug=True)