COMBAT_TURNS = 2


class Combat():
    def __init__(self, attacker, defender):
        self.tries = COMBAT_TURNS
        self.attacker = attacker
        self.defender = defender

    def resolve_power(self, power):
        damage = self.attacker.get(power) - self.defender.get(power)
        if damage > 0:
            self.defender.damage(abs(damage))
        else:
            self.attacker.damage(abs(damage))

    def resolve(self):
        for trie in range(self.tries):
            self.resolve_power('ranged_power')
            self.resolve_power('melle_power')
            self.resolve_power('infernal_power')
