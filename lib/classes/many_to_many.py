class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        if isinstance(hometown, str) and len(hometown) > 0 and not(hasattr(self, '_hometown')):
            self._hometown = hometown

    def concerts(self):
        pass

    def venues(self):
        pass

    def play_in_venue(self, venue, date):
        pass

    def all_introductions(self):
        pass


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def concerts(self):
        pass

    def bands(self):
        pass
