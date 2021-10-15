from application_services.base_application_resource import BaseRDBApplicationResource
import database_services.RDBService as d_service


class OHResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'ohdb', 'OfficeHours'
