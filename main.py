# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from ResolutionManager import environment as env
from ResolutionManager.API.CredentialsManager import CredentialsManager
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository

# import environment as env

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # doc_repo = DocumentRepository()
    #
    # doc_repo.create_file('test 6')
    # print_hi('PyCharm')
    #
    file_repo = FileRepository()
    # file_repo.list_files()

    file_repo.create_folder('ascsu testing')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
