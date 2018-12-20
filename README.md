# Real-SPDT-Contact-Networks
These data sets contain  SPDT contact networks extracted from the GPS location updates from users of a location based online social networks. The contains links among 364K users where links are defined as tuple: [Host-ID, Neighbour-ID, Host-arrival-time, Host-departure-time, Neb-arrival-time, Neb-departure-time]. These tuples are created when two users have visited a location within a time frame. The networks are constructed for 32 days. There are two data sets: sparse-SPDT-network (SDT) and dense-SPDT-network (DDT). The sparse-SPDT-network(SDT) is constructed for co-location interactions from GPS locations. The links extraction procedures are described in the following papers. As users are not present every day in SDT contact network, a DDT contact network are reconsturcted from the SDT network repeating the available links to the missing links.

https://arxiv.org/pdf/1806.03386.pdf
http://www.mlgworkshop.org/2018/papers/MLG2018_paper_19.pdf
