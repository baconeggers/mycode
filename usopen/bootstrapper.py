from netmiko import ConnectHandler

def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
    # create a connection to the switch
    # pass the location of a config file
    try:
        # open the config file
        config_file = open(config, "r")
        
        # netmiko needs the content of our config file
        # SPLIT into lines
        config_lines = config_file.read().splitlines()

        # config_lines is a LIST: each line of the config file is one element

        # open a connection to the switch
        open_connection = ConnectHandler(device_type=dev_type,
                                        ip=dev_ip,
                                        username=dev_un,
                                        password=dev_pw)
        # we need a higher level of privilege
        # giving our connection "admin "
        open_connection.enable()

        # passing a config to a switch        
        open_connection.send_config_set(config_lines)

        # you must save your work!
        open_connection.send_command_expect('write memory')

        open_connection.disconnect()
        
        return True
    except:
        return False