# TODO: multiple day subtract
# TODO: combination of large negative minutes with positive hours
class Clock:
    def __init__(self, hour, minute):
        """ both hours and minutes can be any integer
        this method will take those and modulate them to a standard
        internal representation with rollover"""
        if minute >= 60:
            extra_hours = minute // 60
            minute = minute % 60
        elif minute <= -60:
            extra_hours = -1 * (minute // -60)
            minute = minute % -60
        else:
            extra_hours = 0

        self.minute = minute

        hour += extra_hours
        if hour >= 24:
            hour = hour % 24
        elif hour <= -24:
            hour = hour % -24
        self.hour = hour

        #  print(f'{extra_hours=} {minute=}')

    def __repr__(self):
        #  return f'{self.extra_hours=} {self.hour=} {self.minute=}'
        return f'{self.hour=} {self.minute=}'

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        _ = Clock(self.hour, self.minute+minutes)
        return _
        #  self.hour, self.minute = _.hour, _.minute

    def __sub__(self, minutes):
        _ = Clock(self.hour, self.minute-minutes)
        return _
        #  self.hour, self.minute = _.hour, _.minute
