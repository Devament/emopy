#!/usr/bin/env bash

if [[ -e /usr/bin/hr ]]; then
    hr cmd pip2_install opencv-python
    hr cmd pip2_install dlib
    hr cmd pip2_install tensorflow
    hr cmd pip2_install h5py
    hr cmd pip2_install keras>=2.0
fi
