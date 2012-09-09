"""
flask-sass
==========

A small Flask extension that makes it easy to use Sass (SCSS) with your Flask application.

Package unabashedly adapted from https://github.com/weapp/flask-coffee2js.

Usage
-----

You can activate it by calling the ``sass`` function with your Flask app as a parameter:

      from flaskext.sass import sass
      sass(app, input_dir='assets/scss', output_dir='static/css')

This will intercept the request for ``output_dir/*.css`` and compile the file if it is
necesary using the files from ``input_dir/*.scss``.

When you deploy your app you might not want to accept the overhead of checking
the modification time of your ``.scss`` and ``.css`` files on each request. A
simple way to avoid this is wrapping the sass call in an if statement:

      if app.debug:
          from flaskext.sass import sass
          sass(app)
          
If you do this you'll be responsible for rendering the ``.scss`` files into
``.css`` when you deploy in non-debug mode to your production server.


- documentation_
- development_


.. _documentation: https://github.com/imiric/flask-sass
.. _development: https://github.com/imiric/flask-sass

"""

from setuptools import setup


setup(
    name='flask-sass',
    version='0.1',
    url='https://github.com/imiric/flask-sass',
    license='MIT',
    author='Ivan Miric',
    #author_email='',
    description='A small Flask extension that adds Sass (SCSS) support to Flask.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'pyScss'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
