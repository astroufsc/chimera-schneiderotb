from distutils.core import setup

setup(
    name='chimera_schneiderotb',
    version='0.0.1',
    packages=['chimera_schneiderotb', 'chimera_schneiderotb.instruments'],
    scripts=[],
    install_requires=['pymodbus', 'chimera-python'],
    url='http://github.com/astroufsc/chimera-schneiderotb',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='Chimera instrument plugin for Schneider Electric Advantys OTB Ethernet network I/O module'
)
