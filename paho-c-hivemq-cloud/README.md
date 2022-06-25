# Preq requisites:
In directory of your choice do the following:
## 1. Compile and install paho mqtt c library
```shell
git clone https://github.com/eclipse/paho.mqtt.c.git
cd pahoo.mqtt.c.git
make
sudo make install
cd ..
```
## 2. OpenSSH (Verify if this step is required)
```shell
git clone https://github.com/openssl/openssl.git
cd openssl
./Configure
make
make test
cd ..
```
# Update CMake File
Update the path to `paho.mqtt.c` in your CMake file to ensure that it will
find the right include files.
