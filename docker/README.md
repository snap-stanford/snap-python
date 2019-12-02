# Snap-Python Docker
Creates a lightweight Docker compute stack for performing network graph analysis using snap-python, numpy, and matplotlib agnostic of the host operating system.

This document stipulates installation requirements for the Docker Community Edition (CE), and walks through Docker installation, building, and running the snap-python Docker image.

## OS Requirements

Basic operating system requirements for running the Docker Engine - Community. See more at: [https://docs.docker.com/install/](https://docs.docker.com/install/).

### Linux

* **CentOS**
  * A maintained version of CentOS 7 is required for Docker Engine - Community
* **Debian**
  * To install Docker Engine - Community, you need the 64-bit version of one of these Debian or Raspbian versions:
      * Buster 10
      * Stretch 9 (stable) / Raspbian Stretch
* **Fedora**
  * To install Docker Engine - Community, you need the 64-bit version of one of these Fedora versions:
      * 28
      * 29 
* **Ubuntu**
  * To install Docker Engine - Community, you need the 64-bit version of one of these Ubuntu versions:
      * Disco 19.04
      * Cosmic 18.10
      * Bionic 18.04 (LTS)
      * Xenial 16.04 (LTS)

### macOS
Your macOS hardware must meet the following requirements to install Docker Desktop. See more at: [https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/).

* Mac hardware must be a 2010 or newer model, with Intel’s hardware support for memory management unit (MMU) virtualization, including Extended Page Tables (EPT) and Unrestricted Mode. You can check to see if your machine has this support by running the following command in a terminal: sysctl kern.hv_support

* macOS must be version 10.13 or newer. We recommend upgrading to the latest version of macOS.

* If you experience any issues after upgrading your macOS to version 10.15, you must install the latest version of Docker Desktop to be compatible with this version of macOS.

* Note: Docker supports Docker Desktop on the most recent versions of macOS. That is, the current release of macOS and the previous two releases. As new major versions of macOS are made generally available, Docker will stop supporting the oldest version and support the newest version of macOS (in addition to the previous two releases).

* At least 4 GB of RAM.

* VirtualBox prior to version 4.3.30 must not be installed as it is not compatible with Docker Desktop.

### Windows
System requirements:

* Windows 10 64-bit: Pro, Enterprise, or Education (Build 15063 or later).
Hyper-V and Containers Windows features must be enabled.

* The following hardware prerequisites are required to successfully run Client Hyper-V on Windows 10:
  * 64 bit processor with [Second Level Address Translation (SLAT)](http://en.wikipedia.org/wiki/Second_Level_Address_Translation)
  * 4GB system RAM
  * BIOS-level hardware virtualization support must be enabled in the BIOS settings. For more information, see [Virtualization](https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization-must-be-enabled)

## Docker Installation

Note that installation steps outlined below for Linux are purposefully only defined for Ubuntu. Installation of Docker for other Linux distributions is left as an exercise to the reader. These instructions outline installation from the Docker repository (the recommended approach), and are a subset of the instructions available at [https://docs.docker.com/install/](https://docs.docker.com/install/).

#### Linux (Ubuntu)

1. Begin by updating all packages:

	```
	$ sudo apt-get update
	```

2. It is recommended to uninstall any old Docker software before proceeding (note that this command accounts for old versions of Docker, which were named "docker", "docker.io", etc.):

	```
	$ sudo apt-get remove docker docker-engine docker.io containerd runc
	```

3. Set up the Docker repository to install from:

	```
	$ sudo apt-get install \
    	apt-transport-https \
    	ca-certificates \
    	curl \
    	gnupg-agent \
    	software-properties-common
	```
4. Add Docker's official GPG key:

	```
	$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	```
	
5. Verify that you have the key with the fingerprint `9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88` by searching for the last 8 characters of the fingerprint:
  
	```
  	$ sudo apt-key fingerprint 0EBFCD88
    
	pub   rsa4096 2017-02-22 [SCEA]
      		9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
	uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
	sub   rsa4096 2017-02-22 [S]
  ```

6. Use the following command to setup the **stable** repository:

	```
	$ sudo add-apt-repository \
   		"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	   $(lsb_release -cs) \
   		stable"
	```

7. Install the latest version of Docker Engine - Community and containerd:

	```
	$ sudo apt-get install docker-ce docker-ce-cli containerd.io
	```

8. Verify that Docker Engine - Community is correctly installed by running the `hello-world` image:

	```
	$ sudo docker run hello-world
	```

#### macOS
To download Docker Desktop for macOS, go to [Docker Hub](https://hub.docker.com/?overlay=onboarding) and sign in with your DockerID. You will require a Docker Hub account. See more at [https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/).

1. Download the Docker Desktop installer for macOS from the link above
2. Double-click the Docker.dmg to open the installer, then drag the Docker icon to the Applications folder
3. Double-click Docker.app in the Applications folder to start Docker
4. Verify the Docker daemon is running by running the `hello-world` image:

	```
	$ docker run hello-world
	```

#### Windows
To download Docker Desktop for Windows, go to [Docker Hub](https://hub.docker.com/?overlay=onboarding) and sign in with your DockerID. You will require a Docker Hub account. See more at [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/).

1. Download the Docker Desktop installer for Windows from the link above
2. Double click the **Docker Desktop Installer.exe** to run the installer
3. Follow the instructions on the installation wizard to accept the license, authorize the installer, and proceed with the install
  * **Note:** When prompted, authorize the Docker Desktop Installer with your system password during the install process. Privileged access is needed to install networking components, links to the Docker apps, and manage the Hyper-V VMs
4. Click **Finish** on the setup complete dialog and launch the Docker Desktop application.
5. Verify the Docker daemon is running by running the `hello-world` image:

	```
	$ docker run hello-world
	```

## Building the snap-python Docker image
Once Docker is installed on your host, we can build the `snap-python` Docker image. The Docker image is a lightweight read-only template used to build containers, which are running "jailed" processes. We can build the `snap-python` image in one of two ways:

1. We can install directly from the hosted official image on Docker Hub (recommended):
  * ```$ docker pull cam2337/snap-python:latest```


2. Alternatively, if you've cloned this repository (see installation instructions in the top-level `README.md`), we can build the Docker image directly from the `Dockerfile` in `<repository-root>/docker/`:
  * ```$ docker build . -t snap-python```

## Running a snap-python Docker container
We can verify that the `snap-python` image is installed by issuing the following command:

```
$ ctew-macbookpro:examples ctew$ docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
cam2337/snap-python   latest              e2229d02c39e        46 minutes ago      1.09GB
```

As we see from the example above, this image was downloaded and built from the official image as hosted on Docker Hub.

Now that the image is built, all we need to do is run a snap-python container:

```
$ docker run -it cam2337/snap-python
Python 3.7.5 (default, Nov 23 2019, 05:59:34) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import snap
>>> snap.Version
'5.0.0'
```

While an interactive Python shell with `snap-python` capabilities is great, we can go one step further and specify a working directory for a python application that relies on snap. This directory can be mounted as [volume](https://docs.docker.com/storage/volumes/) in the snap-python Docker container. The scripts then have full access to the `snap-python` module that was baked into our image:

```
docker run -it --rm -v "<working-directory>":/usr/src/snap -w /usr/src/snap cam2337/snap-python python <working-directory>/<example-python-file>
```

Let's individually cover some of the more interesting components of this command:

* `-it`: This tells Docker that we want to run the container interactively, by keeping STDIN open even if not attached. It additionally allocates a pseudo-TTY
* `--rm`: Instructs Docker to automatically remove the container once it exits. Since our Docker container is functioning as a "compute stack" (instead of, say, a server or backend), this is desirable, as there's no need for a container to be hanging around after we've run our application.
* `-v`: Instructs Docker to mount the following local filesystem directory at `/usr/src/snap`
* `-w`: Instructs Docker that its working directory should be the newly-mounted volume at `/usr/src/snap`
* `cam2337/snap-python`: The image we want to run
* `python`: The command we want to issue once our container is started
* `<working-directory>/<example-python-file>`: The python file from our local filesystem to run in the `snap-python` container


## Frequently Asked Questions (FAQ)

### Q: My Python application has specific package requirements. How can I build my own custom Docker image that installs these additional packages?
You can leverage the image created by the `Dockerfile` in this directory (or hosted on [Docker Hub](https://hub.docker.com/repository/docker/cam2337/snap-python)) and build upon it in [layers](https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#images-and-layers). Say, for instance, you need `pandas` installed for your Python application to work. An example Dockerfile might look like:

```
FROM cam2337/snap-python:latest
RUN pip install pandas
```

You can then build this image locally:

```
$ docker build -t my-custom-snap-python .
```

We can then run the container and verify that importing `pandas` behaves as expected:

```
$ ctew-macbookpro:docker ctew$ docker run -it my-custom-snap-python
Python 3.7.5 (default, Nov 23 2019, 05:59:34) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
>>> 
```

### Q: How can I leverage the snap-python Docker compute stack from the comfort of my favorite editor?
Most popular editors nowadays provide the option to create a custom "build system" for building/running a subset of files. In this way, they become more akin to a traditional integrated development environment (IDE). We can leverage this fact to create a custom build system for our snap-python Docker compute stack.

For example, we can create the following custom build system in SublimeText:

```
{
    "shell_cmd": "docker run --rm -v $file_path:/usr/src/snap -w /usr/src/snap cam2337/snap-python python $file_name",
    "selector": "source.python",
    "file_regex": "^\\s*File \"(...*?)\", line ([0-9]*)"
}
```

Saving this as `docker-snap-python.build` in the SublimeText user build system space, we can now select it from `Tools > Build System > docker-snap-python`. Building an in-focus Python file with this option selected will now execute our snap-python Docker compute stack.