from setuptools import setup, find_packages

setup(
    name='Global Economic Growth Forecasting',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'seaborn',
        'flask',
        'wbdata'
        'joblib'  
    ],
    python_requires='>=3.7',
    description='A project for forecasting global economic growth and risk using machine learning techniques.'
)
