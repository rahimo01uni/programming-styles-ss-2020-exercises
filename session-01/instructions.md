Programming Styles -- SoSe20
---

# Setup and Installation
Set up and install the environments necessary for the exercises and the assignments in this course. We will use three different programming languages to exercise the different styles: Python (3.7) for the exercises; Java (JDK 11) and JavaScript (NodeJS v10.20) for the assignments. 

One of the main distinguishing factors between Java and JavaScript is their fundamentally different **type system**: one has *a strong static type system*, the other has *a weak dynamic type system*.

### Install Python 3.7

#### Install Python3 (for Mac)
Those instructions assume that either you have or are willing to install XCode and Home Brew (see [https://programwithus.com/learn-to-code/install-python3-mac/](https://programwithus.com/learn-to-code/install-python3-mac/)). If you prefer to install python3 manually, check: [https://www.saintlad.com/install-python-3-on-mac/](https://www.saintlad.com/install-python-3-on-mac/)

##### 1. Install Xcode
Xcode is Apple's Integrated Development Environment (IDE). You might already have Xcode on your Mac. If not, you can get Xcode from the Apple store.

##### 2. Install Brew
Homebrew installs the stuff you need. Homebrew is a package manager for Mac OS

1. Launch Terminal
2. Install HomeBrew:
```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

##### 3. Install Python3 with Brew
1. Launch Terminal
2. Run:
```brew install python3```

Check the output of this command: 
```python3 --version```

##### 4. Optionally Install PyEnv

If you need to install multiple versions of python, I suggest you to use PyEnv. You can read more about PyEnv at [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

Also PyEnv can be installed using Brew:
```brew install pyenv```

#### Install Python3.7 (for Window)
The following instructions were taken from:
[https://realpython.com/installing-python/#step-1-download-the-python-3-installer](https://realpython.com/installing-python/#step-1-download-the-python-3-installer)

##### 1. Download the Python 3 installer
Go to the download page for Windows at python.org and choose either the 32-bit or 64-bit installer. If your system has a 32-bit processor, then you should choose the 32-bit installer, otherwise go with the 64-bit system.

##### 2. Run the Installer
Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file and check the box that says **Add Python 3.x to PATH** to ensure that the interpreter will be placed in your execution path.

#### Install Python3.7 (for Linux)
> Those instructions are missing... maybe you can add them?

### Install Java

##### 1.Install JDK
If you do not already have a Java JDK on your system, please install it from [Oracle's Java site](https://docs.oracle.com/en/java/javase/11/install/installation-jdk-microsoft-windows-platforms.html#GUID-A7E27B90-A28D-4237-9383-A58B416071CA). 

We will use **Java 11** in this course.
Note you must install the JDK (The Java Development Kit), which includes a JVM and the tools a developer needs (e.g., javac, the Java compiler).

If you do not like to use Oracle's JDK you might want to use other implementations (e.g., OpenJDK)

Check that you have the right version using:
```java -version```

##### 2. Optionally Install jEnv
jEnv is a little utility similar to PyEnv. You can read more about jEnv [here](https://www.jenv.be/). I suggest you to install jEnv to easily manage multiple Java installations.

jEnv can be also installed using Brew:
```brew install jenv```

##### 3. Optionally Install SDKMAN!
[SDKMAN!](https://sdkman.io/) is another alternative for managing multiple JDK installations, similar to jEnv. It gives you a wide variety of choices to choose your JDK's vendor (Oracle, Amazon, Azul, ...). Moreover, you can install other JVM related tools such as Maven, Gradle, Scala, Groovy, ... through it. SDKMAN! installs smoothly on Mac OSX, Linux, WLS, Cygwin, Solaris, FreeBSD, and you can also easily install it on your Windows machine through [Git for Windows BASH](https://git-scm.com/download/win).

### Install NodeJs 

#### Install NodeJs (Mac Os)
We use Node.js v10.20.1 LTS as the JavaScript environment in this course. 

You're free to install it in whatever way you want, but I suggest to use `nvm` (Node Version Manager) to install and manage multiple different versions of node on your machine. 

You can install `nvm` using Homebrew:
```brew install nvm```

Once you have nvm, you can run: 
```nvm install 10.20``` to install the version, and ```nvm use 10.20``` to start using that version.

Check which version of node you are using:
```node --version```

You can check which version of the V8 JavaScript virtual machine your node use using:
```node -p process.versions.v8```

#### Install NodeJs (Windows)
> Those instructions are missing... maybe you can add them?

#### Install NodeJs (Linux)
> Those instructions are missing... maybe you can add them?

### Install an IDE
You are free to use any IDE for programming. Common choices are:

- Eclipse or IntelliJ for developing in Java (I will use Eclipse)
- PyCharm for developing in Python.
- Visual Studio Code (not VisualStudio!) as JavaScript editor.
