import pylatex
import pylatex.utils

import os


class BaseContainer():
    """
    The base class for the package.

    :param title: The title of the tex object to create.
    :type title: str.
    """

    def __init__(self, title, parent=None):
        """Constructor Method."""
        self.title = title
        self.parent = parent
        self.dir = self.title
        self.children = []

        if not os.path.exists(self.dir) and self.child_dir:
            os.mkdir(self.dir)


    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, value):
        self._title = value


    @property
    def parent(self):
        return self._parent


    @parent.setter
    def parent(self, parent):
        self._parent = parent


    @property
    def dir(self):
        return self._dir


    @dir.setter
    def dir(self, value):
        if self.parent:
            self._dir = os.path.join(self.parent.child_dir, value)

        else:
            self._dir = os.path.join(f"{os.getcwd()}/Reports", value)


    @property
    def child_dir(self):
        return self._child_dir


    @child_dir.setter
    def child_dir(self, child):
        self._child_dir = os.path.join(self.dir, child)


    def delete_child(self, child):
        """Deletes child item."""
        if child in self.children:
            self.children.remove(child)

        if not self.children:
            os.rmdir(self.child_dir)


    def create_child(self, child_class, title):
        """Creates a child object of the child class."""
        if not os.path.exists(self.child_dir):
            os.mkdir(self.child_dir)

        child = child_class(title, self)
        self.children.append(child)
        return child


    def input_child(self, child):
        """Insert the content of the child into the parent."""
        self.tex.append(pylatex.Command('input', os.path.join(child.dir, f"{child.title}.tex")))


    def write(self, config):
        """Read in a Configuration and create the sections, call the sections write function and pass in that sections configuration."""
        pass


    def write_raw(self, content):
        """
        Takes a raw string and writes it to the tex object.

        :param content: The raw string to write.
        :type content: str.
        """
        self.tex.append(pylatex.utils.NoEscape(rf'{content}'))
        self.tex.append(pylatex.NewLine())


    def generate(self):
        """
        Generate the Tex files at the given location for the tex object.

        :param filepath: The location to write the file.
        :type filepath: str.
        """
        self.tex.generate_tex(filepath=os.path.join(self.dir, self.title))
