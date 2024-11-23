class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the TV with default settings."""
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        """Toggle the TV's power state."""
        self._status = not self._status

    def mute(self):
        """Toggle the mute state. Mute only works if the TV is on."""
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._volume = self.MIN_VOLUME

    def channel_up(self):
        """Increase the TV channel, loop to minimum if maximum is exceeded."""
        if self._status:
            self._channel = self.MIN_CHANNEL if self._channel == self.MAX_CHANNEL else self._channel + 1

    def channel_down(self):
        """Decrease the TV channel, loop to maximum if minimum is exceeded."""
        if self._status:
            self._channel = self.MAX_CHANNEL if self._channel == self.MIN_CHANNEL else self._channel - 1

    def volume_up(self):
        """Increase the volume unless muted or already at the maximum."""
        if self._status and not self._muted:
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decrease the volume unless muted or already at the minimum."""
        if self._status and not self._muted:
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        """Return a string representation of the TV's current state."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"