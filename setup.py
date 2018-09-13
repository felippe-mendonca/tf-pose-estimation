from setuptools import setup, Extension
import numpy

pafprocess=Extension('_pafprocess',                         \
    ['tf_pose_estimation/pafprocess/pafprocess.cpp',        \
     'tf_pose_estimation/pafprocess/pafprocess.i'],         \
    swig_opts=['-c++'],                                     \
    depends=["tf_pose_estimation/pafprocess/pafprocess.h"], \
    include_dirs=[numpy.get_include()]) 

setup(
    name='tf_pose_estimation',
    version='0.2',
    description='',
    ext_modules=[pafprocess],
    packages=[
        'tf_pose_estimation',
        'tf_pose_estimation.pafprocess',
        'tf_pose_estimation.pycocotools',
        'tf_pose_estimation.slidingwindow',
        'tf_pose_estimation.slim',
        'tf_pose_estimation.slim.nets',
        'tf_pose_estimation.slim.datasets',
        'tf_pose_estimation.slim.deployment',
        'tf_pose_estimation.slim.preprocessing',
        'tf_pose_estimation.tensblur'
    ],
    install_requires=['opencv-python==3.3.1.*', 'psutil==5.4.5'],
    zip_safe=False
)