from nose.tools import assert_almost_equal
from nose.tools import assert_in, assert_equal, assert_false
from mock import patch
import requests
from matplotlib import image 

from ..map import Map
import os
import yaml
#def example():
#    return png.Reader(filename=(os.path.join(
#    os.path.dirname(__file__),"fixtures","london.png"))).asRGB()

def test_build_default_params():
    with patch.object(requests,'get') as mock_get:
        with patch.object(image,'imread') as mock_img:
            Map(51.0, 0.0)
            mock_get.assert_called_with(
            "http://maps.googleapis.com/maps/api/staticmap?",
            params={
            'sensor':'false',
            'zoom':10,
            'size':'400x400',
            'center':'51.0,0.0',
            'style':'feature:all|element:labels|visibility:off',
            'maptype': 'satellite'
            }
        )

#def test_count_green():
#    with open(os.path.join(os.path.dirname(__file__),'fixtures','longlatpng.yaml')) as fixtures_file:
#        fixtures=yaml.load(fixtures_file)
#        with patch.object(requests,'get') as mock_get:
#            for fixture in fixtures:
#                m=Map(fixture['lat'], fixture['long'])
#                m.pixels=image.imread(os.path.join(os.path.dirname(__file__),'fixtures',fixture['png']))
#                assert_equal(m.count_green(), fixture['answer'])

  
