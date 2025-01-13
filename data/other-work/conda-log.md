# 《CONDA 环境配置日志》

- **请注意：此文件为公开文件**。建议按照名称字典序整理。

## 删除一个虚拟环境

```bash
conda remove --name <虚拟环境名> --all
```

## base

```bash
conda activate base
pip install cryptography # 用于 neko load_crypto
pip install build twine  # 用于 pypi 打包
pip install markdown2    # 用于日志 html 的渲染
```

## dcm_env

```bash
conda create -n dcm_env python
conda activate dcm_env
conda install -c conda-forge vtk
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

## flask_env

```bash
conda create -n flask_env python
conda activate flask_env
pip install flask
```

## google_env

- 参考：https://pypi.org/project/google-generativeai/

```bash
conda create -n google_env python
conda activate google_env
pip install numpy
pip install tqdm
pip install -U google-generativeai
```

## imageio_env

```bash
conda create -n imageio_env python
conda activate imageio_env
pip install imageio
pip install matplotlib
pip install scipy
```

## nibabel_env

```bash
conda create -n nibabel_env python
conda activate nibabel_env
pip install nibabel
pip install Pillow
pip install tqdm
```

## pillow_env

```bash
conda create -n pillow_env python
conda activate pillow_env
pip install pillow
```

## sage_env

```bash
conda create -n sage_env python sage
conda activate sage_env
pip install tqdm
pip install Flask
pip install --upgrade --user snappy
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

## tf_gpu_env

- 基本上是跑不起来的，而且 GPU 也不可用，所以后来放弃了 gpu, 但是环境的名字没改

```bash
conda create -n tf_gpu_env python==3.9
conda activate tf_gpu_env
conda install tensorflow==2.18.0
pip install keras==3.5.0
pip install scikit-learn
conda install nltk
python3 -c "import nltk; nltk.download('punkt')"
python3 -c "import nltk; nltk.download('punkt_tab')" # 请确保安装成功，经常会有报错
```

## vtk_env

```bash
conda create -n vtk_env python
conda activate vtk_env
conda install -c conda-forge vtk
pip install opencv-python
pip install pillow
```

## 如何打包一个 python 项目

- 首先，编写 `MANIFEST.IN` 以及 `pyproject.toml` 
- 在 `base` 环境下执行一下命令：

```bash
rm -f ./dist/*
python3 -m build
python3 -m twine upload ./dist/*
```

