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
        self.reports_dir = "Reports"
        self.report_path = self.title
        self.sections_dir = "Sections"
        self.author = author
        self.packages = []
        self.sections = []

        if not os.path.exists(self.reports_dir):
            os.mkdir(self.reports_dir)

        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)

        if not os.path.exists(self.sections_dir):
            os.mkdir(self.sections_dir)


    @property
    def author(self):
        return self._author


    @author.setter
    def author(self, value):
        self._author = value


    @property
    def reports_dir(self):
        return self._reports_dir


    @reports_dir.setter
    def reports_dir(self, value):
        self._reports_dir = os.path.join(os.getcwd(), value)


    @property
    def report_path(self):
        return self._report_path


    @report_path.setter
    def report_path(self, value):
        self._report_path = os.path.join(self.reports_dir, value)


    @property
    def sections_dir(self):
        return self._sections_dir


    @sections_dir.setter
    def sections_dir(self, value):
        self._sections_dir = os.path.join(self.report_path, value)


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


    def create_section(self, section, title):
        """
        Create a section object.

        :param section: The Section to create.
        :type section: :class: BaseReportSection or subclass.
        :param title: The title of the section.
        :type title: str
        :return: The created section object.
        :rtype: :class: BaseReportSection or subclass
        """
        sec = section(title, self)
        self.sections.append(sec)
        return sec


    def input_section(self, section):
        """
        Input the section into the main report Tex file.

        :param section: The section to input.
        :type section: :class: BaseReportSection or subclass.
        """
        self.tex.append(pylatex.Command('input', os.path.join(section.section_dir, f"{section.title}.tex")))#f"Sections/{section.title}/{section.title}.tex")) #


    def generate(self):
        """Generate the Tex file, and compile the PDF."""
        self.tex.generate_pdf(filepath=os.path.join(self.report_path, self.title))
