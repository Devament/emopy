**EMOPY** 
=========

Emotion recognition package for python using audio-visual data

Setup
-----
```sh
$ pip install git+https://github.com/Selameab/emopy.git
```

OR

```sh
$ git clone https://github.com/Selameab/emopy.git
$ python emopy/setup.py install
```

Demos
-----
Live test using webcam
```sh
$ python demos/webcam.py
```

Demo on test images 
```sh
$ python demos/demo.py
```

Usage
-----
```python
# Get coordinates of faces from the image
faces = emopy.get_faces(frame)

# Get emotion of each face
emotions = emopy.recognize(frame, faces)
```
