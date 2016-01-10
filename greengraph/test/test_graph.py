from nose.tools import assert_almost_equal
from nose.tools import assert_in, assert_equal, assert_false
from mock import patch, Mock
import numpy as np
from ..graph import Greengraph
from ..map import Map
import os
import yaml


def test_build_default_params():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','startend.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            g=Greengraph(**fixture)
            assert_equal(g.geocoder.domain, 'maps.google.co.uk')
            assert_equal(g.start, fixture['start'])
            assert_equal(g.end, fixture['end'])

def test_geolocate():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','longlatplace.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            g=Greengraph("","")
            g.geocoder=Mock(geocode=Mock( return_value=[( (fixture['lat'], fixture['long'], 0.0), (fixture['lat'], fixture['long']) )] ))
            latlong=g.geolocate(fixture['place'])
            assert_almost_equal(latlong[0],fixture['lat'],places=2)
            assert_almost_equal(latlong[1], fixture['long'],places=2)

def test_location_sequence():
    result=Greengraph.location_sequence(Greengraph("",""), (0,0),(10,10),5)
    np.testing.assert_equal(result[0],(0,0))
    np.testing.assert_equal(result[1],(2.5,2.5))

#def test_green_between():
#    g=Greengraph("","")
#    geom=Mock(name="geolocate", side_effect=[(0,0),(10,10)])
    #replace geolocate function by mock
#    g.geolocate=geom
#    with patch.object(Map,'__init__', return_value=None) as init_mock:
#        init_mock.count_green=Mock()
#        g.green_between(5)
#        init_mock.assert_called_with((0,0),(2.5,2.5))

    
