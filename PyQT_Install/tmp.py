pip install PyQt6==6.4.2 PyQt6-Qt6==6.4.3 PyQt6-sip==13.5.0

pip install pyqt6-plugins==6.4.2.2.3 qt6-tools==6.4.3.1.3 qt6-applications==6.4.3.2.3



pyqt6_plugins-6.4.2.2.3:
wget https://files.pythonhosted.org/packages/60/13/25ea8ef9bb9a2180e25091ef823ae677d422b36b1413c153e53007cf7b0e/pyqt6_plugins-6.4.2.2.3-cp311-cp311-manylinux2014_x86_64.whl


pyqt6_tools-6.4.2.3.3
wget https://files.pythonhosted.org/packages/82/bc/dcea094a26697ba76ae73dec030dd4070836b1e7e810d304d4917518423b/pyqt6_tools-6.4.2.3.3-py3-none-any.whl



unzip pyqt6_plugins-6.4.2.2.3-cp311-cp311-manylinux2014_x86_64.whl -d pyqt6_plugins
# Edit the METADATA file to remove strict version constraints
zip -r pyqt6_plugins-custom.whl pyqt6_plugins
pip install pyqt6_plugins-custom.whl




wget https://files.pythonhosted.org/packages/55/cc/cd1cd49f36d2f7592fdf0acbc3e24f937f7d8db5e4f89d8fa0ab5952aef0/pyqt6_tools-6.4.2.3.3-py3-none-any.whl
wget https://files.pythonhosted.org/packages/4f/8f/58d4059279f1e9b0261036a4c4176ab09b06dbbfa7fae06270bb7b220ef6/pyqt6_plugins-6.4.2.2.3-cp37-cp37m-manylinux2014_x86_64.whl


