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
        copy_title = 'Copy Title'
        body = {
            'name': copy_title
        }
        try:
            drive_response = self.service.files().copy(
                fileId=document_id, body=body).execute()
            document_copy_id = drive_response.get('id')
            print(f"Copied document. New doc id : {document_copy_id}")
            return document_copy_id;
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')

    def move_file_to_folder(self, file_id, folder_id):
        """Move specified file to the specified folder.
        Args:
            file_id: Id of the file to move.
            folder_id: Id of the folder
        Print: An object containing the new parent folder and other meta data
        Returns : Parent Ids for the file
        """
        try:
            # pylint: disable=maybe-no-member
            # Retrieve the existing parents to remove
            file = self.service.files().get(fileId=file_id, fields='parents').execute()
            previous_parents = ",".join(file.get('parents'))
            # Move the file to the new folder
            file = self.service.files().update(fileId=file_id, addParents=folder_id,
                                          removeParents=previous_parents,
                                          fields='id, parents').execute()
            print(f"new parent id: {file.get('parents')}")
            return file.get('parents')

        except HttpError as error:
            print(F'An error occurred: {error}')
            return None


# https://docs.google.com/document/d/document_id/edit
# copy_title = 'Copy Title'
# body = {
#     'name': copy_title
# }
# drive_response = drive_service.files().copy(
#     fileId=document_id, body=body).execute()
# document_copy_id = drive_response.get('id')
