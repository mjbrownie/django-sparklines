from setuptools import setup, find_packages
with open('README') as file:
    long_description = file.read()

setup(name='django-sparklines',
        version='0.1',
        description='Simple tag abstraction for jquery sparklines',
        #long_description=readme,
        author="Michael Brown",
        author_email="mjbrownie@gmail.com",
        packages=find_packages(),
        package_data={'':[
            'templates/sparklines/*',
            'static/sparklines/*'
            ]},
        include_package_data = True,
        zip_safe=False,
        long_description=long_description,
        )
