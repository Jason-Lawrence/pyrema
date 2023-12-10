import Base_Container

import pylatex
import pylatex.utils
import os


class BaseReportSubsubsection(Base_Container.BaseContainer):
    """"""

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.tex = pylatex.Subsubsection(self.title)
        self.dir = None
        self.child_dir = None


    def generate(self):
        self.tex.generate_tex(filepath=os.path.join(self.parent.child_dir, self.title))
