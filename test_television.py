from television import Television

def test_initial_state():
    tv = Television()
    assert not tv._status
    assert not tv._muted
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL

def test_power_and_mute():
    tv = Television()
    tv.power()
    assert tv._status
    tv.mute()
    assert tv._muted
    tv.mute()
    assert not tv._muted
    tv.power()
    assert not tv._status

def test_channel_change():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._channel == 1
    tv.channel_down()
    assert tv._channel == Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL

def test_volume_change():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._volume == 1
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME
    tv._volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME

def test_mute_effect_on_volume():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._muted
    assert tv._volume == Television.MIN_VOLUME
    tv.mute()
    assert not tv._muted
    tv.volume_up()
    assert tv._volume == 1

def test_str():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 1"