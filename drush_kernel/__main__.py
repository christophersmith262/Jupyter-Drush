from ipykernel.kernelapp import IPKernelApp
from .kernel import AcquiaKernel
IPKernelApp.launch_instance(kernel_class=AcquiaKernel)
