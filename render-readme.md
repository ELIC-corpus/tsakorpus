## Launch on Render

The goal is to deploy Tsakorpus for internal lab use on a non-local website. The architecture consists of two services:

1) Frontend WSGI app (Tsakorpus) served via Gunicorn

2) Elasticsearch backend running as a service to power search and indexing

Render.com was chosen for deployment due to its simple GitHub integration, support for Docker, and ease of setting up internal/private services.

Some alternatives to Render are: 

* Railway (This service actually has a prebuilt Elasticsearch add-on)

* Fly.io

# Setup

Tsakorpus works by running Elasticsearch (database backend) and the tsakorpus web-interface (frontent). We want to replicate this on Render, 
and just as we would have to run two processes on our local machines (elastic search & wsgi), we need to make two web-services within the project that work in parallel.

Here is what has been already done for (1) and (2):

1) Reviewed tsakorpus repo and set up (requirements.txt, etc). This should be ready to launch! When we pull this into Render, the autofilled forms
   are all correct for now. The application runs via: ```gunicorn tsakorpus.wsgi:application```

2) I created a small local instance of elastic search in a seperate public repository on the ELIC github. I made a Docker file and a .render.yaml config file.
   This launches but fails to find a port. **This is the current bug!**

# Next Steps

If we can get the elastic search to run and find the right port, which should be a matter of changing settings, we can launch the front-end in the same way and the
website will be available. Otherwise, we might have to switch to Railway ($5/month for the hobby plan and has built-in ElasticSearch). Then, the issue becomes
password protection.

My reccomendation is: Push until Friday to get Render to work, if we can't do it, give up and switch to Railway. 

Once we have these two processes running, we can just make edits to the repositories (we would really only change the tskaorpus repo though) and we should see the website update
automatically. 
