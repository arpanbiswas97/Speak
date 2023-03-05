from setuptools import setup

setup(
    name="speak",
    version="0.1.1",
    description="Speaks the text out loud using Google Text-to-Speech",
    author="Arpan Biswas",
    author_email="arpanbiswas97.com",
    install_requires=["pygame", "gtts"],
    entry_points={"console_scripts": ["speak=speak:main"]},
)
