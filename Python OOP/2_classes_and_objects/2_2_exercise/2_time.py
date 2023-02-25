class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:

        h, m, s = self.hours, self.minutes, self.seconds

        if s < 10:
            s = "0" + str(self.seconds)
        if m < 10:
            m = "0" + str(self.minutes)
        if h < 10:
            h = "0" + str(self.hours)
        return f"{h}:{m}:{s}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:

            self.seconds = 0
            self.minutes += 1

        if self.minutes > Time.max_minutes:

            self.minutes = 0
            self.hours += 1

        if self.hours > Time.max_hours:

            self.hours = 0

        return self.get_time()