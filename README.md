# Create a virtual environment
conda create -n guidereg python=3.10
conda activate guidereg
conda install -c conda-forge itk-elastix

# Install package
git clone https://github.com/yourname/GuideReg.git
cd Guidereg
pip install -e .