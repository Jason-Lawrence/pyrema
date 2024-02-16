import pylatex
import pylatex.utils

import os


class Config():
    """"""

    def __init__(self, config):
        """Constructor Method."""
        self.config = config
        self.children = {}


    @property
    def config(self):
        return self._config


    @config.setter
    def config(self, config):
        self._config = config


    def add_child(self, child, config):
        """
        Add a child to the parent configuration.

        :param child: The child to add.
        :type child: :class: pyrema.report.Section or subclass.
        :param config: The child's configuration.
        :type config: :class: pyrema.base.Config or subclass.
        """
        self.children[child] = config


    def delete_child(self, child):
        """
        Delete the child from the configuration.

        :param child: The child to delete.
        :type child: pyrema.report.Section or subclass.
        """
        if child in self.children.keys():
            del self.children[child]


class Container():
    """
    The base class for the package.

    :param title: The title of the tex object to create.
    :type title: str.
    """

    def __init__(self, title, config=None, parent=None, child_dir=None):
        """Constructor Method."""
        self.title = title
        self.parent = parent
        self.dir = self.title
        self.config = config
        self.children = []
        self.child_dir = child_dir

        if not os.path.exists(self.dir) and not self.parent:
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
        if child:
            self._child_dir = os.path.join(self.dir, child)

        else:
            self._child_dir = None


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

        child = child_class(title, parent=self)
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
