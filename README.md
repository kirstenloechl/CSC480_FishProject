# CSC480_FishProject

### Installation & Activation

There is a virtual environment already setup with tensorflow and keras installed on it. So you must also have **python3, pip3, and virtualenv** installed to run it.

###### To Install the Python development environment on your *Mac*
Check if your Python environment is already configured:

```sh
$ python3 --version
$ pip3 --version
$ virtualenv --version
```

If these packages are already installed, skip to the next step.
Otherwise, install [Python](https://www.python.org/), the [pip package manager](https://pip.pypa.io/en/stable/installing/), and [Virtualenv](https://virtualenv.pypa.io/en/stable/):

Install using the [Homebrew](https://brew.sh/) package manager:
```sh
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
$ brew update
$ brew install python  # Python 3
$ sudo pip3 install -U virtualenv  # system-wide install
```

###### To activate the virtual environment on your *Mac*
Activate the virtual environment using a shell-specific command:

```sh
$ source ./venv/bin/activate  # sh, bash, ksh, or zsh
```
When virtualenv is active, your shell prompt is prefixed with (venv).
```sh
(venv) $ pip list  # show packages installed within the virtual environment
```
And to exit virtualenv later:
```sh
(venv) $ deactivate  # don't exit until you're done using TensorFlow
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
```

### Todos
- Import dataset
- Setup CNN
- Train model 
