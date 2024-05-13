class PropertyUtil:
    @staticmethod
    def get_property_string():
        hostname = 'localhost'
        dbname = 'CRS'
        username = 'root'
        password = '0000'
        port = 3306

        connection_string = f"host={hostname} dbname={dbname} user={username} password={password} port={port}"

        return connection_string