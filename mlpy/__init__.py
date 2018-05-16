import sys
from .version import v as __version__

# extension modules
from . import gsl
from .libsvm import *
from .liblinear import *
from .libml import *
from .findpeaks import *
from .kmeans import *
from .kernel import *
from .adatron import *
from .canberra import *
from .dtw import *
from .lcs import *

# python modules
from .crossval import *
from .hcluster import *
from .metrics import *
from .perceptron import *
from .da import *
from .ols import *
from .ridge import *
from .bordacount import *
from .lars import *
from .elasticnet import *
from .dimred import *
from .irelief import *
from .parzen import *
from .stats import *
from .fastcluster import *
from .kernel_class import *
from .rfe import *
from .golub import *
from .pls import *

from . import crossval
from . import hcluster
from . import metrics
from . import perceptron
from . import da
from . import ols
from . import ridge
from . import bordacount
from . import lars
from . import elasticnet
from . import dimred
from . import irelief
from . import parzen
from . import stats
from . import fastcluster
from . import kernel_class
from . import rfe
from . import golub
from . import pls

# visible submodules
from . import wavelet

__all__ = []
__all__ += crossval.__all__
__all__ += hcluster.__all__
__all__ += metrics.__all__
__all__ += perceptron.__all__
__all__ += da.__all__
__all__ += ols.__all__
__all__ += ridge.__all__
__all__ += bordacount.__all__
__all__ += lars.__all__
__all__ += elasticnet.__all__
__all__ += dimred.__all__
__all__ += irelief.__all__
__all__ += parzen.__all__
__all__ += stats.__all__
__all__ += fastcluster.__all__
__all__ += kernel_class.__all__
__all__ += rfe.__all__
__all__ += golub.__all__
__all__ += pls.__all__

__all__ += ['LibLinear']
__all__ += ['LibSvm']
__all__ += ['findpeaks_dist', 'findpeaks_win']
__all__ += ['kmeans']
__all__ += [
    'kernel_linear', 'kernel_gaussian', 'kernel_polynomial',
    'kernel_exponential', 'kernel_sigmoid', 'kernel_center'
]
__all__ += ['KernelAdatron']
__all__ += [
    'canberra', 'canberra_location', 'canberra_stability',
    'canberra_location_expected', 'canberra_location_max',
    'canberra_stability_max'
]
__all__ += ['KNN', 'ClassTree', 'MaximumLikelihoodC']
__all__ += ['dtw_std', 'dtw_subsequence']
__all__ += ['lcs_std', 'lcs_real']
