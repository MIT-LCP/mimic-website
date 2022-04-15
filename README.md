# Website and documentation for the MIMIC Critical Care Database

## Instructions for running the website locally

1. Install Go and Hugo. For instructions, see: http://gohugo.io/overview/installing/
2. Clone the website repository:
   ```
   git clone --recursive https://github.com/MIT-LCP/mimic-website.git
   ```
3. Run ```hugo server``` at the command line to build the website and serve the pages;
4. View the website at: http://127.0.0.1:1313

## Note on deploying the website

* 1: Add mimic-production to remote
After the pull request of the new material is merged into the main branch of mimic-website, pull down the latest version of main to your local repo. Run the following command after filling in the IP address for server Heimdallr:
 
`git remote add mimic-production webuser@<IP address for Heimdallr>:/home/webuser/mimic-website.git`
 
* Optional: Check if the command above ran correctly,
Run command: `git remote -v`
should return:
Mimic-production webuser@<IP address for Heimdallr>:/home/webuser/mimic-website.git (fetch)
Mimic-production webuser@<IP address for Heimdallr>:/home/webuser/mimic-website.git (push)
origin   https://www.github.com/MIT-LCP/mimic-website (fetch)
origin   https://www.github.com/MIT-LCP/mimic-website (push)
 
* 2: Sshuttle into the production server
 
Run the following command after filling in the  LCP username and IP address: `alias sshcsail="sshuttle -r <LCP username>@heimdallr.csail.mit.edu <IP address for Heimdallr>/24"`
 
Run command: `sshcsail`
 
Should return:  “client: Connected” after you enter your password
 
* 3: Push development
 
In another terminal from your mimic-website repo:
 
Run command: `git push mimic-production`


 
* Note:
Your public key (for the machine you're pushing from) must be in the webuser group


## Issues with the website or MIMIC

Please raise issues related to the website or MIMIC-III in the [mimic-code repository](https://github.com/mit-lcp/mimic-code).