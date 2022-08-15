from setuptools import setup, find_packages

setup(
    name='pylotier',
    version='0.1.0',    
    description='Common toolings for python.',
    url='https://github.com/pilotier/pylotier',
    author='Ibrahim Abdulhafiz',
    author_email='ibrahim@pilotier.com',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=['opencv-python',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)