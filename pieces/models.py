def get_name_last_part(name):
    return name.split('_')[-1]

def add_function(num, where=None, structure=None):
    structure[where] += num

def add_function_factory(where, structure):
    new_add_function = add_function
    new_add_function.__defaults__ = (where, structure)
    return new_add_function

def join_names(prefix, name):
    return '%s%s' % (prefix, name)

def init_class(item):
    return type(item)()

class FigureStats(object):
    GET = 'get_'
    ADD = 'add_permanent_'
    SET = 'set_permanent_'
    ADD_TURN = 'add_'
    SET_TURN = 'set_'

    def __init__(self, **kargs):
        self.stats = dict()
        self.turn_stats = dict()
        for key, val in kargs.items():
            name = join_names(self.SET, key)
            self.__setattr__(name, val)

    def __getattr__(self, name):
        if name.startswith(self.GET):
            attr = self._stat_get(name)
        elif name.startswith(self.ADD_TURN):
            attr = self._add_turn_stat(name)
        elif name.startswith(self.ADD):
            attr = self._add_permanent_stat(name)
        else:
            attr = super(FigureStats, self).__getattr__(name)
        return attr

    def __setattr__(self, name, value):
        if name.startswith(self.SET_TURN):
            self._set_turn_stats(name, value)
        elif name.startswith(self.SET):
            self._set_permanent_stats(name, value)
        else:
            super(FigureStats, self).__setattr__(name, value)

    def _add_turn_stat(self, name):
        name = get_name_last_part(name)
        new_function = add_function_factory(name, self.turn_stats)
        return new_function

    def _add_permanent_stat(self, name):
        name = get_name_last_part(name)
        new_function = add_function_factory(name, self.stats)
        return new_function

    def _stat_get(self, name):
        name = get_name_last_part(name)
        stat = self.stats.get(name, None)
        turn_stat = self.turn_stats.get(name, None)
        result = self._add_stats(stat, turn_stat)
        return result 
    
    def _add_stats(self, a, b):
        if (a is None) or (b is None):
            result = (a or b)
        else:
            result = a + b
        return result

    def _set_permanent_stats(self, name, value):
        self._set_stats(self.stats, self.turn_stats, name, value)

    def _set_turn_stats(self, name, value):
        self._set_stats(self.turn_stats, self.stats, name, value)

    def _set_stats(self, origin, duplicate, name, value):
        name = get_name_last_part(name)
        origin[name] = value
        if name not in duplicate:
            duplicate[name] = init_class(item)

    def regenerate(self):
        for key, item in self.turn_stats.items():
            item = init_class(item)
            # base_stat = self.stats.get(key, None)
            # item.regenerate(base_stat)

    def __repr__(self):
        return str(self.__dict__)
        

class Figure(object):
    def __init__(self, 
                name, 
                position, **kargs):
        self.name = name
        # self.position = position
        self.stats = FigureStats(**kargs)

    def __str__(self):
        return '%s(%s)' % (self.name, self.position)

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, name):
        try:
            attr = super(self, Figure).__getattr__(name)
        except AttributeError:
            attr = self.stats.__getattr__(name)
        return attr

    def __setattr__(self, name, value):
        try:
            super(self, Figure).__setattr__(name, value)
        except AttributeError:
            self.stats.__setattr__(name, value)

    def end_turn(self):
        self.stats.regenerate()

    def die(self):
        pass

    def move(self, movement_cost, point):
        self.stats.add_movement(-movement_cost)
        self.stats.set_permanent_position = point












