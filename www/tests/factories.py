from www.models import Map, Player, Creature
from ming import mim, Session


mim_connection = mim.Connection()


class MapFactory(Map):
    class __mongometa__:
        session = Session(mim_connection)


class PlayerFactory(Player):
    class __mongometa__:
        session = Session(mim_connection)


class CreatureFactory(Creature):
    class __mongometa__:
        session = Session(mim_connection)
