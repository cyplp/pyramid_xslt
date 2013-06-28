# -*- coding: utf-8 -*-
import os.path

from zope.interface import implementer
from zope.component import getGlobalSiteManager
from zope.component import getUtility
from zope.component import ComponentLookupError

from lxml import etree

from pyramid.interfaces import IRenderer
from pyramid.path import package_path

gsm = getGlobalSiteManager()

def includeme(config):
    """
    Auto include pour pyramid
    """
    config.add_renderer('.xsl', XsltRendererFactory)

class XsltRendererFactory:
    def __init__(self, info):
        """ Constructor: info will be an object having the
        following attributes: name (the renderer name), package
        (the package that was 'current' at the time the
        renderer was registered), type (the renderer type
        name), registry (the current application registry) and
        settings (the deployment settings dictionary). """
        print info
        print dir(info)
        self._info = info

    def __call__(self, value, system):
        """ Call the renderer implementation with the value
        and the system value passed in as arguments and return
        the result (a string or unicode object).  The value is
        the return value of a view.  The system value is a
        dictionary containing available system values
        (e.g. view, context, and request). """

        try:
            xsl = getUtility(IRenderer, system['renderer_name'])
        except ComponentLookupError:
            xsl = XslRenderer(os.path.join(package_path(self._info.package),
                                           system['renderer_name']))

            gsm.registerUtility(xsl, IRenderer, system['renderer_name'])
        return xsl(value, system)


@implementer(IRenderer)
class XslRenderer(object):

    def __init__(self, xslfilename):
        """
        """
        self._transform = etree.XSLT(etree.parse(xslfilename))

    def __call__(self, value, system):
        """
        """

        print value
        print system

        doc = etree.fromstring(value)
        return etree.tostring(self._transform(doc))
