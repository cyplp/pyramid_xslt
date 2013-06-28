# -*- coding: utf-8 -*-
import os.path

from zope.interface import implementer
from zope.component import getGlobalSiteManager
from zope.component import getUtility
from zope.component import ComponentLookupError

from lxml import etree

from pyramid.interfaces import IRenderer
from pyramid.path import package_path
from pyramid.response import Response

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
        print etree.parse(xslfilename)
        self._transform = etree.XSLT(etree.parse(xslfilename))

    def __call__(self, value, system):
        """
        """
        xslArgs = None
        responseArgs = None

        if type(value) is not tuple:
            doc = self._mkdoc(value)

        else:
            doc = self._mkdoc(value[0])
            try:
                xslArgs  = {key: str(value[1][key]) for key in  value[1]}
                try :
                   responseArgs = value[2]
                except IndexError:
                   pass
            except IndexError:
               pass

        return etree.tostring(self._transform(doc, **xslArgs))

    @staticmethod
    def _mkdoc(value):
        # TODO url and file
        if isinstance(value, etree._Element):
            return value
        elif value.startswith('http') or os.path.isfile(value):
            etree.parse(value)
        else:
            return etree.fromstring(value)
