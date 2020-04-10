try:
    from setuptools import setup
except:
    from distutils.core import setup



setup(name="import_test",
      version="0.1",
      description="functions to read, convert and handle toyMC simulations, fit results and templates used by the XENONnT inference codes",
      author="XENONnT collaboration",
      author_email="knut.dundas.moraa@columbia.edu",
      url="https://github.com/XENONnT/inference_interface",
      py_modules=["testimports"]
      )
