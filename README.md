# tsakorpus
An implementation of the Tsakorpus platform for ELIC

## Setup: running locally
A guide for setting up tsakorpus from scratch on the UGA corpus server is available in `tsakorpus_setup.ipynb`. Alternatively, to run and view tsakorpus locally, you can

0. Setup a virtual environment and install all necessary packages
1. Clone this repository
   - **NOTE:** the directory containing the actual converted JSON files is listed under .gitignore (a decision made by the Tsakorpus creator). We will need to decide if we want to overwrite this and include all .eaf or converted JSON files. Until then, the corpus will not run "out of the box" unless you create a `corpus/elic` directory and add converted JSON files to it.
2. Install and run elasticsearch
3. Start the corpus interface with `python tsakorpus.wsgi` within the `search` directory
4. Go to http://127.0.0.1:7342/search

## Setup: updating Railway deployment
These steps index the corpus to the Elasticsearch instance in Railway and download all media files to the deployed directory that Railway is reading from to run the website. 

1. Run `fix_media_files.py`
2. Run `eaf2json.py`
3. Run `edit_jsons.py` to add metadata information
4. Run indexator (with updated "elastic_url" in `conf/corpus.json` pointed at Railway Elasticsearch)
5. Download media files to local computer and upload to onedrive, get download url and change end of url from `...dl=0` to `...dl=1'
6. Install Railway CLI, link account and ssh into Tsakorpus project
7. Download media files into Railway volume with:
```
curl -fSL 'https://www.dropbox.com/media/files/location/...dl=1' -o /tmp/media.tgz
mkdir -p /search/media
tar -xzf /tmp/media.tgz -C /search/media --strip-components=2
```

---
## To-do
- [x] Show tiers for each word in search results when searching sentences
- [x] Fix tiers to show correct information
- [x] Fix audio clipping issue with new .eaf files
- [x] Add and show metadata information
- [ ] Fix bug that prevents English dictionary from loading
- [x] Deploy on ~~AWS~~ Railway
- [x] Add password protection

### Railway deployment bugs
- [x] Correct spelling of Čakavian
- [ ] Fix .csv & .xlsx file download issues
- [ ] Fix "expand context" button
- [x] Add other languages
- [ ] Fix virtual keyboard
- [ ] Check copying to clipboard