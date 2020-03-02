from src.utils import ucm


def test_get_metadata_dbinfo():
    env, ls_url = ucm.get_server_properties()
    conn = ucm.get_metadata_dbinfo(ls_url)
    print(conn)

if __name__ == '__main__':
    test_get_metadata_dbinfo()