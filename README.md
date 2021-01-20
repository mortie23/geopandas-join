##Back ground
To use geopands need to have python3.8 and also install conda for easy installation, pip install seems to repeatedly fail


##Building Python 3.8 on Debian is a relatively straightforward process and will only take a few minutes.
##Start by installing the packages necessary to build Python source:
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
python --version
curl -O https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tar.xz 
tar -xf Python-3.8.0.tar.xz 
cd Python-3.8.0
./configure --enable-optimizations
make
sudo make altinstall
python3.8 --version

##Next need to install miniconda
As per the guide install miniconda
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

Need to download the file : https://docs.conda.io/en/latest/miniconda.html
bash Miniconda3-latest-Linux-x86_64.sh

Need to add conda to path: 
echo $path
export PATH=$PATH:/root/miniconda3/bin/

##Next check to see if conda is working by running the conda command then run conda install geopands
conda
conda install geopandas
