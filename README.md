# fakenews detector (Frankie)
Disinformation are spreading like wildfire in Europe, for political or commercial manipulation, hampering efforts to contain the pandemic, and ripping apart our society’s social fabric. Lives literally depend on all of us listening to health authorities and our ability to access, rely and trust reliable information. Yet more and more European citizens find themselves unable to do so.\
\
Many technical approaches against the spread of fake news either rely entirely on human fact-checks or entirely on AI. We want to combine the accuracy and pluralism of fact-checks from trusted journalists with the scalability machine based validation.\
\
We also see this as an opportunity to showcase the excellent work already done by fact-checkers and to raise citizens' awareness of the importance of media pluralism and the unprecedented existential challenge COVID represents for the news sector.\
\
We will leverage our existing contacts to partner with fact-checkers, traditional media, European civil society and policymakers for our product dissemination and continuous improvement. We are also committed to transparency and a human rights-based approach – including with regards to the recognition of the intrinsic limitations of the technology that we offer.
# What Frankie does:
“Frankie”, detects disinformation about COVID-19 by checking if similar texts were already debunked on a website of independent fact-checkers and high-quality publishers. If that is the case we provide a link to the fact-check and thus not only inform the user of a disinformation but also help to disseminate the work of these organizations.\
\
We provide multiple Interfaces for users to interact with our system. For this Hackathon we want to develop:
1. A chrome extension, which "scans" visited websites on disinformation about COVID-19
2. A text field on our website, where users can insert texts from sources like Whatsapp or Facebook
3. A public API which is not only used by the previous UIs but can also be embedded into other Apps

# How to run Chrome Extension and Server Locally
Let's start with the server, assuming python3 is already installed. We highly recommend the usage of a virtual environment but the first step can also be ommitted. 

1. Setup virtualenv (if not installed yet follow these instructions: [Link](https://virtualenv.pypa.io/en/stable/installation.html))
```bash 
cd path/to/your/fakenews/directory
python3 -m virtualenv ./env
source env/bin/activate
pip install -r requirements.txt
```

2. Run local development server
```bash
python wsgi.py
```

3. Install Chrome Extension:
  a. Go to you chrome browser and enter `chrome://extensions`
  b. In the upper right corner enable the developer mode by clicking on the switch button.
  c. Click on Load unpacked in the upper left corner
  d. Select path/to/your/fakenews/dir/chrome_app
  f. Optional: Adapt score threshold by clicking on Details -> Extension options
  g. Have fun with Frankie (e.g. test it on https://www.poynter.org/?ifcn_misinformation=coronavirus-was-created-from-hiv)

# Data resources and visualization
update with visualization of poynter data
# Models and results:
\
\
\
\
# Disclaimer: 
