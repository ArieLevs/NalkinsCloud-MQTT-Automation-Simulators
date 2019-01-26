import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nalkinscloud-mqtt-simulators",
    version="0.1.1",
    author="Arie Lev",
    author_email="levinson.arie@gmail.com",
    description="Simulate MQTT end devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArieLevs/Nalkinscloud-MQTT-Simulators",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'mqtt-simulate.py = src.start_service:main'
        ],
    },
)
