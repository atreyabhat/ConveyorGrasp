from setuptools import find_packages, setup

package_name = 'pandarobotmove'

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
    maintainer='vishwas',
    maintainer_email='vishwas@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'pandarobotmove = pandarobotmove.panda_pnp:main',
                            'pandarobotcloseloop = pandarobotmove.panda_closeloop:main',
                            'pandarobotcloselooperror = pandarobotmove.panda_closeloop_error:main',
                            'pandarobotcloseloopyolo = pandarobotmove.panda_closeloop_yolo:main',
        ],
    },
)
