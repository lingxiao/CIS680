
## configure virtualenv and install tensorflow ##

	1. run the following commands in sequence:
	
		pip uninstall virtualenv
		sudo conda update --all
		conda install virtualenv
		cd ~/
		mkdir tensorflow-master
		cd tensorflow-master
		virtualenv --system-site-packages .
		easy_install -U pip 
		pip install --upgrade tensorflow

	2. enter virtualenv

		source ~/tensorflow-master/bin/activate

	2. validate tensorflow is installed, on command-line: 

		python
		import tensorflow as tf
		tf.__version__ 

	it should say 1.7.0


## set up environmental path ## 

	export PYTHONPATH=$HOME/dirWithScripts/:$PYTHONPATH
