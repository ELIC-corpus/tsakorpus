# tsakorpus
An implementation of the Tsakorpus platform for ELIC

## Setup
A guide for setting up tsakorpus from scratch on the UGA corpus server is available in `tsakorpus_setup.ipynb`. Alternatively, to run and view tsakorpus locally, you can

0. Setup a virtual environment and install all necessary packages
1. Clone this repository
   - **NOTE:** the directory containing the actual converted JSON files is listed under .gitignore (a decision made by the Tsakorpus creator). We will need to decide if we want to overwrite this and include all .eaf or converted JSON files. Until then, the corpus will not run "out of the box" unless you create a `corpus/elic` directory and add converted JSON files to it.
2. Install and run elasticsearch
3. Start the corpus interface with `python tsakorpus.wsgi` within the `search` directory
4. Go to http://127.0.0.1:7342/search

## To-do
- [x] Show tiers for each word in search results when searching sentences
- [x] Fix tiers to show correct information
- [ ] Adjust tier formatting to show blank cells and header column on the left
- [ ] Fix audio clipping issue with new .eaf files
- [x] Add and show metadata information
- [ ] Fix bug that prevents English dictionary from loading
