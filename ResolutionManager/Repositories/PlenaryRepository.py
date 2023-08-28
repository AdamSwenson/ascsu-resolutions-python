from ResolutionManager.Models.Plenaries import Plenary

class PlenaryRepository(object):
    def __init__(self, dao):
        self.dao = dao

    def load_plenary(self, plenary_id):
        result = self.dao.conn.execute(f"select * from plenaries where id = {plenary_id}").fetchone()

        return Plenary(thursday_date=result.thursday_date,
                       first_reading_folder_id=result.first_reading_folder_id,
                       plenary_folder_id=result.plenary_folder_id,
                       feedback_folder_id=result.feedback_folder_id,
                       second_reading_folder_id=result.second_reading_folder_id)

