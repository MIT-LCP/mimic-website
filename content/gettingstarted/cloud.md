+++
title = "Cloud"
linktitle = "Cloud"
weight = 3
toc = false

[menu]
  [menu.main]
    parent = "About"

+++

# Cloud access

MIMIC is available for use via two cloud platforms: Google Cloud Platform (GCP) and Amazon Web Services (AWS). Access to these services is directly controlled via your PhysioNet account.

In order to use MIMIC on the cloud, you must:

1. Be an approved user on PhysioNet. [Read this page for instructions on gaining access to MIMIC-III.](/gettingstarted/access)
2. Add cloud credentials to your PhysioNet profile
3. Request access on the MIMIC-III PhysioNet project page

## Adding cloud credentials

Go to your PhysioNet profile page.

![Profile page on PhysioNet](/img/cloud/profile.png)

Click "Emails":

![Navigate to the e-mails page](/img/cloud/emails.png)

For GCP access, ensure that one of your e-mails is a Google account. This can either be a gmail account (as in the picture), or a G Suite account if your organization is a member of G Suite. You can add an e-mail at the bottom of the page:

![Navigate to the Cloud page](/img/cloud/add_email.png)

You will need to verify your e-mail address before continuing (note: e-mail addresses are only used for GCP access, and not for AWS access).

Once you have a verified e-mail address ready, navigate to the "Cloud" page on PhysioNet.

![Navigate to the Cloud page](/img/cloud/cloud_page.png)

You should see two options on this page: one for GCP, and one for AWS.

![Profile cloud credentials](/img/cloud/credentials.png)

For GCP, click the drop down menu and set your GCP e-mail to the Google account you provided in the earlier step.

For AWS, add your AWS canonical ID. This is *not your e-mail*. It is a numeric identifier that can be found in your AWS cloud profile. [Click here to go to your AWS profile page](https://console.aws.amazon.com/billing/home?#/account). Then look for your "Account Id":

![AWS ID](/img/cloud/aws/aws_id.png)

## Accessing a project on the cloud

Now that your cloud credentials are available in PhysioNet, you can request access to databases within those cloud systems.
Cloud access to PhysioNet projects such as MIMIC-III and eICU-CRD are managed independently. You must request access to the cloud systems via their project pages (access is provisioned instantly for credentialed approved users).

## Accessing MIMIC-III on the cloud

For MIMIC-III, go to the [MIMIC-III PhysioNet project page](https://physionet.org/content/mimiciii/1.4/).

Once there, scroll to the bottom to the "Files" section.
*If* the page shows a restricted-access warning, you need to [get access to MIMIC-III](/gettingstarted/access) or sign the data use agreement for this project.
Otherwise, you should see the following:

![Methods for accessing MIMIC-III](/img/cloud/mimic_files.png)

The following describes the access options listed above in the order they are listed:

* Downloading the data as one large zip file
* **Cloud**: Adds your GCP e-mail to the access list for GCP BigQuery.
* Adds your GCP e-mail to the access list for downloading the data from a GCP Storage Bucket.
* A public page for viewing the data description in the AWS Open Data Repository.
* **Cloud**: Adds your AWS account ID to the access list for AWS.
* Provides a command for downloading the data from PhysioNet as individual CSV files using `wget` (your command will have a different username).

For cloud access, the 2nd and 5th options are the relevant items. Click the one which you would like to use. Then, proceed to the appropriate section below.

## GCP - BigQuery

BigQuery is a columnar, distributed relational database management system. BigQuery accesses only the columns specified in the query, making it ideal for data analysis workflows. [Read more about BigQuery on Google.](https://cloud.google.com/bigquery/)

Once you have requested access to using MIMIC-III on BigQuery, you need to "pin" the dataset to see it on the web browser. This adds the dataset to the sidebar in BigQuery. While not required, we do recommend pinning the data for easier navigation.

1. Go to the BigQuery console: http://console.cloud.google.com/bigquery
2. On the left sidebar, next to "Resources", click "+ ADD DATA", followed by "Pin a project"
![Pin data for easy access](/img/cloud/bq/pin_data.png)
3. In the pop up window, type `physionet-data`, and click "PIN".
![Type physionet-data to pin the MIMIC-III data project](/img/cloud/bq/pin_physionet_data.png)
4. In the sidebar on the left, you should now see the `physionet-data` project. Click the arrow to the left of `physionet-data` to expand the project.
5. You should now see the following projects: `eicu_crd_demo`, `mimiciii_clinical`, `mimiciii_demo`, `mimiciii_notes`, and `mimiciii_derived`. You are ready to query the data! Try a simple query in the main dialogue box:

```sql
SELECT *
FROM `physionet-data.mimiciii_clinical.icustays`
WHERE icustay_id < 200100
ORDER BY icustay_id
```

The query should return some data, and your browser window should be similar to the below:

![Example output for the query](/img/cloud/bq/example_query.png)

At this point you are ready to use MIMIC on BigQuery!

A tutorial on using BigQuery to query MIMIC-III is available [here](/tutorials/intro-to-mimic-iii-bq.md).

Note that we have a number of pre-generated "views" of the data. These are available in the `mimiciii_derived` dataset which you are free to query. All code used to generate these views has been made openly available in the [google-cloud-views branch of the MIMIC code repository](https://github.com/MIT-LCP/mimic-code/tree/google-cloud-views).

If you are having issues, see the [Troubleshooting section](#troubleshooting).

## AWS

Recently, the MIT Laboratory of Computational Physiology (LCP) started hosting the MIMIC-III dataset on the AWS cloud through the AWS Public Dataset program. You can now use the MIMIC-III dataset via S3 without having to download, copy, or pay to store it. Instead, you can analyze the MIMIC-III dataset in the AWS Cloud using AWS services like Amazon EC2, Athena, AWS Lambda, or Amazon EMR. AWS Cloud availability enables quicker and cheaper research into the dataset.

Services like Athena also offer you new analytical approaches to the MIMIC-III dataset. Using Athena, you can execute standard SQL queries against MIMIC-III without first loading the data into a database. Because you can reference the MIMIC-III dataset hosted by MIT LCP in Amazon S3, your analyses always reference the most recent version of the MIMIC-III dataset. Live hosting reduces upfront time and effort, eliminates data synchronization issues, improves data analysis, and reduces overall study costs.

Once you have successfully requested access to MIMIC-III on AWS, you can follow the instructions linked below. These instructions initialize and execute an entire study performed on MIMIC-III using a hosted Jupyter notebook service on AWS.

https://aws.amazon.com/blogs/big-data/perform-biomedical-informatics-without-a-database-using-mimic-iii-data-and-amazon-athena/



## Troubleshooting

### GCP

#### I get a pop-up about Terms of Service

![Agree to the terms of service](/img/cloud/bq/agree_tos.png)

You will need to agree to all GCP Terms of Service and adhere to their terms in order to use the data on BigQuery.

#### When I go to BigQuery, it asks me to create a project

![Create a project on GCP](/img/cloud/bq/create_project.png)

Almost all of your interactions with GCP are associated with a *project*. Importantly, all billing for your usage must be allotted to a single project.
In order to use BigQuery you must have an activate project associated with your account. BigQuery offers a $300 free trial for first time users.

Create a project and select it as your activate project. If you've done this correctly, then the top bar of the Google console page should stop saying "Select a project", and instead have your project name. For example, in the below, I have selected the project `alistairewj`, which is now the activate project:

![Example of a working activate project](/img/cloud/bq/active_project.png)

