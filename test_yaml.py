import yaml


def test_ignore_yaml():
    assert yaml.safe_load(open("ignore.yaml"))
