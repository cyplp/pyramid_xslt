from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.xsl')
def my_view(request):
    return ('<a>aa</a>', {'A': 2})

@view_config(route_name='etree', renderer='templates/home.xsl')
def etreeView(request):
    from lxml import etree
    return etree.fromstring('<a>aa</a>')
