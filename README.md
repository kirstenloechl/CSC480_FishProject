# CSC480_FishProject

### Installation & Activation for [Mac](https://github.com/kirstenloechl/CSC480_FishProject#mac) and [Windows](https://github.com/kirstenloechl/CSC480_FishProject#windows)

There is a virtual environment already setup with tensorflow and keras installed on it. So you must also have **python3, pip3, and virtualenv** installed to run it.

#### Mac
###### To Install the Python development environment on *Mac*
1. Check if your Python environment is already configured:
    ```sh
    $ python3 --version
    $ pip3 --version
    $ virtualenv --version
    ```
    If these packages are already installed, skip to the create step.
    Otherwise, install [Python](https://www.python.org/), the [pip package manager](https://pip.pypa.io/en/stable/installing/), and [Virtualenv](https://virtualenv.pypa.io/en/stable/):

2. Install using the [Homebrew](https://brew.sh/) package manager:
    ```sh
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    $ export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
    $ brew update
    $ brew install python  # Python 3
    $ sudo pip3 install -U virtualenv  # system-wide install
    ```
###### To create the virtual environment on *Mac*
3. Create a new virtual environment by choosing a Python interpreter and making a ./venv directory to hold it:
    ```sh
    $ virtualenv --system-site-packages -p python3 ./venv
    ```
###### To activate and setup the virtual environment on *Mac*
4. Activate the virtual environment using a shell-specific command:
    ```sh
    $ source ./venv/bin/activate  # sh, bash, ksh, or zsh
    ```
    When virtualenv is active, your shell prompt is prefixed with (venv).
5. Setup the virtual environment:
    ```sh
    (venv) $ pip install --upgrade tensorflow
    (venv) $ pip install keras
    (venv) $ pip list  # show packages installed within the virtual environment
    # this output should match requirements.txt
    ```
6. And to exit virtualenv later:
    ```sh
    (venv) $ deactivate  # don't exit until you're done using TensorFlow and Keras
    ```
#### Windows
###### To Install the Python development environment on *Windows*
1. Check if your Python environment is already configured:
    ```sh
    $ python3 --version
    $ pip3 --version
    $ virtualenv --version
    ```
    If these packages are already installed, skip to the create step.
    Otherwise, install [Python](https://www.python.org/), the [pip package manager](https://pip.pypa.io/en/stable/installing/), and [Virtualenv](https://virtualenv.pypa.io/en/stable/):

2. Install the Microsoft Visual C++ 2015 Redistributable Update 3. This comes with Visual Studio 2015 but can be installed separately:
    1. Go to the [Visual Studio downloads](https://visualstudio.microsoft.com/vs/older-downloads/),
    2. Select Redistributables and Build Tools,
    3. Download and install the Microsoft Visual C++ 2015 Redistributable Update 3.
    Install the 64-bit Python 3 release for Windows (select pip as an optional feature).
    ```sh
    C:\> pip3 install -U pip virtualenv
    ```
###### To create the virtual environment on *Windows*
3. Create a new virtual environment by choosing a Python interpreter and making a ./venv directory to hold it:
    ```sh
    C:\> virtualenv --system-site-packages -p python3 ./venv
    ```
###### To activate and setup the virtual environment on *Windows*
4. Activate the virtual environment using a shell-specific command:
    ```sh
    (venv) C:\> .\venv\Scripts\activate
    ```
    When virtualenv is active, your shell prompt is prefixed with (venv).
5. Setup the virtual environment:
    ```sh
    (venv) $ pip install --upgrade tensorflow
    (venv) $ pip install keras
    (venv) $ pip list  # show packages installed within the virtual environment
    # this output should match requirements.txt
    ```
6. And to exit virtualenv later:
    ```sh
    (venv) $ deactivate  # don't exit until you're done using TensorFlow and Keras
    ```
### Image Recognition Example 
```sh
(venv) $ cd models/tutorials/image/imagenet
(venv) $ python classify_image.py
```
If the model runs correctly, the script will produce the following output:
```
giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca (score = 0.88493)
indri, indris, Indri indri, Indri brevicaudatus (score = 0.00878)
lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens (score = 0.00317)
custard apple (score = 0.00149)
earthstar (score = 0.00127)
```
If you wish to supply other JPEG images, you may do so by editing the --image_file argument.
```
If you download the model data to a different directory, you will need to point --model_dir to the directory used.
```### Image Recognition Example 
```sh
(venv) $ cd models/tutorials/image/imagenet
(venv) $ python classify_image.py
```
If the model runs correctly, the script will produce the following output:
```
giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca (score = 0.88493)
indri, indris, Indri indri, Indri brevicaudatus (score = 0.00878)
lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens (score = 0.00317)
custard apple (score = 0.00149)
earthstar (score = 0.00127)
```
If you wish to supply other JPEG images, you may do so by editing the --image_file argument.
```
If you download the model data to a different directory, you will need to point --model_dir to the directory used.
```

### Todos
- Import dataset
- Setup CNN
- Train model 
