# try_traitlets_for_ctapipe
Here I try to understand how traitlets works

You can follow my "steps" by checking out each "step_xxx" tag.

# step 1

input:

    git checkout step1
    python myapp.py -i 3

output:

    app.config:
    {'Foo': {'i': 3}}

Just to see if everything works, if not .. you might need to:

    pip install traitlets

