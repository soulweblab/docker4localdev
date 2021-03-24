# Docker4LocalDev

_by [Soulweb](https://soulweb.it)_

Docker base URL: `docker.localdev`.

## Run with Docker Compose

`docker-compose -f traefik.yml up -d`

## Available domains

* Traefik Dashboard: https://docker.localdev
* Portainer: https://portainer.docker.localdev
* Whoami: https://whoami.docker.localdev

## Locally-trusted certificate

You need to generate your own locally-trusted certificates.

Install [mkcert](https://github.com/FiloSottile/mkcert) on your system.

Once installed, run `mkcert-install`.

Than you are ready to generate your self-signed certificates:

`mkcert -key-file ./certs/key.pem -cert-file ./certs/cert.pem localdev 'docker.localdev' '*.docker.localdev'`

Move the generated certificates (`cert.pem`, `key.pem`) to the folder `certs/` on the root of your `traefix`.
