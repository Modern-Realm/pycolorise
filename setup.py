import re
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("pycolorise/__init__.py") as f:
    search_v = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)

    if search_v is not None:
        version = search_v.group(1)
    else:
        raise RuntimeError(
            "Error occurred while installing !\n"
            "go to https://github.com/Modern-Realm/pycolorise for more info ...")

packages = [
    "pycolorise",
    "pycolorise.colors",
    "pycolorise.bgColors"
]

setuptools.setup(
    name="pycolorise",
    version=version,
    author="P. Sai Keerthan Reddy",
    author_email="saikeerthan.keerthan.9@gmail.com",
    description="Add colors to the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Modern-Realm/pycolorise",
    project_urls={
        "Documentation": "https://modern-realm.github.io/pycolorise/",
        "Bug Tracker": "https://github.com/Modern-Realm/pycolorise/issues",
        "Examples": "https://github.com/Modern-Realm/pycolorise/tree/main/Examples",
        "Source": "https://github.com/Modern-Realm/pycolorise/tree/main/package/pycolorise",
        "Discord Server": "https://discord.gg/GVMWx5EaAN",
    },
    keywords=["colors", "terminal colors", "pycolorise"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    license="MIT",
    packages=packages,
    include_package_data=True,
    python_requires=">=3.7"
)
