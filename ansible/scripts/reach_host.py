#!/usr/bin/env python3

def reach_host(module, host, port, timeout):
    nc_path = module.get_bin_path('nc', required=True)
    args = [
        nc_path, '-z', '-w', str(timeout),
        host, str(port)
    ]
    (rc, stdout, stderr) = module.run_command(args)
    return rc == 0


def main():
    module = AnsibleM