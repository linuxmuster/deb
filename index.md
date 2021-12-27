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

# Packages
This repo currently contains the following packages:
- [webui7](https://github.com/linuxmuster/linuxmuster-webui7) (lmn71)
- [prepare](https://github.com/linuxmuster/linuxmuster-prepare) (lmn71)
- [linbo7](https://github.com/linuxmuster/linuxmuster-linbo7) (lmn71)
- [linbo-gui7](https://github.com/linuxmuster/linuxmuster-linbo-gui7) (lmn71)
- [linuxclient7](https://github.com/linuxmuster/linuxmuster-webui7) (lmn71)
- [sophomorix4](https://github.com/linuxmuster/sophomorix4) (lmn71)

# Setup

To use the repository, please follow these steps:

## 1. Import key:

```bash
wget -qO - "https://deb.linuxmuster.net/pub.gpg" | sudo apt-key add -
```

## 2. Add repo:

### Linuxmuster 7.1 testing
```bash
sudo sh -c 'echo "deb https://deb.linuxmuster.net/ lmn71 main" > /etc/apt/sources.list.d/lmn71.list'
```

## 3. Apt update

```bash
sudo apt update
```

# Index of /
Files in this directory:
- 📁 [dists/](dists)
- 📁 [pool/](pool)
- 🗒 [pub.gpg](pub.gpg)
