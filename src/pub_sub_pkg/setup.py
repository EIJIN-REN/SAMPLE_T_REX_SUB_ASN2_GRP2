from setuptools import find_packages, setup

package_name = 'pub_sub_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eijin',
    maintainer_email='eijin@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'minimal_publisher = pub_sub_pkg.minimal_publisher:main',
            'minimal_subscriber = pub_sub_pkg.subscriber_member_function:main',
        ],
    },
)
