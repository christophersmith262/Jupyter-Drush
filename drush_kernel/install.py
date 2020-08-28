import json
import os
import sys
import argparse
import re

kernel_json_template = {
  "argv": [sys.executable, "-m", "drush_kernel", "-f", "{connection_file}"],
  "display_name": "Drush",
  "language": "php",
  "env": {},
}

def install_my_kernel_spec(name, kernel_json, user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755) # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        # TODO: Copy resources once they're specified

        print('Installing IPython kernel spec')
        KernelSpecManager().install_kernel_spec(td, name, user=user, prefix=prefix)

def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Install KernelSpec for Drush Kernel'
    )
    prefix_locations = parser.add_mutually_exclusive_group()

    prefix_locations.add_argument(
        '--user',
        help='Install KernelSpec in user homedirectory',
        action='store_true'
    )
    prefix_locations.add_argument(
        '--sys-prefix',
        help='Install KernelSpec in sys.prefix. Useful in conda / virtualenv',
        action='store_true',
        dest='sys_prefix'
    )
    prefix_locations.add_argument(
        '--prefix',
        help='Install KernelSpec in this prefix',
        default=None
    )

    parser.add_argument(
        '--drush-path',
        help='Specify the path to drush',
        default='drush'
    )

    parser.add_argument(
        '--drush-alias',
        help='Specify the drush alias to connect with',
        required=True
    )

    parser.add_argument(
        '--drush-alias',
        help='Specify the drush alias to connect with',
        default='@local'
    )

    args = parser.parse_args(argv)

    display_name = "Drush: " + args.drush_alias

    re = re.compile('[^a-zA-Z_\- ]')
    machine_name = display_name.lower()
    machine_name = re.sub('', machine_name)

    user = False
    prefix = None
    if args.sys_prefix:
        prefix = sys.prefix
    elif args.prefix:
        prefix = args.prefix
    elif args.user or not _is_root():
        user = True

    kernel_json = kernel_json_template
    kernel_json['display_name'] = display_name

    install_my_kernel_spec(machine_name, kernel_json, user=user, prefix=prefix)

if __name__ == '__main__':
    main()
