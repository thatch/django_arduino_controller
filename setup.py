import setuptools

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup = dict(
    name="django_arduino_controller",
    version="0.1",
    author="Julian Kimmig",
    author_email="julian-kimmig@gmx.net",
    description="app to conrolls arduinos via ArduinoController and PlugInDjango",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JulianKimmig/django_arduino_controller",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
if __name__ == "__main__":
    setuptools.setup(**setup)
