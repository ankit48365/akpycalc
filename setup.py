from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup
(
    
    # case Sensitive should match - pip install NAME
    name = 'akpycalc', 
    # your version
    version = '0.1.0',
    
    '''
    This is the short description will show on the top of the webpage of your package on pypi.org
    '''
    description = 'test python package.',
    
    '''
    This is the name of your main module file. No need to include the .py at the end.
    '''    
    py_modules = ["akpycalc"],
    
    '''
    shows where the module is stored.
    '''
    package_dir = {'':'src'},
    

    Change the author name(s) and email(s) here.
    '''
    author = 'AuthorName',
    author_email = 'xyz123@something.com',
    
    '''
    Leave the following as default. It will show the readme and changelog on the main page of your package.
    '''
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    
    '''
    The url to where your package is stored for public view. Normally, it will be the github url to the repository you just forked.
    '''
    url='https://github.com/jinhangjiang/morethansentiments',
    
    '''
    Leave it as deafult.
    '''
    include_package_data=True,
    
    '''
    This is not a enssential part. It will not affect your package uploading process. 
    But it may affect the discoverability of your package on pypi.org
    Also, it serves as a meta description written by authors for users.
    Here is a full list of what you can put here:
    
    https://pypi.org/classifiers/
    
    '''
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Text Processing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    
    
    '''
    This part specifies all the dependencies of your package. 
    "~=" means the users will need a minimum version number of the dependecies to run the package.
    If you specify all the dependencies here, you do not need to write a requirements.txt separately like many others do.
    '''
    install_requires = [

        'pandas ~= 1.2.4',
        ...

    ],
    
    
    
    '''
    The keywords of your package. It will help users to find your package on pypi.org
    '''
    keywords = ['Text Mining', 'Data Science', ...],
    
)