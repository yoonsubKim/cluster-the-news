from setuptools import setup, find_packages

setup(
    name='cluster_the_article',
    version='0.0.1',
    description='',
    url='https://github.com/yoonsubKim/cluster-the-article.git',
    author='rupert kim',
    author_email='my@rupert.in',
    license='MIT',
    install_requires=[
        'numpy',
        'konlpy'
    ],
    packages=find_packages('lib'),
)