# tsakorpus
An implementation of the Tsakorpus platform for ELIC

## Setup
A guide for setting up tsakorpus from scratch on the UGA corpus server is available in `tsakorpus_setup.ipynb`. Alternatively, to run and view tsakorpus locally, you can

0. Setup a virtual environment and install all necessary packages
1. Clone this repository
2. Install and run elasticsearch
3. Start the corpus interface with `python tsakorpus.wsgi` within the `search` directory
4. Go to http://127.0.0.1:7342/search

## To-do
- [x] Show tiers for each word in search results when searching sentences
- [ ] Fix tiers to show correct information
- [ ] Fix audio clipping issue with new .eaf files
- [x] Add and show metadata information
