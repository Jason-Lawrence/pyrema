import Base_Container

import pylatex
import pylatex.utils
import os


class BaseReportSubsection(Base_Container.BaseContainer):
    """

    """

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.tex = pylatex.Subsection(self.title)
        self.child_dir = "Subsubsections" #children_dir
