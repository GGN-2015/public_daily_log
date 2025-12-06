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
pip install pygithub     # 用于获取 repo 列表
pip install pynput       # 用于使用键盘控制鼠标点击
```

## cupy_env

```bash
conda create -n cupy_env python
conda activate cupy_env
conda install -c conda-forge cupy
pip install pillow
pip install tqdm
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

## dicom_bone_env

```bash
conda create -n dicom_bone_env python
conda activate dicom_bone_env
pip install dicom-bone
```

## itk_env

```bash
conda create -n itk_env python
conda activate itk_env
pip install pydicom SimpleITK scikit-image trimesh 
pip install matplotlib tqdm
```

## flask_env

```bash
conda create -n flask_env python
conda activate flask_env
pip install flask
```

## glut_env

```bash
conda create -n glut_env
conda activate glut_env
pip install PyOpenGL PyOpenGL_accelerate
pip install numpy
conda install -c anaconda pyopengl
conda install -c conda-forge glfw
pip install glfw
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

## librosa_env

```bash
conda create -n librosa_env python==3.11
conda activate librosa_env
pip install librosa
pip install sounddevice soundfile
```

## nibabel_env

```bash
conda create -n nibabel_env python
conda activate nibabel_env
pip install vtk
pip install nibabel
pip install Pillow
pip install tqdm
pip install scipy
pip install numpy-stl
pip install SimpleITK
pip install pyvista
pip install pymeshlab
pip install trimesh
pip install scikit-learn
```

## open3d_env

```bash
conda create -n open3d_env python
conda activate open3d_env
conda install -c open3d-admin open3d
pip install tqdm
```

## openai_env

```bash
conda create -n openai_env python
conda activate openai_env
pip install openai
pip install flask
pip install eel
pip install requests
pip install pillow
pip install requests
pip install flask-socketio
pip install psutil
pip install pyperclip
pip install flask-cors
```

## opencv_env

```bash
conda create -n opencv_env python
conda activate opencv_env
pip install opencv-python
pip install matplotlib
```

## pillow_env

```bash
conda create -n pillow_env python
conda activate pillow_env
pip install pillow
```

## pyautogui_env

```bash
conda create -n pyautogui_env python
conda activate pyautogui_env
pip install pyautogui
pip install pyperclip
pip install Pillow
pip install opencv-python
pip install requests
pip install openai
sudo oma install gnome-screenshot # on AOSC OS
```

## librosa_env

```bash
conda create -n librosa_env python=3.12
conda activate librosa_env
pip install numpy 
pip install scipy 
pip install soundfile 
pip install librosa
pip install matplotlib
```

## pygame_env

```bash
conda create -n pygame_env python=3.13
conda activate pygame_env
pip install pygame
pip install numpy
```

## pytorch_cpu_env

```bash
conda create -n pytorch_cpu_env python
conda activate pytorch_cpu_env
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install matplotlib
pip install tqdm
pip install scikit-learn
```

## pytorch_gpu_env

```bash
conda create -n pytorch_gpu_env python=3.13.3
conda activate pytorch_gpu_env
conda install cudatoolkit=11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install matplotlib
pip install tqdm
pip install scipy
pip install scikit-learn
```

## pyvista_env

```bash
conda create -n pyvista_env python
conda activate pyvista_env
conda install -c conda-forge pyvista
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
pip install tqdm
pip install scikit-learn
pip install scikit-image
pip install opencv-python
pip install PyWavelets
pip install flask
pip install SimpleITK
pip install trimesh
pip install vedo
pip install vtk
```

## sklearn_env

```bash
conda create -n sklearn_env python
conda activate sklearn_env
conda install scikit-learn
pip install tqdm
pip install matplotlib
```

## shapez_env

```bash
conda create -n shapez_env
conda activate shapez_env
conda config --add channels conda-forge
conda install nodejs=16.18.0
```

## sympy_env

```bash
conda create -n sympy_env python
conda activate sympy_env
pip install sympy
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

## vlc_env

```bash
conda create -n vlc_env python
conda activate vlc_env
pip install python-vlc
```

## vtk_env

```bash
conda create -n vtk_env python
conda activate vtk_env
conda install -c conda-forge vtk
pip install opencv-python
conda install -c open3d-admin open3d
pip install pillow
pip install tqdm
```

## trimesh_env

```bash
conda create -n trimesh_env python
conda activate trimesh_env
pip install trimesh numpy
```

## yolov8_env

```bash
conda create -n yolov8_env python=3.9 -y
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install ultralytics opencv-python-headless pillow matplotlib
conda install -c conda-forge rasterio
```

## 如何打包一个 python 项目

- 首先，编写 `MANIFEST.IN` 以及 `pyproject.toml` 
- 在 `base` 环境下执行一下命令：

```bash
rm -f ./dist/*
python3 -m build
python3 -m twine upload ./dist/*
```

