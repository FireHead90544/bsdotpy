import datetime

class BombSquadPlayer:
    """
    Represents a BombSquadPlayer object.

    Attributes:
        unique_id {str} -- The unique id of the player.
        name {str} -- The name of the player.
        icon_url {str} -- The url of the player's icon.
        created_at {datetime.datetime} -- The date and time when the player was created.
    
    """
    def __init__(self, unique_id, name, icon_url, created_at) -> None:
        self.unique_id: str = unique_id
        self.name: str = name
        self.icon_url: str = icon_url
        self.created_at: datetime.datetime = created_at

    def __repr__(self) -> str:
        return f"<BombSquadPlayer unique_id='{self.unique_id}', name='{self.name}', icon_url='{self.icon_url}', created_at='{self.created_at}'>" 