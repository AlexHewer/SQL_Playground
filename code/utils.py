'''General functions which are widely applicable to the program'''

def get_config_value(config_type: str) -> str:
    '''Returns the specified config value.
            Parameters:
                    config type (string): The config value to retrieve
            Returns:
                    config value (string): The value to retrieve'''

    file = open('properties/config.txt', 'r')
    contents = file.readlines()
    file.close()

    for line in contents:
        if line.startswith(config_type + "="):
            return line[line.find('=') + 1:].strip()


def write_config_value(config_type: str, new_value: str) -> bool:
    '''Returns the specified config value.
            Parameters:
                    config type (string): The config value to edit
                    new value (string): The new config value to input
            Returns:
                    is updated (bool): True if written successfully'''

    file = open('properties/config.txt', 'r')
    contents: list[str] = file.readlines()
    file.close()

    file = open('properties/config.txt', 'w')
    for line in contents:
        if line.startswith(config_type + "="):
            file.write(line[:line.find('=')+1].strip() + new_value + '\n')
        else:
            file.write(line)
    return True

def create_config():
    '''temp'''
    print("hello")
    #TODO: implement logic
