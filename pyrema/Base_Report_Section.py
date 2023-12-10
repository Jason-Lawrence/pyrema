import Base_Container

import pylatex
import pylatex.utils
import os


class BaseReportSection(Base_Container.BaseContainer):
    """Wrapper for the Section object in """


    def __init__(self, title, parent):
        super().__init__(title)
        self.parent = parent
        self.tex = pylatex.Section(self.title)
        self.section_dir = self.title
        self.subsections_dir = "Subsections"
        self.subsections = []

        if not os.path.exists(self.section_dir):
            os.mkdir(self.section_dir)


    @property
    def section_dir(self):
        return self._section_dir

    @section_dir.setter
    def section_dir(self, value):
        self._section_dir = os.path.join(self.parent.sections_dir, value)


    @property
    def subsections_dir(self):
        return self._subsections_dir


    @subsections_dir.setter
    def subsections_dir(self, value):
        self._subsections_dir = os.path.join(self.section_dir, value)


    def delete_subsection(self, subsection):
        """Delete a subsection."""
        if subsection in self.subsections:
            self.subsections.remove(subsection)

        if not self.subsections: # if empty
            os.rmdir(self.subsections_dir)




    def create_subsection(self, subsection, title):
        """Create a subsection."""
        if not os.path.exists(self.subsections_dir):
            os.mkdir(self.subsections_dir)
            
        sub = subsection(title, self)
        self.subsections.append(sub)
        return sub


    def input_subsection(self, subsection):
        """
        Input the subsection into the Section.

        :param subsection: The subsection to input.
        :type subsection: :class: BaseReportSubsection
        """
        self.tex.append(pylatex.Command('input', f"Sections/{self.title}/Subsections/{subsection.title}.tex"))


    def generate(self):
        super().generate(filepath=os.path.join(self.section_dir, self.title))