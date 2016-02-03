# Info on Top Level Domain

### Installation Requirements

```bash
sudo apt-get install whois
```

### Usage

```bash
whois https://www.facebook.com/ # erroneous
whois facebook.com # spits out correct info
```


***


# Extract IP Address of URL

```bash
host facebook.com
```

Example Output:

```bash
facebook.com has address 66.220.158.68
facebook.com has IPv6 address 2a03:2880:2130:7f20:face:b00c:0:25de
facebook.com mail is handled by 10 msgin.vvv.facebook.com.
```

### GeoIPs with Multiple IP Addresses

```bash
host google.com
```

Example Output:

```bash
google.com has address 74.125.200.113
google.com has address 74.125.200.101
google.com has address 74.125.200.139
google.com has address 74.125.200.102
google.com has address 74.125.200.138
google.com has address 74.125.200.100
google.com has IPv6 address 2404:6800:4003:c01::64
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
```


***


# Nmap Scanner

### Installation Requirements

```bash
sudo apt-get install nmap
```

### Usage

```bash
nmap -F 54.186.250.79
```

Example Output:

```bash

Starting Nmap 6.47 ( http://nmap.org ) at 2016-02-03 16:13 WIB
Nmap scan report for 79.250.186.54.in-addr.arpa (54.186.250.79)
Host is up (0.057s latency).
Not shown: 97 filtered ports
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 9.25 seconds


```