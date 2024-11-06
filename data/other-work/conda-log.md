# 《CONDA 环境配置日志》

## sage_env

```bash
conda create -n sage_env python sage
conda activate sage_env
conda install -c conda-forge singular
pip install tqdm
pip install Flask
pip install --upgrade --user snappy
pip install mptrolley
```

## dcm_env

```bash
conda create -n dcm_env python
conda activate dcm_env
pip install pydicom
pip install pylibjpeg
pip install pylibjpeg-libjpeg
pip install tqdm
pip install numpy
pip install matplotlib
pip install scipy
pip install scikit-learn
pip install scikit-image
```

## scipy_env

```bash
conda create -n scipy_env python
conda activate scipy_env
pip install numpy
pip install matplotlib
pip install pillow
pip install scipy
```

## vtk_env

```bash
conda create -n vtk_env python
conda activate vtk_env
conda install -c conda-forge vtk
pip install opencv-python
```

## tf_gpu_env

- 目前这个环境还有很严重的问题
- 基本上是跑不起来的，而且 GPU 也不可用

```bash
conda create -n tf_gpu_env python==3.9
conda install tensorflow==2.18.0
pip install keras==3.5.0
pip install scikit-learn
conda install nltk
```

