import pylatex
import base
import os

class Section(base.Container):
    """Wrapper for the Section object in """

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.tex = pylatex.Section(self.title)
        self.child_dir = "Subsections" #children_dir


class Subsection(base.Container):
    """

    """

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.tex = pylatex.Subsection(self.title)
        self.child_dir = "Subsubsections" #children_dir


class Subsubsection(base.Container):
    """

    """

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.tex = pylatex.Subsubsection(self.title)
        self.dir = None
        self.child_dir = None


    def generate(self):
        self.tex.generate_tex(filepath=os.path.join(self.parent.child_dir, self.title))


class Report(base.Container):
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
        self.add_newpage()


    def generate(self):
        """Generate the Tex file, and compile the PDF."""
        self.tex.generate_pdf(filepath=os.path.join(self.dir, self.title))