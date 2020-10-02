# Classes with bot messages

class Console():
    def __init__(self, activated: str = "[Event:BotActivated]" , member_joined: str = "[Event:UserJoin]", member_left: str = "[Event:UserRemove]", command_error: str = "[Event:CommandError]", cog_reload: str = "[Event:CogReload]"):
        self.activated = activated
        self.member_joined = member_joined
        self.member_left = member_left
        self.command_error = command_error
        self.cog_reload = cog_reload

class Guild():
    def __init__(self, insufficient_perms: str = "Insufficient Permissions!", member_joined: str = "Welcome ", member_left: str = "Goodbye ", command_error: str = "Command failed ", cog_reload: str = "Successfully reloaded "):
        self.insufficient_perms = insufficient_perms
        self.member_joined = member_joined
        self.member_left = member_left
        self.command_error = command_error
        self.cog_reload = cog_reload

class Meta():
    def __init__(self, cmd_prefix: str = ".", bot_game: str = "Change me, dev-sama!", admin_ids: str = "ThisWillNotWorkChangeMe"):
        self.cmd_prefix = cmd_prefix
        self.bot_game = bot_game
        self.admin_ids = admin_ids
        # This is not used for guild admins, but for bot developers - i.e anyone who needs access to the "reload {extension}" command.

