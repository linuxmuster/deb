<p align="center">
   <img src="https://raw.githubusercontent.com/linuxmuster/deb/master/.github/media/lmn-logo.svg" alt="LMN logo" width="70%" />
</p>

<p align="center">
  <a href="https://github.com/linuxmuster/deb/actions/workflows/build-and-deploy.yml"><img src="https://github.com/linuxmuster/deb/actions/workflows/build-and-deploy.yml/badge.svg" /></a>
  <a href="https://ask.linuxmuster.net"><img src="https://img.shields.io/discourse/users?logo=discourse&logoColor=white&server=https%3A%2F%2Fask.linuxmuster.net" alt="Community Forum"/></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0" ><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" /></a>
</p>

<p align="center">
This is the Linuxmuter.net archive. It is the place where you can get the latest versions of all Linuxmuster.net software.
</p>

# Packages
This repo currently contains the following packages:
- [leoclient2](https://github.com/linuxmuster/leoclient2) (lmn71-testing)
- [base7](https://github.com/linuxmuster/linuxmuster-base7) (lmn71,lmn72,lmn73)
- [linbo-gui7](https://github.com/linuxmuster/linuxmuster-linbo-gui7) (lmn71,lmn72,lmn73)
- [linbo7](https://github.com/linuxmuster/linuxmuster-linbo7) (lmn71, lmn71-testing,lmn72,lmn73)
- [linuxclient7](https://github.com/linuxmuster/linuxmuster-linuxclient7) (lmn71,lmn72,lmn73)
- [prepare](https://github.com/linuxmuster/linuxmuster-prepare) (lmn71,lmn72,lmn73)
- [webui7](https://github.com/linuxmuster/linuxmuster-webui7) (lmn71, lmn72,lmn73)
- [sophomorix-samba](https://github.com/linuxmuster/sophomorix-samba) (lmn72,lmn73)
- [tools](https://github.com/linuxmuster/linuxmuster-tools) (lmn72,lmn73)
- [cli](https://github.com/linuxmuster/linuxmuster-cli) (lmn72,lmn73)
- [api](https://github.com/linuxmuster/linuxmuster-api) (lmn72,lmn73)
 
# Setup

To use the repository, please follow these steps:

## 1. Import key:

```bash
sudo wget -qO- "https://deb.linuxmuster.net/pub.gpg" | gpg --dearmour -o /usr/share/keyrings/linuxmuster.net.gpg
```

## 2. Add repo:

### Linuxmuster 7.3
```bash
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/linuxmuster.net.gpg] https://deb.linuxmuster.net/ lmn73 main" > /etc/apt/sources.list.d/lmn73.list'
```

## 3. Apt update

```bash
sudo apt update
```

# Linuxmuster.net packages interaction

A quick view over the interaction between all packages when installed on the server:

<p align="center">
   <img src="https://raw.githubusercontent.com/linuxmuster/deb/master/.github/media/Linuxmuster.drawio.png" alt="LMN Structure" width="100%" />
</p>

# Index of /
Files in this directory:
- 📁 [dists/](dists)
- 📁 [pool/](pool)
- 🗒 [pub.gpg](pub.gpg)
