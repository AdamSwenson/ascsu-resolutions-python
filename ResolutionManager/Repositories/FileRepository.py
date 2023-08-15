import ResolutionManager.environment as env

from ResolutionManager.API.CredentialsManager import CredentialsManager

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class FileRepository(object):

    def __init__(self):
        self.cred_manager = CredentialsManager()
        self.service = build('drive', 'v3', credentials=self.cred_manager.creds)

    def create_folder(self, folder_name):
        """ Create a folder and prints the folder ID
        Returns : Folder Id

        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
        Based on : https://developers.google.com/drive/api/quickstart/python
        """
        # creds, _ = google.auth.default()

        try:
            # create drive api client
            # service = build('drive', 'v3', credentials=creds)
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }

            # pylint: disable=maybe-no-member
            file = self.service.files().create(body=file_metadata, fields='id'
                                          ).execute()
            print(F'Folder ID: "{file.get("id")}".')
            return file.get('id')

        except HttpError as error:
            print(F'An error occurred: {error}')
            return None

    def list_folders(self):
        pass

    def list_files(self):
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        try:
            # Call the Drive v3 API
            results = self.service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
                return
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')



    def copy_file(self, document_id):
        pass

    def move_file(self, destination_id, document_id):
        pass

# https://docs.google.com/document/d/document_id/edit
# copy_title = 'Copy Title'
# body = {
#     'name': copy_title
# }
# drive_response = drive_service.files().copy(
#     fileId=document_id, body=body).execute()
# document_copy_id = drive_response.get('id')
