
# BSDotPy

BSDotPy, A module to get a bombsquad player's account data from bombsquad's servers.

## Badges

Provided By: [shields.io](https://shields.io/)

[![PyPI Version](https://img.shields.io/pypi/v/bsdotpy?style=for-the-badge)](https://pypi.org/project/bsdotpy/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/bsdotpy?color=red&style=for-the-badge)](https://pypi.org/project/bsdotpy/)
[![Apache License 2.0](https://img.shields.io/pypi/l/bsdotpy?color=lime&style=for-the-badge)](https://opensource.org/licenses/)
[![Connect On Discord](https://img.shields.io/discord/710909601356447805?color=yellow&style=for-the-badge)](https://discord.gg/dN66r3D)
[![Code Lines](https://img.shields.io/tokei/lines/github/FireHead90544/bsdotpy?color=orange&style=for-the-badge)](https://github.com/FireHead90544/bsdotpy)
[![Code Size](https://img.shields.io/github/languages/code-size/FireHead90544/bsdotpy?style=for-the-badge)](https://github.com/FireHead90544/bsdotpy)
[![Pull Requests](https://img.shields.io/github/issues-pr/FireHead90544/bsdotpy?style=for-the-badge)](https://github.com/FireHead90544/bsdotpy/pulls)
[![Issues](https://img.shields.io/github/issues/FireHead90544/bsdotpy?color=teal&style=for-the-badge)](https://github.com/FireHead90544/bsdotpy/issues)
[![Contributors](https://img.shields.io/github/contributors/FireHead90544/bsdotpy?style=for-the-badge)](https://github.com/FireHead90544/bsdotpy/graphs/contributors)

## Acknowledgements

 - [Issues](https://github.com/FireHead90544/bsdotpy/issues)
 - [Pull Requests](https://github.com/FireHead90544/bsdotpy/pulls)
 - [View Project On PyPI](https://pypi.org/project/bsdotpy/)

  
## Authors

- [@Rudransh Joshi](https://www.github.com/FireHead90544)

  
## Installation

Easiest way is to install bsdotpy with pip

```shell
  pip install -U bsdotpy
```


## Usage / Examples

### As mentioned in the bombsquad's server builds, you might need to show stats of the players playing in your server's website, instead of using `http://bombsquadgame.com/accountquery?id={YOUR_UNIQUE_ID}` api and manually reformating the data, you can use this api wrapper to do everything for you automatically. Currently, the below four parameters are returned by API.

**To get your account id, enter 'getaccountid' in BombSquad Application's Settings -> Advanced -> Enter Code.**

```py
from bsdotpy import BombSquadServer

server = BombSquadServer() # Instantiates a BombSquadServer object which will interact with bombsquad's server.

unique_id = "pb-IF4rVEQCKg==" # Unique ID must be valid else an error will be thrown
player = server.get_player_data(unique_id) # Returns a bsdotpy.BombSquadPlayer object

print(player.name) # Prints the player's name returned by bombsquad server's api
>>> '꧁༒Firͥe Heͣaͫd༒꧂'

print(player.unique_id) # Prints unique id of the player
>>> 'pb-IF4rVEQCKg=='

print(player.icon_url) # Prints the url to the icon the player has
>>> 'http://bombsquadgame.com/img/char/30.png'

print(player.created_at) # Prints a datetime.datetime object of when the player was created
>>> 2020-02-17 17:10:50

print(repr(player))  # Prints the class object representation of the BombSquadPlayer object
>>> <BombSquadPlayer unique_id='pb-IF4rVEQCKg==', name='꧁༒Firͥe Heͣaͫd༒꧂', icon_url='http://bombsquadgame.com/img/char/30.png', created_at='2020-02-17 17:10:50'>
```

## Contributing

Contributions are always welcome!

- Fork this repository.
- Make the changes in your forked repositry.
- Make sure to fetch upstream before generating a PR.
- Generate a pull request.

Please adhere to the GitHub's `code of conduct` for contributions and contributors.

  
## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
