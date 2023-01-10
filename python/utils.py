
def get_config_value(config_type: str) -> str:
    '''Returns the specified config value.
            Parameters:
                    config type (string): The config value to retrieve
            Returns:
                    config value (string): The value to retrieve'''

    file = open('config.txt', 'r')
    contents = file.readlines()

    for line in contents:
        if line.startswith(config_type + "="):
            return line[line.find('=') + 1:].strip()