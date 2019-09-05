# Website and documentation for the MIMIC Critical Care Database [![Build Status](https://travis-ci.org/MIT-LCP/mimic-website.svg?branch=master)](https://travis-ci.org/MIT-LCP/mimic-website)

## Instructions for running the website locally

1. Install Go and Hugo. For instructions, see: http://gohugo.io/overview/installing/
2. Clone the website repository:
   ```
   git clone https://github.com/MIT-LCP/mimic-website.git
   ```
3. Run ```hugo server``` at the command line to build the website and serve the pages;
4. View the website at: http://127.0.0.1:1313

## Note on deploying the website

Automatic builds have not yet been implemented. Currently deploys using the method described at: http://www.andrewcodispoti.com/deploy-process/

## Issues with the website or MIMIC

Please raise issues related to the website or MIMIC-III in the [mimic-code repository](https://github.com/mit-lcp/mimic-code).