import ResolutionManager.environment as env
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository

from ResolutionManager.API.CredentialsManager import CredentialsManager

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

HEADER_TEMPLATE = "AS-{resolution_number}-{year}/{committee}"

class ResolutionTemplateRepository(object):

    def __init__(self, plenary=None):
        self.plenary = plenary
        self.doc_repo = DocumentRepository()
        self.file_repo = FileRepository()
        self.cred_manager = CredentialsManager()
        self.service = build('docs', 'v1', credentials=self.cred_manager.creds)

    def update_title(self, document_id, title):
        title_idxs = {'start_index': 54, 'end_index': 62}
        rez_number = {'start_index': 54, 'end_index': 62}

        title_start = title_idxs['start_index'] - 1
        title_end = title_idxs['start_index'] + len(title)


        # Make sure to order backwards so offsets don't change
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': title_start,
                    },
                    'text': title

                }
            },

            {
                'updateTextStyle': {
                    'range': {
                        'startIndex': title_start,
                        'endIndex': title_end
                    },
                    'textStyle': {
                        'bold': True,
                    },
                    'fields': 'bold,'
                }
            },
            {
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': title_start,
                        'endIndex': title_end
                    },
                    'paragraphStyle': {
                        'alignment': 'CENTER'
                    },
                    'fields': 'alignment'
                }
            },

            {
                'deleteContentRange': {
                    'range': {
                        'startIndex': title_end,
                        'endIndex': title_end + 1 + len('[Title]'),
                    }
                }},

        ]

        result = self.service.documents().batchUpdate(
            documentId=document_id, body={'requests': requests}).execute()

        return result

    def create_file_from_template(self, resolution, template_id=env.TEMPLATE_DOCUMENT_ID):
        # def create_file_from_template(self, folder_id, resolution_number, resolution_name,
        #                               template_id=env.TEMPLATE_DOCUMENT_ID):
        """Uses the template to make a new resolution in the first readings folder
        returns Resolution object with document id of created resolution set
        """
        filename = env.RESOLUTION_FILENAME_TEMPLATE.format(resolution_number=resolution.number,
                                                           resolution_name=resolution.title)
        resolution.document_id = self.file_repo.copy_file(template_id, filename)

        self.file_repo.move_file_to_folder(resolution.document_id, self.plenary.first_reading_folder_id)
        return resolution


    def make_header(self, resolution_number, year, committee, cosponsors=[]):
        if year > 2000:
            year = year - 2000

        v = HEADER_TEMPLATE.format(resolution_number=resolution_number, year=year, committee=committee.abbreviation)
        if len(cosponsors) > 0:
            for c in cosponsors:
                v += f"/{c.abbreviations}"
        return v


    def update_header(self, document_id, resolution_number, committee, cosponsors=[]):
        txt = f"{self.make_header(resolution_number, self.plenary.year, committee, cosponsors)}\n{self.plenary.formatted_plenary_date()}"

        requests = [{
            "insertText": {
                "location": {
                 "segmentId": env.TEMPLATE_HEADER_ID,
                "index": 0
            },
            "text": txt
        }
        }]
        # requests = [
        #     {
        #         "createHeader": {
        #             "sectionBreakLocation": {
        #                 "index": 0
        #             },
        #             "type": "DEFAULT"
        #         }
        #     },
        # ]

        result = self.service.documents().batchUpdate(
            documentId=document_id, body={'requests': requests}).execute()

        print(result)


