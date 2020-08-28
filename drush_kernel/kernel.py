import os
from bash_kernel.kernel import BashKernel

drush_path = os.environ.get('DRUSH_PATH', 'drush')
alias = os.environ.get('DRUSH_ALIAS', '@local')

class AcquiaKernel(BashKernel):

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        return BashKernel.do_execute(self, drush_path + ' ' + alias + ' ev "' + code.replace('"', '\\"').replace('$', '\\$') + '"', silent, store_history, user_expressions, allow_stdin)

if __name__ == '__main__':
    IPKernelApp.launch_instance(kernel_class=AcquiaKernel)
