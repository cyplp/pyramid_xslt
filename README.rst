========================
Xslt renderer for pyramid
=========================


Rendering for pyramid_ using XSLT.

.. _pyramid : http://docs.pylonsproject.org/projects/pyramid/en/latest/


Usage
=====

You can include the xslt rendering in your pyramid app via :

..

  config.include('pyramid_xslt')

or in the .ini deployement file :

..

 pyramid.includes =
     pyramid_xslt


And in your views :

..

  @view_config(route_name='home', renderer='templates/home.xsl')
  def my_view(request):
      return ('<a>aa</a>', {'A': 2})


