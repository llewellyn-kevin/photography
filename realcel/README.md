# Real Cel Shading
This contains utilities for performing a cel shading type effect
on real photographs.

## Running
To install dependencies you need to have `pipenv` module installed. Then run:

```$ python -m pipenv install```

to install dependencies.

To run tests:

```$ python -m pipenv run pytest```

To run a script:

```$ python -m pipenv run console/example.py```
Or to deal with path and import issues, run as a module:
```$ python -m console.example```

To enter a virtual shell and run everything to pipenv by default:

```$ python -m pipenv shell```

Then tests:

```$ pytest```

And scripts:

```$ python console/example.py```
Or to deal with path and import issues, run as a module:
```$ python -m console.example```

When testing or using the package, you will need to provide and generate images. For working locally, if you create an `images` directory at this level, it is already in the `.gitignore`. That way none of the images you use for testing will be included in the repo. For example, to use `compress_palette.py` for creating a minimized palette file:

```$ python -m realcel.compress_palette ./images/in.png .images/out.png```
