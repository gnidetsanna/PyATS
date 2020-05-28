# Introduction

Training project for mastering PyATS testing ecosystem on the topology created in the graphical network simulator GNS3

## Requirements

* Vagrant
* Oracle VM VirtualBox

## Project deploy / usage
```bash
vagrant up
vagrant ssh -- -R 5002:localhost:5002 -R 5003:localhost:5003 -R 5004:localhost:5004
cd /vagrant/
python3 connectivity_test.py
```


## Topology
                        localhost:5002                             localhost:5003
                       +-------------+                            +-------------+
                       |   Router    | s0/1                  s1/0 |    Router   |
                       |             | —— —— —— —— —— —— —— —— —— |             |
                       | Cisco 7200  |                            |  Cisco 7200 |
                       +-------------+                            +-------------+
                                 s1/1 \                          / s1/2
                                       \      200.1.1.0/24      /
                                        \                      /
                                         \                    /
                                          \                  /                 
                                           \+--------------+/ 
                                        s1/1|    Router    |s1/2
                                            |              |
                                            |  Cisco 7200  |
                                            +--------------+
                                             localhost:5004
