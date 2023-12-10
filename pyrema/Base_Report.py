import Base_Container

import pylatex
import pylatex.utils

import os


class BaseReport(Base_Container.BaseContainer):
    """
    Base Report class. Manages the file tree for the Tex files.

    :param title: Title of the Report.
    :type title: str.
    :param author: Author of the Report.
    :type author: str.
    """

    def __init__(self, title, author):
        """Constructor Method"""
        super().__init__(title)
        self.child_dir = "Sections"
        self.author = author
        self.packages = []

        if not os.path.exists(os.path.join(os.getcwd(), "Reports")):
            os.mkdir(os.path.join(os.getcwd(), "Reports"))


    @property
    def author(self):
        return self._author


    @author.setter
    def author(self, value):
        self._author = value


    def add_package(self, package):
        """
        Add Package to the Preamble.

        :param package: The name of the package to add.
        :type package: str.
        """
        self.tex.preamble.append(pylatex.Package(package))
        self.packages.append(package)


    def make_doc(self):
        """Create the Report Document."""
        self.tex = pylatex.Document(geometry_options={
            "margin": "2.2cm",
            "includeheadfoot": True
        })


    def make_preamble(self):
        """Make the preamble of the Report."""

        self.add_package('titletoc')

        self.add_package('hyperref')


    def add_newpage(self):
        """Start new page."""
        self.tex.append(pylatex.NewPage())


    def add_toc(self):
        """Add table of contents to the report."""
        self.write_raw("\tableofcontents")


    def add_lof(self):
        """Add list of figures to the report."""
        self.write_raw("\listoffigures")


    def add_lot(self):
        """Add list of tables to the report."""
        self.write_raw("\listoftables")


    def write_title(self):
        self.write_raw("\maketitle")


    def generate(self):
        """Generate the Tex file, and compile the PDF."""
        self.tex.generate_pdf(filepath=os.path.join(self.dir, self.title))
