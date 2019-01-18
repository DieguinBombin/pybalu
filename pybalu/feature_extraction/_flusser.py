__all__ = ['flusser', 'FlusserExtractor']
from ._flusser_c import flusser as _flusser
from ._feature_extractor import FeatureExtractorBase


def flusser(image, show=False, labels=False):
    '''\
flusser(image, *, show=False, labels=False)

Return an array of with the the four Flusser moments extracted from a binary image.

Parameters
----------
image : a numpy 2 dimensional int array
    It represents a binary image. Non binary arrays will return nonsensical results.
show : bool, optional
    Wether to print or not messages during execution
labels : bool, optional
    Wether to return a second array that contains the label of each value. 

Returns
-------
labels: ndarray, optional
    A one dimensional string ndarray that contains the labels to each of the features.
    This array is only returned if `labels` is set to True.
features: ndarray
    A float ndarray that contains all 4 Flusser moments extracted from the image.

See Also
--------
fit_ellipse : <Not Implemented Yet>
gupta : Extract the three Gupta moments from binary image.
hugeo : Extract the seven Hu moments from a binary image.
standard : <Not Implemented Yet>

Examples
--------
Load an image and get its binary representation, then proceed to get its features:

>>> from pybalu.feature_extraction import flusser
>>> from pybalu.img_processing import segbalu
>>> from pybalu.misc import imread
>>> img = imread('testimg.png')
>>> binary_img, _, _ = segbalu(img)
>>> features = flusser(binary_img)

Print a binary image features:

>>> from pybalu.IO import print_features
>>> labels, features = flusser(binary_img, labels=True)
>>> print_features(labels, features)
Flusser-moment 1:  0.03429
Flusser-moment 2: -0.00000
Flusser-moment 3: -0.00009
Flusser-moment 4:  0.00003
'''
    return _flusser(image, show=show, labels=labels)

class FlusserExtractor(FeatureExtractorBase):
    extractor_func = flusser