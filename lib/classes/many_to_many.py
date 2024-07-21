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
        band_concerts = [concert for concert in Concert.all if self == concert.band]
        return band_concerts if len(band_concerts) > 0 else None

    def venues(self):
        venues_list = []
        for concert in Band.concerts(self):
            if not(concert.venue in venues_list):
                venues_list.append(concert.venue)
        return venues_list if len(venues_list) > 0 else None

    def play_in_venue(self, venue, date):
        new_concert = Concert(date,self,venue)
        return new_concert

    def all_introductions(self):
        all_venues = Band.venues(self)
        all_intros = []
        if len(all_venues) == 0:
            return None
        else:
            for venue in all_venues:
                all_intros.append(f"Hello {venue.city}!!!!! We are {self.name} and we're from {self.hometown}")
        return all_intros


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        if isinstance(venue, Venue):
            self._venue = venue

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city

    def concerts(self):
        venue_concerts = [concert for concert in Concert.all if self == concert.venue]
        return venue_concerts if len(venue_concerts) > 0 else None

    def bands(self):
        bands_set = set()
        for concert in Venue.concerts(self):
            bands_set.add(concert.band)
        return list(bands_set) if len(bands_set) > 0 else None

    def concert_on(self,date):
        for concert in Venue.concerts(self):
            if date == concert.date:
                return concert
        return None

