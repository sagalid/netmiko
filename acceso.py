import conf
from netmiko import Netmiko


def main():
    net_connect = Netmiko(
         conf.host,
         username=conf.username,
         password=conf.password,
         device_type=conf.device_type,
    )

    # command = "show ip int brief"
    # command = "show interfaces description"
    command = "show mac-address-table"

    print()
    print(net_connect.find_prompt())
    output = net_connect.send_command(command)
    type(output)
    net_connect.disconnect()
    print(output)
    print()


if __name__ == "__main__":
    main()
