import ResolutionManager.environment as env

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.ResolutionTemplateRespository import ResolutionTemplateRepository
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Committees import Committee
from ResolutionManager.Models.Resolutions import Resolution

def main():
    resolution_name = "Opposing the existence of the CO"
    resolution_number = 3456
    # resolution = Resolution(resolution_number, resolution_name)

    committee = Committee('Faculty Affairs', 'FA')
    cosponsors = [ Committee('Academic Affairs', 'AA')]

    plenary = Plenary(year=2023,
                      month='September',
                      thursday_date=12,
                      friday_date=14,
                      first_reading_folder_id='1sv_4BUV5fk6Kcjss8HeSCJWnsLZJVpKC'
                      )



    template_repo = ResolutionTemplateRepository(plenary=plenary)

    new_rez_id = template_repo.create_file_from_template(plenary.first_reading_folder_id, resolution_number, resolution_name)
    template_repo.update_title(new_rez_id, resolution_name)
    template_repo.update_header(new_rez_id, resolution_number, committee, cosponsors)


if __name__ == '__main__':
    main()
