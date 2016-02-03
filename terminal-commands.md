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


# Install Python `tld` Module

```bash
sudo apt-get install python-pip # installs python package manager
sudo pip install -U tld # installs the `tld` module itself
```

***


# Extract IP Address of URL

```bash
host facebook.com
```

Output:

```bash
```

### GeoIPs with Multiple IP Addresses

```bash
host google.com
```

Output:

```bash
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

Output:

```bash

```