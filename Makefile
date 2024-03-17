PYTHON = python

build_routers:
	$(PYTHON) tools/build_routers.py

update_packages:
	$(PYTHON) tools/update_packages.py