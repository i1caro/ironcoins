from ming import Field, schema
from ming.declarative import Document

from www.main import session


class Map(Document):
    class __mongometa__:
        session = session
        name = 'map'

    _id = Field(schema.ObjectId),
    map_matrix = Field([[str]], if_missing=[[]])
    creatures = Field(
        {str: {'position': [int]}},
        if_missing=[]
    )
    borders = Field(
        {str: {'position': [[int]]}},
        if_missing=[]
    )
    moves = Field(
        [[int, int]],
        if_missing=[]
    )


class Player(Document):
    class __mongometa__:
        session = session
        name = 'player'

    _id = Field(schema.ObjectId),
    side = Field(str)
    borders = Field(str)
    name = Field(str)
    cards = Field(
        [str],
        if_missing=[]
    )
    resources = Field({
        'souls': int,
        'fire': int,
        'ichor': int,
        'dark': int,
        'prestige': int
    })
    creatures = Field({str: None}, if_missing=[])


class Creature(Document):
    class __mongometa__:
        session = session
        name = 'creature'

    _id = Field(schema.ObjectId),
    card = Field(str),
    name = Field(str),
    side = Field(str),
    stats = Field([
        {str: [int]}
    ], if_missing=[]),
    cards = Field([str], if_missing=[])

