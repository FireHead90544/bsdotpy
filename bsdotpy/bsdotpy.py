import requests
from bs4 import BeautifulSoup
import datetime
from bsdotpy.errorhandlers import NetworkError, InvalidUniqueIdError
from bsdotpy.dataclasses import BombSquadPlayer


class BombSquadServer:
    """
    Instantiates a BombsquadServer object, which is capable of getting player data from the bombsquad's server.

    Methods:
        get_player_data() -- Gets the player data from the bombsquad's server and return a BombSquadPlayer object.

    Raises:
        NetworkError: Raised when there is a network error.
        InvalidUniqueIdError: Raised when an invalid unique id is provided.
    """
    BASE_URL = "http://bombsquadgame.com/accountquery"

    def __init__(self) -> None:
        self.name: str = None
        self.icon_url: str = None
        self.created_at: datetime.datetime = None

    def get_player_data(self, unique_id: str) -> BombSquadPlayer:
        """
        Gets the player data from the bombsquad's server and return a BombSquadPlayer object.

        Arguments:
            unique_id {str} -- The unique id of the player.
        
        Returns:
            BombSquadPlayer -- The player's data as a BombSquadPlayer object.
        """
        try:
            resp = requests.get(self.BASE_URL, params={"id": unique_id})
            data = eval(resp.text)
        except Exception:
            raise NetworkError("Could not connect to server.")

        try:
            soup = BeautifulSoup(data["name_html"], "html.parser")
            self.name = soup.getText()
            self.icon_url = soup.find('img')['src']
            self.created_at = datetime.datetime(*data['created'])

            return BombSquadPlayer(unique_id, self.name, self.icon_url, self.created_at)
        except KeyError:
            raise InvalidUniqueIdError("Invalid unique id provided. Please try again.")