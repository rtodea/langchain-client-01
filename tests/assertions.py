import os


def assert_env(env_var_list):
    for e in env_var_list:
        assert os.environ.get(e, None) is not None
