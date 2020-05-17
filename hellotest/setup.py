from distutils.core import setup, Extension
setup(name='hellotest', version='1.0',  \
      ext_modules=[Extension('hellotest', ['hellotest.c'])])

