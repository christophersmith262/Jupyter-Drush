# A Jupyter kernel for Drush

This requires IPython 3.

## To install::

```
    pip install drush_kernel
    python -m drush_kernel.install --drush-alias=@mysite.local
```

## To use it, run one of:

```
    jupyter notebook
    # In the notebook interface, select Bash from the 'New' menu
    jupyter qtconsole --kernel drush_mysite_local
    jupyter console --kernel drush_mysite_local
```

For details of how this works, see the Jupyter docs on `wrapper kernels
<http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html>`_, and
Pexpect's docs on the `replwrap module
<http://pexpect.readthedocs.org/en/latest/api/replwrap.html>`_
