import unittest

from pyrema.report import (
    Report,
    Section,
    Subsection,
    Subsubsection
)
import os

def get_base_path():
    return os.path.join(f"{os.getcwd()}/Reports")

def get_path(path, loc):
    return os.path.join(path, loc)

def create_report():
    return Report("Test Report", "Tester")


class TestReport(unittest.TestCase):
    """"""

    def test_create_report(self):
        """"""
        title = "Test Report"
        author = "Tester"

        report = Report(title, author)

        self.assertEqual(title, report.title)
        self.assertEqual(author, report.author)

        base_path = get_base_path()
        sections_path = get_path(get_path(base_path, title), "Sections")

        self.assertEqual(sections_path, report.child_dir)

    def test_create_section(self):
        """"""
        report = create_report()
        sec = report.create_child(Section, "Test Section")

        self.assertEqual(sec.title, "Test Section")
        self.assertIn(sec, report.sections)
