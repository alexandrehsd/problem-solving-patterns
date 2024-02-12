.PHONY: environment
# setup python environment
environment:
	pyenv install -s 3.9.13 ;\
	pyenv virtualenv 3.9.13 interview ;\
	pyenv local interview