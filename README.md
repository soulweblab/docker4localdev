# Docker4LocalDev

Please, follow the full tutorial on [Medium](https://medium.com/soulweb-academy/docker-local-dev-stack-with-traefik-https-dnsmasq-locally-trusted-certificate-for-ubuntu-20-04-5f036c9af83d)!

## Run with Docker Compose

`docker-compose -f traefik.yml up -d`

## Available domains

* Traefik Dashboard: https://docker.localdev
* Portainer: https://portainer.docker.localdev
* Whoami: https://whoami.docker.localdev

## Locally-trusted certificate

You need to generate your own _locally-trusted_ certificate.

Install [Mkcert](https://github.com/FiloSottile/mkcert) on your system.

Once installed, run `mkcert-install`.

Than you are ready to generate your self-signed certificates:

`mkcert -key-file ./certs/key.pem -cert-file ./certs/cert.pem localdev 'docker.localdev' '*.docker.localdev'`

Move the generated certificates (`cert.pem`, `key.pem`) to the folder `certs/` on the root of your `traefix`.
