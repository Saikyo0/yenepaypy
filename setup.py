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
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)