from setuptools import setup

package_name = 'cclehui_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cclehui',
    maintainer_email='chenlehui@example.com',
    description='cclehui_test',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cclehui_test_node = cclehui_test.cclehui_test_node:main',
            'topic_pub_node = cclehui_test.topic_pub_node:main',
            'topic_sub_node = cclehui_test.topic_sub_node:main',
            'service_server_node = cclehui_test.service_server_node:main',
            'service_client_node = cclehui_test.service_client_node:main',
        ],
    },
)
