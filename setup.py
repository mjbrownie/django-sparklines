from setuptools import setup, find_packages
setup(name='django-sparklines',
        version='0.1',
        description='Simple tag abstraction for jquery sparklines',
        #long_description=readme,
        author="Michael Brown",
        author_email="mjbrownie@gmail.com",
        packages=find_packages(),
        package_data={'':[
            'templates/sparklines/*',
            ]},
        include_package_data = True,
        zip_safe=False,
        )
