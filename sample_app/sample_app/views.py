from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.xsl')
def my_view(request):
    return '<a>aa</a>'
