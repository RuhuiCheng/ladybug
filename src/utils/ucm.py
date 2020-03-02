import logging
from pyapollos import ApolloClient
logger = logging.getLogger(__name__)
app_id = "bigdata-dq"
# server_properties
server_properties = '/data/ucm2/settings/server.properties'
env = None
ls_url = None


def get_server_properties():
    global env
    global ls_url
    if env is not None:
        return env, ls_url
    with open(server_properties, 'r') as sp:
        ls_line = sp.readlines()
        ls_url = ls_line[0].strip('\n').split('=')[1].split(',')
        env = ls_line[1].strip('\n').split('=')[1]
        print("==============env, ls_url================{0},{1}".format(env, ls_url))
    return env, ls_url


def get_metadata_dbinfo(_ls_url):

    if (_ls_url is not None) and len(_ls_url) > 0:
        for url in _ls_url:
            try:
                client = ApolloClient(app_id, cluster="default",
                                      config_server_url=url)
                addr = client.get_value('spring.datasource.url', default_val=None,
                                        namespace='db', auto_fetch_on_cache_miss=False)
                user = client.get_value('spring.datasource.username', default_val=None,
                                        namespace='db', auto_fetch_on_cache_miss=False)
                password = client.get_value('spring.datasource.password', default_val=None,
                                            namespace='db', auto_fetch_on_cache_miss=False)
                ls_param = addr.split('/')
                url = ls_param[2].split(':')
                user_pwd = ls_param[3].split('?')
                ls_conn = {
                    'host': url[0],
                    'port':url[1],
                    'user': user,
                    'password': password,
                    'database': user_pwd[0]
                }
                return ls_conn
            except Exception as e:
                logger.error(
                    "run func get_metadata_dbin error trace:{0}".format(e))
