COMBAT_TRIES = 2


class Combat():
    def __init__(self, attacker, defender):
        self.tries = COMBAT_TRIES
        self.attacker = attacker
        self.defender = defender

    def resolve_power(self, power):
        damage = self.attacker.stats.get(power, 0) - self.defender.stats.get(power, 0)
        if damage > 0:
            self.defender.stats['life'] -= damage
        else:
            self.attacker.stats['life'] += damage

    def resolve(self):
        for trie in range(self.tries):
            self.resolve_power('ranged_power')
            self.resolve_power('melle_power')
            self.resolve_power('infernal_power')
