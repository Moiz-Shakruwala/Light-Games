
class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (230,230,230)
        self.bullets_allowed = 3

        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1