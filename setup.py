import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

# Read version from MTM/version.py
exec(open('haarcascade/version.py').read())


setuptools.setup(
	name="haar-cascade-nms",
	version=__version__,
	author="Laurent Thomas",
	author_email="laurent132.thomas@laposte.net",
	description="Extend opencv haar-cascade detector with Non-Maxima Supression (NMS)",
	long_description=long_description,
	long_description_content_type="text/markdown",
	keywords="object-recognition object-localization",
	url="https://github.com/LauLauThom/haar-cascade-nms",
	packages=["haarcascade"],
	install_requires=['opencv-python-headless']
	  ],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
		"Topic :: Scientific/Engineering :: Image Recognition",
		"Intended Audience :: Science/Research"		
	],
)