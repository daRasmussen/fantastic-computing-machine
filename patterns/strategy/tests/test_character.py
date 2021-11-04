from strategy.character.character import KnifeBehavior, AxeBehavior, Queen, SwordBehavior, BowAndArrowBehavior, Troll, \
    King, Knight


def test_strategy():
    queen = Queen(KnifeBehavior())
    assert queen.fight()
    queen = Queen(AxeBehavior())
    assert queen.fight()
    queen = Queen(SwordBehavior())
    assert queen.fight()
    queen = Queen(BowAndArrowBehavior())
    assert queen.fight()

    troll = Troll(KnifeBehavior())
    assert troll.fight()
    troll = Troll(AxeBehavior())
    assert troll.fight()
    troll = Troll(SwordBehavior())
    assert troll.fight()
    troll = Troll(BowAndArrowBehavior())
    assert troll.fight()

    king = King(KnifeBehavior())
    assert king.fight()
    king = King(AxeBehavior())
    assert king.fight()
    king = King(SwordBehavior())
    assert king.fight()
    king = King(BowAndArrowBehavior())
    assert king

    knight = Knight(KnifeBehavior())
    assert knight.fight()
    knight = Knight(AxeBehavior())
    assert knight.fight()
    knight = Knight(SwordBehavior())
    assert knight.fight()
    knight = King(BowAndArrowBehavior())
    assert knight.fight()
