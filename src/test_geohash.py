import pytest
import geohash


def test_geohash_success():
    assert geohash.geohash(37.421542, -122.085589, b'2005-05-26-10458.68') == [37.857713, -122.544543]


def test_geohash_string():
    with pytest.raises(TypeError):
        assert geohash.geohash(37.421542, -122.085589, '2005-05-26-10458.68') is None


def test_geohash_no_coord():
    with pytest.raises(TypeError):
        assert geohash.geohash(None, None, b'2005-05-26-10458.68') is None


def test_geohash_no_date():
    with pytest.raises(TypeError):
        assert geohash.geohash(37.421542, -122.085589, None) is None