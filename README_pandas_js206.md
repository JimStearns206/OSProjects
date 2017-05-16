# Setting up Pandas Development Environment

## References

[Contributing to pandas](http://pandas.pydata.org/pandas-docs/stable/contributing.html#contributing)

The starting point. Learnings:
* How to use rebase to update my repos from upstream/master
```bash
git fetch upstream
git rebase upstream/master
```

[Pandas Installation](http://pandas.pydata.org/pandas-docs/stable/install.html#dependencies)

Python 2.7, 3.4, 3.5 and 3.6 supported. Will be using 3.6.

Recommends installing Anaconda environment. I think will build pandas in a conda environment.

Name: **py36_pandas**

## Source

## Dependencies

## The Steps

* Source

(Insert here, down to git remote add upstream)

**Recommends a pandas repo named pandas_<I>github_name</I>**

## Anaconda Environment

```bash
conda create -name pandas_dev3 python=3 --file ci/requirements_dev.txt

(or requirements_all.txt)
```

Tried requirements_all.txt but ran into missing package:
```bash

[pandas-jimstearns206]$ conda install -n pandas_dev3 -c pandas --file ci/requirements_all.txt
Fetching package metadata ...........


PackageNotFoundError: Package missing in current osx-64 channels: 
  - pytest-xdist
```

```bash
source activate pandas_dev3
```

## In-Place Install

"The best way to develop pandas is to build the C extensions in-place by running:"
```bash
python setup.py build_ext --inplace
```

This built on Sierra. No errors but lots of warnings

[CExtensionBuildOutput](README_pandas_js206_addenda.md#CExtensionBuildOutput)

