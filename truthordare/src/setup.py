import setuptools


long_description = "My long description"

setuptools.setup(
    name="Truth-Or-Dare",
    version="0.0.1",
    author="Oleksandr Lopasov, Tagir Bektenov",
    author_email="s22672@pjwstk.edu.pl",
    description="Game for the party Truth or Dare",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OleksandrLopasov/PPY_OL_TB_12c",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "nonion==0.4.4",
    ],
)
