import os
import pytest

import vaping
from vaping.config import parse_interval


def test_parse_interval():
    assert 1 == parse_interval('1s')
    assert .5 == parse_interval('500ms')
    assert 300 == parse_interval('5m')
    assert 3600 == parse_interval('1h')
    assert 86400 == parse_interval('1d')

    with pytest.raises(ValueError):
        parse_interval('1x')


def test_probe_plugin_name(config_dir):
    """
    checks that vaping correct errors if a probe is named the same as a plugin
    """
    config_dir = os.path.join(config_dir, "dupe")

    with pytest.raises(ValueError) as excinfo:
        vaping.daemon.Vaping(config_dir=config_dir)
    assert "probes may not share names with plugins" in str(excinfo)
