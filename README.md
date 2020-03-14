# Youtube_Test
Opens "Indian National Anthem" in youtube
Testing youtube by using Selenium Webdriver - Python

To Setup Firefox-Selenium-Browser in Ubuntu/liniux

sudo apt install python-pip

pip install selenium
wget latest geckodriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-vxxx-x-linux64.tar.gz
tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
chmod +x geckodriver 
sudo cp geckodriver /usr/local/bin/

This text open Firefox browser with www.youtube.com --> Enter "Indian National Anthem" in youtube search box 
--> click on Search button --> Opens first video appears in search page
