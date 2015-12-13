from nose.tools import assert_almost_equal
from nose.tools import assert_in, assert_equal, assert_false
from mock import patch, Mock
import requests
from matplotlib import image 
from StringIO import StringIO

from ..map import Map
import os
import yaml

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
"""
# old alternative tests, new ones below better use of mock
def test_count_green():
    #load fictures from yaml, easily extendable, predownloaded maps
    with open(os.path.join(os.path.dirname(__file__),'fixtures','longlatpng.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        #mock internet request
        with patch.object(requests,'get') as mock_get:
            for fixture in fixtures:
                #mock image parsing which would raise error otherwise due to request mock
                with patch.object(image,'imread') as mock_img:
                    m=Map(fixture['lat'], fixture['long'])
                #inject fixture png into map object
                m.pixels=image.imread(os.path.join(os.path.dirname(__file__),'fixtures',fixture['png']))
                #compare with green answer
                assert_equal(m.count_green(), fixture['answer'])

def test_show_green():
    #load fictures from yaml, easily extendable, predownloaded maps
    with open(os.path.join(os.path.dirname(__file__),'fixtures','longlatpng.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        #mock internet request
        with patch.object(requests,'get') as mock_get:
            for fixture in fixtures:
                #mock image parsing which would raise error otherwise due to request mock
                with patch.object(image,'imread') as mock_img:
                    m=Map(fixture['lat'], fixture['long'])
                #inject fixture png into map object
                m.pixels=image.imread(os.path.join(os.path.dirname(__file__),'fixtures',fixture['png']))
                #compare with fixture green image
                fixBuf=StringIO()
                image.imsave(fixBuf, image.imread(os.path.join(os.path.dirname(__file__),'fixtures',fixture['png-green']), format='png'))
                assert_equal(m.show_green()[0:100], fixBuf.getvalue()[0:100])
"""

def test_count_green2():
    #load fictures from yaml, easily extendable, predownloaded maps
    with open(os.path.join(os.path.dirname(__file__),'fixtures','longlatpng.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            #open png fixture
            with open(os.path.join(os.path.dirname(__file__),'fixtures',fixture['png'])) as png_file:
                #mock the internet request and return png from file
                with patch('requests.get', return_value=Mock(content=png_file.read())) as mock_get:
                    m=Map(fixture['lat'], fixture['long'])
                    #compare with green answer
                    assert_equal(m.count_green(), fixture['answer'])


def test_show_green2():
    #load fictures from yaml, easily extendable, predownloaded maps
    with open(os.path.join(os.path.dirname(__file__),'fixtures','longlatpng.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            #open png fixture
            with open(os.path.join(os.path.dirname(__file__),'fixtures',fixture['png'])) as png_file:
                #mock the internet request and return png from file
                with patch('requests.get', return_value=Mock(content=png_file.read())) as mock_get:
                    m=Map(fixture['lat'], fixture['long'])
                    #compare with fixture green image
                    fixBuf=StringIO()
                    image.imsave(fixBuf, image.imread(os.path.join(os.path.dirname(__file__),'fixtures',fixture['png-green']), format='png'))
                    assert_equal(m.show_green()[0:100], fixBuf.getvalue()[0:100])



    


 
