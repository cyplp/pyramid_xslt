import unittest
# import transaction

# from pyramid import testing

# from .models import DBSession

from pyramid_xslt import XsltRendererFactory


class TestXsl(unittest.TestCase):
    def test_factory_init(self):
        xf = XsltRendererFactory({'a': 2})
        self.assertEquals(xf._info, {'a': 2})
