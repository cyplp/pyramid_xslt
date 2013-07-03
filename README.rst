Xslt renderer for pyramid
=========================


Rendering for pyramid_ using XSLT.

.. _pyramid : http://docs.pylonsproject.org/projects/pyramid/en/latest/

.. image:: https://travis-ci.org/cyplp/pyramid_xslt.png?branch=master
   :target: https://travis-ci.org/cyplp/pyramid_xslt


Usage
-----

You can include the xslt rendering in your pyramid app via :

::

  config.include('pyramid_xslt')

or in the .ini deployement file :

::

 pyramid.includes =
     pyramid_xslt


And in your views :

::

  @view_config(route_name='home', renderer='templates/home.xsl')
  def my_view(request):
      return ('<a>aa</a>', {'A': 2})


The view can return
 - a string containing the whole xml, an url to an xml file or a path to an xml file,
 - a tuple where the first element is a string as above, the second is a dictionnary of
   arguments passed to xslt stylesheet and the third is a dictionnary of arguments for
   the pyramid response (not implented yet). The second and the third element of the
   tuple are optionnal.


The xslt tree is build one the first request and cached after. So the first request
is slower than the next one.
