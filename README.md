# try_traitlets_for_ctapipe
Here I try to understand how traitlets works

You can follow my "steps" by checking out each "step_xxx" tag.

# step 1

input:

    git checkout step_1
    python myapp.py -i 3

output:

    app.config:
    {'Foo': {'i': 3}}

Just to see if everything works, if not .. you might need to:

    pip install traitlets

# step 2

Here I moved the "Components" Foo and Bar out of the "Application" source code file, just to make it more look like ctapipe.

I added some `print()` so we can see that `Foo` and `Bar` are still nicely configured.

Have a look at the help again:

    python myapp.py --help-all

To see what configurations Foo and Bar have.

input:

    git checkout step_2
    python myapp.py -i 3 --enabled=False --Foo.name="Prian"

output:

    app.config:
    {'Foo': {'i': 3, 'name': 'Prian'}, 'Bar': {'enabled': False}}

    self.foo.__dict__:
    {'_trait_values': {
        'i': 3,
        'j': 1,
        'name': 'Prian',
        'config': <same_as_above>,
        'parent': None},
        # I deleted some lines
    }

    self.bar.__dict__:
    {'_trait_values': {
        'enabled': False,
        'config': <same_as_above>,
        'parent': None},
        # I deleted some lines
    }

We see both components are nicely configured. They even have both a "copy"
of the entire configuration of the entire Application.
**Observe**: the `parent` was obviously not used, as it is `None`.

# step 3

Now let's try to use a config file `config.py`.

input:

    git checkout step_3
    cat config.py  # if you like
    python myapp.py --config=config.py

output:

    app.config:
    {'MyApp': {'config_file': 'config.py', 'Foo': {'i': 10}, 'Bar': {'enabled': False}}}

**Observe**: Foo and Bar were not correctly configured. Why?

Well, I made a mistake in the config file, I appended the name of the Application `MyApp`. Note  there was no error whatsoever, out application simply used the default values.

I leave it to the reader to try a few other simply errors, like typos ... try to configure values which do not even exist.

No problem .. is that what ctapipe wants?


# step 4

Here I only fixed the error in the config.py

input:

    git checkout step_4
    python myapp.py --config=config.py

output:

    boring

observe that indeed `foo` and `bar` were correctly configured.
