# -*- coding: utf-8 -*-
import os.path

from zope.interface import implementer
from zope.component import ComponentLookupError

from lxml import etree

from pyramid.interfaces import IRenderer
from pyramid.path import package_path
#from pyramid.response import Response


def includeme(config):
    """
    Auto include pour pyramid
    """
    config.add_renderer('.xsl', XsltRendererFactory)


class XsltRendererFactory(object):
    def __init__(self, info):
        """
        Factory constructor.
        """
        self._info = info

    def __call__(self, value, system):
        """
        Call to renderer.

        The renderer is cached for optimize access.
        """
        registry = system['request'].registry
        try:
            xsl = registry.getUtility(IRenderer, system['renderer_name'])
        except ComponentLookupError:
            xsl = XslRenderer(os.path.join(package_path(self._info.package),
                                           system['renderer_name']))
            registry.registerUtility(xsl, IRenderer, system['renderer_name'])
        return xsl(value, system)


@implementer(IRenderer)
class XslRenderer(object):

    def __init__(self, xslfilename):
        """
        Constructor.

        :param: xslfilename : path to the xsl.
        """
        self._transform = etree.XSLT(etree.parse(xslfilename))

    def __call__(self, value, system):
        """
        Rendering.

        :param: value can be a tuple, a string or etree.Element.
        If value is a tuple the first element must be a string or etree.Element.
        The string can be a xml content, an url to an xml document or path to an xml.

        value[1] and value[2] are optionnal and have to be dictionnary.

        value[1] is a dictionnary of arguments to passed to the xsl.
        value[2] is a dictionnary of arguments for pyramid response. /!\ not implemented yet.
        """
        xslArgs = {}
        responseArgs = {}

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
        """
        Return an etree.Element based on value.

        :param: value can be etree.Element, an XML content, a path or an url to
        an XML file.
        """
        if isinstance(value, etree._Element):
            return value
        elif value.startswith('http') or os.path.isfile(value):
            return etree.parse(value)
        else:
            return etree.fromstring(value)
