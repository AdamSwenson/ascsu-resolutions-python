from ResolutionManager.Repositories.FileRepository import FileRepository
import ResolutionManager.environment as env

PLENARY_FOLDER_TEMPLATE = "{year} {month}"
RESOLUTIONS_ROOT_NAME = 'Resolutions'
FIRST_READING_FOLDER_NAME = 'First reading'
ACTION_FOLDER_NAME = 'Action items'


def main():
    file_repo = FileRepository()

    # todo Check if folder already exists
    plenary_folder_name = PLENARY_FOLDER_TEMPLATE.format(year=2023, month='September')
    plenary_root_folder_id = file_repo.create_folder(plenary_folder_name)
    file_repo.move_file_to_folder(plenary_root_folder_id, env.GOOGLE_DRIVE_ROOT_FOLDER_ID)

    # Make subfolders
    first_reading_folder_id = file_repo.create_folder(FIRST_READING_FOLDER_NAME)
    file_repo.move_file_to_folder(first_reading_folder_id, plenary_root_folder_id)
    second_reading_folder_id = file_repo.create_folder(ACTION_FOLDER_NAME)
    file_repo.move_file_to_folder(second_reading_folder_id, plenary_root_folder_id)

    print("created folders ")
    print(f"Plenary folder id : {plenary_root_folder_id} \n First readings folder id : {first_reading_folder_id} \n Second reading folder id : {second_reading_folder_id}")

if __name__ == '__main__':
    main()
