import Base_Container

import pylatex
import pylatex.utils
import os


class BaseReportSubsection(Base_Container.BaseContainer):
    """

    """

    def __init__(self, title, parent):
        super().__init__(title)
        self.parent = parent
        self.tex = pylatex.Subsection(self.title)


    def generate(self):
        super().generate(filepath=os.path.join(self.parent.subsections_dir, self.title))