from setuptools import setup, find_namespace_packages

setup(name='blur_detector',
      packages=find_namespace_packages(include=["blur_detector", "blur_detector.*"]),
      version='0.1',
      description='none',
      url='127.0.0.1',
      author_email='Utkarsh Deshmukh <d_utkarsh@yahoo.co.in>',
      license='BSD-2-Clause license',
      install_requires=[
            "numpy",
            "scikit-image",
            "tqdm",
            "opencv-python"
      ],
      zip_safe=False)
