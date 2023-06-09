from setuptools import setup
import os
from glob import glob

package_name = 'ros2_course'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
    	(os.path.join('share', package_name),
        glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lex',
    maintainer_email='lex@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [            
            'fractal = ros2_course.fractal_turtle:main',
            'turtle = ros2_course.turtle:main',
            'listener = ros2_course.turtle_listener:main',
            'talker = ros2_course.talker:main',
            'hello = ros2_course.hello:main',
            'turtlesim_controller = ros2_course.turtlesim_controller:main',
            'psm_controller = ros2_course.psm_grasp:main',
            'dragon = ros2_course.dragon_fractal_turtle:main'
        ],
    },
)
