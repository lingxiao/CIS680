
## configure virtualenv and install tensorflow ##

0. pip uninstall virtualenv
1. sudo conda update --all
2. conda install virtualenv
3. cd ~/
4. mkdir tensorflow-master
5. cd tensorflow-master
6. virtualenv --system-site-packages .
7. easy_install -U pip 
8. pip install --upgrade tensorflow
9. check tensorflow is installed, on command-line: 


	```
		python
		import tensorflow as tf
		tf.__version__ 
	```


	it should say 1.7.0
