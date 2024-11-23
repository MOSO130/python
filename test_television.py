import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        """Setup for each test."""
        self.tv1 = Television()

    def teardown_method(self):
        """Teardown after each test."""
        del self.tv1

    def test_init(self):
        """Test the initial state of the TV."""
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        """Test the power toggle functionality."""
        self.tv1.power()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 0"
        self.tv1.power()
        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        """Test the mute functionality."""
        self.tv1.mute()
        assert not self.tv1._muted
        self.tv1.power()
        self.tv1.mute()
        assert self.tv1._muted
        self.tv1.mute()
        assert not self.tv1._muted

    def test_channel_up(self):
        """Test channel increment functionality."""
        self.tv1.power()
        self.tv1.channel_up()
        assert str(self.tv1) == "Power = True, Channel = 1, Volume = 0"
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        """Test channel decrement functionality."""
        self.tv1.power()
        self.tv1.channel_down()
        assert str(self.tv1) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        """Test volume increment functionality."""
        self.tv1.power()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        """Test volume decrement functionality."""
        self.tv1.power()
        self.tv1.volume_down()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 0"

    def test_mute_effect(self):
        """Test the effect of muting on volume."""
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 0"
        self.tv1.mute()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power = True, Channel = 0, Volume = 1"