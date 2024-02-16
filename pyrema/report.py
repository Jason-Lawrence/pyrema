import pylatex
import pyrema.base
import os
import pyrema.config

class Section(pyrema.base.Container):
    """Wrapper for the Section object in """

    def __init__(self, title, config=None, parent=None):
        super().__init__(title, config=config, parent=parent)
        self.tex = pylatex.Section(self.title)
        self.child_dir = "Subsections" #children_dir


class Subsection(pyrema.base.Container):
    """

    """

    def __init__(self, title, config, parent):
        super().__init__(title, config, parent)
        self.tex = pylatex.Subsection(self.title)
        self.child_dir = "Subsubsections" #children_dir


class Subsubsection(pyrema.base.Container):
    """

    """

    def __init__(self, title, config, parent):
        super().__init__(title, config, parent)
        self.tex = pylatex.Subsubsection(self.title)
        self.dir = None
        self.child_dir = None


    def generate(self):
        self.tex.generate_tex(filepath=os.path.join(self.parent.child_dir, self.title))


class Report(pyrema.base.Container):
    """
    Base Report class. Manages the file tree for the Tex files.

    :param title: Title of the Report.
    :type title: str.
    :param author: Author of the Report.
    :type author: str.
    """

    def __init__(self, title, author, config=pyrema.config.ReportConfig()):
        """Constructor Method"""
        super().__init__(title, config)
        self.child_dir = "Sections"
        self.author = author
        self.packages = []

        if not os.path.exists(os.path.join(os.getcwd(), "Reports")):
            os.mkdir(os.path.join(os.getcwd(), "Reports"))


    def __str__(self):
        return f"Report: {self.title}, By {self.author}"

    def __repr__(self):
        return f"Report({self.title}, {self.author})"

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
        self.tex = pylatex.Document(**self.config.report_options)


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