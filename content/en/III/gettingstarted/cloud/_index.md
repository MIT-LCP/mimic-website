+++
title = "Cloud access"
linktitle = "Cloud"
toc = false

+++

<!-- 
NOTE: the content below was copied directly from the /iv/access/cloud .md page.  If an automated way of duplicating this content while keeping it under the /iii/ path can be determined it should be implemented.
-->

MIMIC-III and MIMIC-IV are made available via Physionet: [MIMIC-III](https://physionet.org/content/mimiciii/), [MIMIC-IV](https://physionet.org/content/mimiciv/). Beyond directly downloading the dataset from PhysioNet, there are a few mechanisms for accessing the data:

* Accessing the data in BigQuery
* Accessing the data on AWS (MIMIC-III)
* Accessing the data in a Google Cloud storage bucket (MIMIC-IV)

We **highly** recommend using MIMIC in BigQuery for the following reasons:

* No setup required
* Updates will be integrated into BigQuery when they are available
* Derived concepts from the [MIMIC code repository](https://www.github.com/MIT-LCP/mimic-iv) are precomputed and available on the `mimic_derived` dataset

If absolutely necessary, it is possible to download the data from a Google cloud bucket; instructions are provided at the end of the document.
Please do keep in mind that the PhysioNet team is covering the cost of downloading the dataset.

## Accessing data on the cloud

There are three steps to accessing data on the cloud:

1. Link your cloud account to your PhysioNet profile
2. Request access to the cloud resource
3. Log-in to the appropriate service and navigate to the resource

These steps assume you are already credentialed and have signed the data use agreement for MIMIC-IV.
If you have not, read this page for instructions on gaining access to [MIMIC-III](/iii/gettingstarted/access) or [MIMIC-IV](/iv/access).




<!--
NOTE: This was the only page (/getttingstarted/_index.md) for info on cloud access on the original MIMIC III website.  To consolidate with the MIMIC IV content, I'm breaking this into sections.

MIMIC is available for use via two cloud platforms: Google Cloud Platform (GCP) and Amazon Web Services (AWS). Access to these services is directly controlled via your PhysioNet account.

In order to use MIMIC on the cloud, you must:

1. Be an approved user on PhysioNet. [Read this page for instructions on gaining access to MIMIC-III.](/iii/gettingstarted/access)
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
*If* the page shows a restricted-access warning, you need to [get access to MIMIC-III](/iii/gettingstarted/access) or sign the data use agreement for this project.
Otherwise, you should see the following:

![Methods for accessing MIMIC-III](/img/cloud/mimic_files.png)

The following describes the access options listed above in the order they are listed:

1. Downloading the data as one large zip file
  * This downloads the data directly from the PhysioNet servers.
2. **Cloud**: Adds your GCP e-mail to the access list for GCP BigQuery.
  * This option adds the GCP e-mail in your PhysioNet account to a BigQuery access list; it's required in order to use the data in BigQuery.
3. **Cloud**: Adds your GCP e-mail to the access list for downloading the data from a GCP Storage Bucket.
  * This option adds the GCP e-mail in your PhysioNet account to a GCP access list; it's required in order to download the data from a storage bucket on GCP.
4. **Cloud**: A public page for viewing the data description in the AWS Open Data Repository.
  * This forwards you to the AWS Open Data Repository listing of the data. For information on how to use AWS, we [recommend reading this tutorial](https://aws.amazon.com/blogs/big-data/perform-biomedical-informatics-without-a-database-using-mimic-iii-data-and-amazon-athena/).
5. **Cloud**: Adds your AWS account ID to the access list for AWS.
  * This is necessary in order to access the data via AWS services. For information on how to use AWS, we [recommend reading this tutorial](https://aws.amazon.com/blogs/big-data/perform-biomedical-informatics-without-a-database-using-mimic-iii-data-and-amazon-athena/).
6. Provides a command for downloading the data from PhysioNet as individual CSV files using `wget` (when compared to the image above, your command will have a distinct username).
  * This downloads the data directly from PhysioNet servers, but in their raw (usually uncompressed) form.

Options #1, #3, #4, and #6 all provide the ability to download the data locally. For the remainder of this guide, we will focus on the two options which provide access to the data in a cloud based relational database (#2 and #5 in the above).

## GCP - BigQuery

BigQuery is a columnar, distributed relational database management system. BigQuery accesses only the columns specified in the query, making it ideal for data analysis workflows. [Read more about BigQuery on Google.](https://cloud.google.com/bigquery/)

Once you have requested access to using MIMIC-III on BigQuery, you need to "pin" the dataset to see it on the web browser. This adds the dataset to the sidebar in BigQuery. While not required, we do recommend pinning the data for easier navigation.

1. Ensure you have added a gmail account to your PhysioNet profile as described above.
2. Go to the BigQuery console: http://console.cloud.google.com/bigquery while logged into your gmail account.
3. If you haven't created a BigQuery project previously you will be asked to do so.  You will need to enter information
   to pay for the cost of queries.  For more details see: https://cloud.google.com/resource-manager/docs/creating-managing-projects  
4. On the left sidebar, next to "Resources", click "+ ADD DATA", followed by "Pin a project"
![Pin data for easy access](/img/cloud/bq/pin_data.png)
5. In the pop up window, type `physionet-data`, and click "PIN".
![Type physionet-data to pin the MIMIC-III data project](/img/cloud/bq/pin_physionet_data.png)
6. In the sidebar on the left, you should now see the `physionet-data` project. Click the arrow to the left of `physionet-data` to expand the project.
7. You should now see the following projects: `eicu_crd_demo`, `mimiciii_clinical`, `mimiciii_demo`, `mimiciii_notes`, and `mimiciii_derived`. Make sure you are logged in under your project that pays for queries: /bigquery?project=paying-project-name . You are ready to query the data! Try a simple query in the main dialogue box:

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


#### I can only see `eicu_crd_demo` and `mimiciii_demo`

These datasets are fully public, so the implication is that you have not been granted access to the full versions of the databases.
Please (1) double check you have entered your cloud information into your PhysioNet profile, verifying any e-mails as needed, and (2) requested access to the specific cloud project on its respective PhysioNet project page.
-->