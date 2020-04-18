# Persistence

2020 MATH 197 Persistence Group

## GUDHI Library Installation and Setup

---

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

Coming soon