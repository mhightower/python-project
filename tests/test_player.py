import pytest
from src.player import Player

def test_player_name() -> None:
    player = Player(10)
    assert player.name == 'Player'

def test_player_id() -> None:
    player = Player(10)
    assert player.id == 10

def test_player_hash() -> None:
    player = Player(5, 'Foo')
    assert player.__hash__() == 5

def test_player_equal() -> None:
    player01 = Player(5, 'Foo')
    player02 = Player(5, 'Bar')
    assert player01.__eq__(player02)

def test_player_not_equal() -> None:
    player01 = Player(5, 'Foo')
    player02 = Player(10, 'Bar')
    assert not player01.__eq__(player02)