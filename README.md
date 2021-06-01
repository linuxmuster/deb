<p align="center">
   <img src="https://raw.githubusercontent.com/linuxmuster/archive/master/.github/media/lmn-logo.svg" alt="LMN logo" width="70%" />
</p>

<p align="center">
  <a href="https://github.com/linuxmuster/archive/actions/workflows/build-and-deploy.yml"><img src="https://github.com/linuxmuster/archive/actions/workflows/build-and-deploy.yml/badge.svg" /></a>
  <a href="https://ask.linuxmuster.net"><img src="https://img.shields.io/discourse/users?logo=discourse&logoColor=white&server=https%3A%2F%2Fask.linuxmuster.net" alt="Community Forum"/></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0" ><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" /></a>
</p>

<p align="center">
This is the Linuxmuter.net archive. It is the place where you can get the latest versions of all Linuxmuster.net software.
</p>

# Setup
To use the repository, please follow these steps:
#### 1. Import key:
```bash
wget -qO - "linuxmuster.github.io/archive/pub.gpg" | sudo apt-key add -
```
#### 2. Add repo:
Choose ONE of these depending on your system:
###### Ubuntu 20.04 Focal:
```bash
echo "deb https://linuxmuster.github.io/archive focal main" > /etc/apt/sources.list.d/lmn7.list
```

###### Ubuntu 18.04 Bionic:
```bash
echo "deb https://linuxmuster.github.io/archive bionic main" > /etc/apt/sources.list.d/lmn7.list
```
#### 3. Apt update
```bash
apt update
```
