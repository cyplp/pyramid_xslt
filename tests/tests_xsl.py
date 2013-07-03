import unittest
import sys
# import transaction

# from pyramid import testing

# from .models import DBSession
from lxml import etree

from zope.interface.registry import Components
from pyramid.interfaces import IRenderer

from pyramid_xslt import XsltRendererFactory
from pyramid_xslt import XslRenderer



class FakeRequest(object):
    pass


class FakeInfo(object):
    package = sys.modules[__name__]


class TestXslFactory(unittest.TestCase):
    def test_factory_init(self):
        """
        Test XsltRendererFactory __init__.
        """
        xf = XsltRendererFactory({'a': 2})
        self.assertEquals(xf._info, {'a': 2})

    def test_factory_call(self):
        """
        Test XsltRendererFactory __call__.
        """
        system = {}

        system['renderer_name'] = '../sample_app/sample_app/templates/home.xsl'
        system['request'] = FakeRequest()
        system['request'].registry = Components()

        self.assertEquals(system['request'].registry.queryUtility(IRenderer,
                                                '../sample_app/sample_app/templates/home.xsl'), None)

        xf = XsltRendererFactory(FakeInfo())
        result = xf('<a>bb</a>', system)

        self.assertEquals('<b>bb</b>', result)
        renderer = system['request'].registry.queryUtility(IRenderer,
                                            '../sample_app/sample_app/templates/home.xsl')
        self.assertNotEquals(renderer, None)
        self.assertTrue(isinstance(renderer, XslRenderer))


        result = xf('<a>bb</a>', system)
        self.assertEquals('<b>bb</b>', result)

        self.assertTrue(renderer is system['request'].registry.queryUtility(IRenderer,
                                                      '../sample_app/sample_app/templates/home.xsl'))


class TestXslRender(unittest.TestCase):
    """
    """
    def test_renderer_init(self):
        """
        Test XslRenderer __init__.
        """
        xslt = XslRenderer('sample_app/sample_app/templates/home.xsl')
        self.assertTrue(isinstance(xslt._transform, etree.XSLT))
        # TODO check interface

    def test_call(self):
        """
        Test de XslRenderer __call__.
        """
        xslt = XslRenderer('sample_app/sample_app/templates/home.xsl')

        result = xslt('<a>bb</a>', {})
        self.assertEquals('<b>bb</b>', result)

        result = xslt(('<a>bb</a>'), {})
        self.assertEquals('<b>bb</b>', result)

        result = xslt(('<a>bb</a>', {}), {})
        self.assertEquals('<b>bb</b>', result)

        result = xslt(('<a>bb</a>', {}, {}), {})
        self.assertEquals('<b>bb</b>', result)

        result = xslt(etree.fromstring('<a>bb</a>'), {})
        self.assertEquals('<b>bb</b>', result)

        # import os.path
        # print os.path.isfile('tests/fake.xml')

        # result = xslt('tests/fake.xml', {})
        # self.assertEquals('<b>bb</b>', result)

    def test_mkdoc(self):
        """
        Test de XslRenderer _mkdoc.
        """
        xslt = XslRenderer('sample_app/sample_app/templates/home.xsl')

        self.assertTrue(isinstance(xslt._mkdoc('<a>bb</a>'), etree._Element))

        self.assertTrue(isinstance(xslt._mkdoc(etree.fromstring('<a>bb</a>')),
                                   etree._Element))

        self.assertTrue(isinstance(xslt._mkdoc('tests/fake.xml'),
                                   etree._ElementTree))


