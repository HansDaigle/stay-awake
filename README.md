# stay-awake

Simple python script to a console script to keep your computer from going to sleep.

### Install

##### Install the wheels (optional)
```
pip install wheel
cd stay-awake/wheels
python -m pip install <wheel> --user  # they have to be install in the right order
```

##### Install the package
```
cd stay-awake
pip install .
```

### How-to use

```bash
stay-awake <args>

stay-awake --help
```

Run the script as a backgroup process:
```
stay-awake <args> &

-> [1] 24474    # pid is will be returned

kill <pid id>   # to stop it
```
