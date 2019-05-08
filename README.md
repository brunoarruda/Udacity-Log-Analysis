# Udacity Nanodegree Full Stack Developer

## Project 3 - Log Analysis

In this project, we must manipulate a PostGree database and produce a log file as requested. The database was extracted from real world data application and is [available for downloading](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

The questions proposed to build the queries are:

- 'Quais são os três artigos mais populares de todos os tempos?'
- 'Quem são os autores de artigos mais populares de todos os tempos?'
- 'Em quais dias mais de 1% das requisições resultaram em erros?'

## Setup

The project was done using a VM with Ubuntu 16.04 on Windows 0. Up to this date, the latest releases of Vagrant and Oracle VM didn't work together to deploy the VM related to this project. Through trial and error I came to the set of lastest working releases, which are specified below:

1. Install [Vagrant v.2.0.0](https://releases.hashicorp.com/vagrant/2.0.0/)
2. Install [Oracle VM v.5.1.38](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3. Download vagrantfile from this repo or clone from [Udacity repo](https://github.com/udacity/fullstack-nanodegree-vm)
4. go to Vagrantfile folder on prompt and run ```vagrant up``` to set the Virtual Machine and dependencies of the project.
5. save the file ```newsdata.sql``` inside the vagrant folder so that it can be seen by the VM.

## Running

1. Go to the folder where Vagrantfile is
2. Activate and connect to the the VM by running ```vagrant up``` and ```vagrant ssh```
3. Run ```psql -d news -f newsdata.sql``` to load the data on PostGreSQL
4. Run ```python2 news_log.py```

## Views

The first 2 queries depends upon 3 views, all of them in [views.sql](views.sql).