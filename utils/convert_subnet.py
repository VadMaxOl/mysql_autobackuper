import socket
import struct
from subnet_info import SubnetInfo

# Convert Subnet Mask To CIDR: 255.255.255.0 -> 24
def netmask_to_cidr(subnetmask_input: str) -> str:
    _subnet = SubnetInfo()
    value = _subnet.calculate_cidr(subnet_mask=str(subnetmask_input))
    return value

# Convert CIDR To Subnet Mask: 24 -> 255.255.255.0
def cidr_to_subnetmask(cidr_input: str) -> str:
    host_bits = 32 - int(cidr_input)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return netmask