# 《CONDA 环境配置日志》

## `sage_env`

```bash
conda create -n sage_env python sage
conda activate sage_env
conda install -c conda-forge singular
pip install tqdm
pip install Flask
pip install --upgrade --user snappy
pip install mptrolley
```

## `dcm_env`

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

