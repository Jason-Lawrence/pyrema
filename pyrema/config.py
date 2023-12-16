from pyrema.base import Config


class ReportConfig(Config):
    """"""

    def __init__(self, config=None, report_options=None):
        """Constructor Method."""
        super().__init__(config)
        self.report_options = {
            "documentclass": 'article',
            "document_options": None,
            "fontenc": 'T1',
            "inputenc": 'utf8',
            "font_size": 'normalsize',
            "lmodern":True,
            "textcomp": True,
            "page_numbers": True,
            "indent": None,
            "geometry_options": None,
            "data": None
        }
        self.config = config

        if report_options:
            self.report_options.update(report_options)