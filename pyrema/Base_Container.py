import pylatex
import pylatex.utils


class Base_Container():
    """
    The base class for the package.

    :param title: The title of the tex object to create.
    :type title: str.
    """

    def __init__(self, title):
        """Constructor Method."""
        self.title = title
        


    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, value):
        self._title = value


    def write_raw(self, content):
        """
        Takes a raw string and writes it to the tex object.

        :param content: The raw string to write.
        :type content: str.
        """
        self.tex.append(pylatex.utils.NoEscape(rf'{content}'))
        self.tex.append(pylatex.NewLine())


    def generate(self, filepath):
        """
        Generate the Tex files at the given location for the tex object.

        :param filepath: The location to write the file.
        :type filepath: str.
        """
        self.tex.generate_tex(filepath=filepath)