===
PSY
===

Utility to create aws lambda bundles out of python packages.

`psy` is a python utility that allows you to generate (and handle) aws lambda bundles out of classical
setuptools based python packages.

=====
Why ?
=====

If you had to work with AWS Lambda as part of your day to day work you may have noticed that you can easily end up
with spaguetti-long-single-file python scripts: Not easy to keep track, organize distribute or package.

`psy` tries to address this problem by leveraging python packaging capabilities.

And therefore you don't manage lambda scripts anymore as file anymore, rather you work with packages as you use to do.
You can then have more than one lambda function in a single package allowing you to gather code that share
common code.

=====
Usage
=====

1. Write you python package as you would do for any application, organize your code as you feel like to and put your
lambda handler anywhere within your source code.

2. For any lambda function that you want your package to `export`, add an `entrypoint` to your pyton distribution as such
::

  psy.lambda_handler =
      <name_of_your_handler> = <path_to_your_code_dotted_python_notation>

3. Install `psy`
::

  pip install git+https://github.com/Grindizer/psy#egg=psy

4. Generate your lambda zip ready to upload with
::

  python setup.py bdist_lambda

Here you should have a self contain zip file in ./dist/ you can upload the file to aws lambda, any handler that you defined in your package can be referenced as
::

  lambda_handler.<name_of_your_handler>

============
Installation
============

::

    pip install git+https://github.com/Grindizer/psy#egg=psy

Or in a develop mode after downloading a zip or cloning the git repository ::

    git clone https://github.com/Grindizer/psy
    cd psy
    pip install -e .

Or in a develop mode from a git repository ::

    pip install -e git+https://github.com/Grindizer/psy#egg=psy

Once installed your setuptools will be augmented with a new command `bdist_lambda`

==============
Enhancement...
==============

* Add a psy command line that can work with bundle as to run the handler locally for test.
* Generate a iam policy - even if not always totally correct - to work with the lambda.
