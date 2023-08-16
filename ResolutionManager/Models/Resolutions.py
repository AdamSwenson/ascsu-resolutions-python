from ResolutionManager.Models.Committees import Committee


class Resolution(object):

    def __init__(self, number, title, document_id=None, committee: Committee = None, cosponsors=[]):
        """
        :param number:
        :param title:
        :param document_id: Google Drive id
        """
        self.committee = committee
        self.cosponsors = cosponsors
        self.document_id = document_id
        self.title = title
        self.number = number

    @property
    def name(self):
        return self.title
