import Base_Container

import pylatex
import pylatex.utils
import os


class BaseReportSection(Base_Container.BaseContainer):
    """Wrapper for the Section object in """


    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.tex = pylatex.Section(self.title)
        self.child_dir = "Subsections" #children_dir
