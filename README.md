# shrt
CLI client for creating links with [shirt](https://github.com/ErikBoesen/shirt).

## Setup
Clone and move to directory:

    git clone https://github.com/ErikBoesen/shrt && cd shrt

Set your default host by adding a `$SHRT_HOST` environment variable:

    export SHIRT_HOST=https://myshortener.com

Install python dependencies:

    pip3 install -r requirements.txt

If necessary, mark as executable:

    chmod +x shrt.py

Copy executable to executable location, for example:

    cp shrt.py /usr/local/bin/shrt

If desired, remove residual files:

    cd .. && rm -rf shrt

Link away!

    shrt erikboesen.com

## Options

    url          The URL you want to shorten.

    -h, --help   show help message
    --key KEY    Custom shortlink key to use.
    --host HOST  A custom host to upload links to, if necessary. Defaults to environment variable
		 $SHIRT_HOST.

## Author
This software was developed and is maintained by [Erik Boesen](https://github.com/ErikBoesen).

## Licensing
This software is licensed under the [MIT License](LICENSE).
