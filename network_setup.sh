#!/bin/bash

# Configurações de rede para simular latência ou perda de pacotes, se necessário
docker exec router1 tc qdisc add dev eth0 root netem delay 50ms
docker exec router2 tc qdisc add dev eth0 root netem delay 50ms
docker exec router3 tc qdisc add dev eth0 root netem delay 50ms
docker exec router4 tc qdisc add dev eth0 root netem delay 50ms
