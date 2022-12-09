# kedro-project

## Overview

This is your new Kedro project, which was generated using `Kedro 0.18.4`.

It servers as an example to convert a Jupyter Notebook to a Kedro project.

It is based on the [Kaggle starter competition “Spaceship Titanic”](https://www.kaggle.com/competitions/spaceship-titanic) and provides a basic machine learning pipeline to produce a model.

## How to install dependencies

All dependencies are declared in `src/requirements.txt` for `pip` installation.

Be sure to create a virtual environment then to install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

It will save the model as pickle file in the folder `data/06_models/` and print how the model performs to the output.

## How to test your Kedro project

No testing so far.

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
