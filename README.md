# Persistence

Spring 2020 MATH 197 Persistence Group at UC, Riverside.

## GUDHI Library Installation and Setup

### With Anaconda (Easiest)

#### Step 1. Download and Install Anaconda

Anaconda can be downloaded [here](https://www.anaconda.com/distribution/).
Get the Python 3 version. A graphical installer is available for Mac and Windows,
and in my opinion is the easiest way to install anaconda.

(Optional): Create an [Environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)
in Anaconda for this project.

1. Open Anaconda-Navigator from your applications.
2. Click `Environments` in the left pane.
3. Click `Create` in the bottom left (next to the social media buttons).
4. Name it whatever you want (examples: TDA or Persistence) and make sure the python checkbox is selected.

or if you want to do it from the command-line:

```bash
conda create --name UR_ENV_NAME python
```

where `UR_ENV_NAME` is whatever you choose to name your environment.

Press enter when you see

``` bash
Proceed ([y]/n)?
```

#### Step 2. Install GUDHI

Open up a terminal emulator (such as Terminal.app on Mac or PowerShell(?) on Windows)
and enter the following:

``` bash
conda install -n UR_ENV_NAME -c conda-forge gudhi
```

where `UR_ENV_NAME` is whatever you named your environment. If you didn't set
up an environment, then exclude the `-n UR_ENV_NAME` in the above command.

Press enter when you see

``` bash
Proceed ([y]/n)?
```

Once that finishes you have successfully installed GUDHI.

#### Step 3. Add additional packages

You will need `matplotlib` for plotting and `scikit-learn` for persistence
representations. Then can be installed by entering the following in your
command-line:

```bash
conda install -n UR_ENV_NAME matplotlib scikit-learn
```

and pressing enter when you see the prompt `Proceed ([y]n)?`.

#### Step 4. Install your jupyter notebook interface

I was using JupyterLab in the Zoom meeting which can be installed directly
from Anaconda-Navigator. Click on **Home** in the left pane and in the
**Applications on** drop down menu located to the right of **Home** select your
environment. When that finishes loading, click install in the
**JupyterLab** tile and then click launch. It will load your environment and
everything.

If you prefer IDEs, **Jet Brains** offers the Community Edition of
[PyCharm for Anaconda](https://www.jetbrains.com/pycharm/promo/anaconda/)
for free.

### Without Anaconda

#### Step 1. Install Python 3.7 or greater if you haven't already

Install python 3.7.x (since the rest will be using 3.7 in Anaconda).
I will be using [homebrew](https://brew.sh)
on my Mac which currently installs python 3.7.7.

```bash
$ brew install python
```

#### Step 2. Install GUDHI dependencies

The library uses c++14 and requires
- [Boost](https://www.boost.org/) ≥ 1.56.0,
- [CMake](https://cmake.org/) ≥ 3.1,

to generate makefiles;
- Eigen3,
- CGAL >= 4.11.0,
- Doxygen;

and cython, numpy, scipy, pytest, sphinx, matplotlib, sklearn, and pot to
compile the GUDHI Python module.

I will be using [GCC](https://gcc.gnu.org/) in this setup.

**Install compilation dependencies:**

```bash
$ brew install gcc boost cmake eigen cgal doxygen
```

**Install Python dependencies**:

```bash
$ python3 -m pip install cython numpy scipy
$ python3 -m pip install pytest matplotlib sphinx sklearn pot
```

#### Step 3. Install GUDHI

**Get GUDHI source:**

I will be using **wget** and **tar** do download and extract the source, but
you are free to use whatever you feel most comfortable with.

```bash
$ wget -O- https://github.com/GUDHI/gudhi-devel/releases/download/tags%2Fgudhi-release-3.1.1/gudhi.3.1.1.tar.gz | tar xvz
```

**Compile Python module:**

```bash
$ cd gudhi/gudhi.3.1.1/
$ mkdir build
$ cd build/
$ cmake -DPYTHON_EXECUTABLE=/usr/local/bin/python3 -DPython_ADDITIONAL_VERSIONS=3 ..
$ cd python
$ python3 setup.py build_ext -j 4 --inplace
```

Now you can either add this to your `PYTHONPATH` in your `.bash_profile`,
`.zshrc`, etc:

```bash
export PYTHONPATH='$PYTHONPATH:/path-to-gudhi/build/python'
```

or install it to your python packages folder

```bash
$ python3 setup.py install
```

#### Step 4. Install Jupyter Interface

Install JupyterLab

```bash
$ brew install jupyterlab
```

or

```bash
$ python3 -m pip install ipython jupyter
```
