from setuptools import setup

setup(
    name='yenepaypy',
    version='0.1.0',    
    description='A simple and easily integrable yenepay library for your python code',
    url='https://github.com/Saikyo0/yenepaypyth',
    author='Saikyo0',
    author_email='tmansaikyou@gmail.com',
    license='GNU General Public License',
    packages=['pyOpenSSL','requests'],
    install_requires=['pyOpenSSL',
                      'requests',             
                      ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
