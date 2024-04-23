@echo off

echo Installing opencv...
pip install opencv-python

echo Installing deepforest...
pip install deepforest

echo Installing numpy...
pip install numpy

echo Installing scikit-learn...
pip install scikit-learn

echo Pandas...
pip install pandas

echo Checking installation...
python -c "import cv2; print(cv2.__version__)"
python -c "import deepforest; print(deepforest.__version__)"
python -c "import numpy; print(numpy.__version__)"
python -c "import sklearn; print(sklearn.__version__)"
python -c "import pandas; print(pandas.__version__)"

echo Installation complete.
