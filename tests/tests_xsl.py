import unittest
# import transaction

# from pyramid import testing

# from .models import DBSession

from pyramid_xslt import XsltRendererFactory
from pyramid_xslt import XslRenderer


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


class TestXslRender(unittest.TestCase):
    """
    """
    def test_renderer_init(self):
        """
        Test XslRenderer __init__.
        """
        xslt = XslRenderer('sample_app/sample_app/templates/home.xsl')
        # TODO check _transform
        # TODO check interface

    def test_call(self):
        """
        Test de XslRenderer __call__.
        """
        xslt = XslRenderer('sample_app/sample_app/templates/home.xsl')
        result = xslt('<a>bb</a>', {})
        self.assertEquals('<b>bb</b>', result)
