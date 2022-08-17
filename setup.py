import setuptools

setuptools.setup(
    name="asrs",
    version="0.0.0",
    packages=setuptools.find_packages(),
    install_requires=["typer"],
    entry_points="""
    [console_scripts]
    asr=cli:app
    """,
)
