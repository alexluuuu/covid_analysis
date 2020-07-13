# Analysis of interaction between SARS-CoV-2 sequence variation and predicted HLA binding 


## set up 

Python is a coding language that is great because it is quite readable, and pretty easy to get started with. One of the things about Python is that there are a lot of existing packages -- this means we don't have to reinvent the wheels super often. There are also a variety of tools that allow for efficient management of packages. This means we can control 1) which version of Python we're using, 2) which version of packages we're using, 3) install everything at once. 

For package management, I use Miniconda. Go to this link to install Miniconda for MacOSX: https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html

Essentially, you can just follow these steps: 

1. Open Terminal app. 

2. If you haven't done any coding before, it'll be helpful for you to run this command: 

```bash
xcode-select --install
```

3. Copy paste the following commands. 

```bash 
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh $HOME/miniconda
```

I think the installer should ask “Do you wish the installer to initialize Miniconda3 by running conda init?” and you should answer yes. 

I'm pretty you should be good after this. I think in your terminal window, you can enter the command

```bash
python
```

and I hope you can see something like the following output: 

```
Python 2.7.16 |Anaconda, Inc.| (default, Aug 13 2019, 12:00:15) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

The important part here is that you see something like "Anaconda, Inc.| (default, Aug 13 2019, 12:00:15) " after `Python <version number>`. 



Next, we're going to talk about setting up our Conda environment. 


## conda environments 

So the first step is actually to set up github. Because you have a .edu email, you can get a free Github Pro account: https://education.github.com/pack


After you've made an account, you can go to this link and follow the instructions: https://kbroman.org/github_tutorial/pages/first_time.html

Now that Github is set up, you want to clone (basically, download) this repository. You can do this by doing the following: 

```bash
cd 
cd Documents/
git clone https://github.com/alexluuuu/covid_analysis.git
```

Feel free to change the `cd` command to put the cloned repo into a different directory. 

Note that there is an file called `environment.yml` in this repository. It contains the name of a local environment that we will be using, and which packages should be included in this environment. To initialize a local env based on this configuration file, do the following:

```bash
cd covid_analysis
conda env create -f environment.yml
```

If prompted about the installation of packages, enter "y". 

If we ever need to update this conda environment, we'll make change the list of packages in the environment.yml file and run the following command: 

```bash 
conda env update --prefix ./env --file environment.yml  --prune
```

You can activate the local environment by doing: 

```bash
conda activate bioinformatics 
```

You can deactivate the local environment by doing: 

```bash
conda deactivate
```

**It would be best if you activate the local environment whenever we're working on code** 

It's probably helpful for you to read the following: 
https://medium.com/crowdbotics/a-dead-simple-intro-to-github-for-the-non-technical-f9d56410a856

I will continue to push changes to this repository over the next few days, so you might want to pull them (sync down from repository in cloud to your local machine). 


## Getting started on some code 

Here's the official Python tutorial: https://docs.python.org/3/tutorial/introduction.html

I feel like you can jump to Chapter 3, but if you want to be really thorough, Ch1-2 should be good too. 

I've also attached a starter code file `starter.py`. I've attached a lot of explanations in that file for how things work. 


