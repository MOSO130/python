class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        """Turn the TV on or off."""
        self._status = not self._status

    def mute(self):
        """Mute or unmute the TV."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """Increase the TV channel, looping back to minimum if maximum is exceeded."""
        if self._status:
            self._channel = self.MIN_CHANNEL if self._channel == self.MAX_CHANNEL else self._channel + 1

    def channel_down(self):
        """Decrease the TV channel, looping back to maximum if minimum is exceeded."""
        if self._status:
            self._channel = self.MAX_CHANNEL if self._channel == self.MIN_CHANNEL else self._channel - 1

    def volume_up(self):
        """Increase the TV volume unless muted or at maximum volume."""
        if self._status and not self._muted:
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decrease the TV volume unless muted or at minimum volume."""
        if self._status and not self._muted:
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        """Return the TV's current status, channel, and volume."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"