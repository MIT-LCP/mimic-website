---
title: "Google Cloud Storage"
linktitle: "Google Cloud Storage"
date: 2020-08-10
weight: 5
description: >
  Access the MIMIC datasets on Google Cloud Storage (GCS).
---

The MIMIC databases are hosted on Google Cloud Storage (GCS). Access to the bucket, if available, can be requested via the PhysioNet project page. See [this page for more detail on this process](/docs/gettingstarted).

Datasets available on GCS include:

- [MIMIC-III](https://physionet.org/content/mimiciii/)
- [MIMIC-IV](https://physionet.org/content/mimiciv/)
- [MIMIC-CXR](https://physionet.org/content/mimic-cxr/)\*\*
- [MIMIC-ED](https://physionet.org/content/mimic-iv-ed)


\*\* MIMIC-CXR is over 4.7 TB, almost entirely due to the size of the DICOMs.
Users should strongly consider *not* downloading the data, and instead using it within Google Cloud Platform (GCP), which we support natively.
GCP does not charge for data transfer within a region in GCP ([see this page for more details about network charges.](https://cloud.google.com/storage/pricing#network-pricing)).

# Downloading a dataset using `gsutil`

`gsutil` is a command-line tool for interacting with object stores.
You'll need to install `gsutil` locally and authenticate with the same Google account you have linked to your PhysioNet account.

See their instruction page for details on the install and configuration process: https://cloud.google.com/storage/docs/quickstart-gsutil

Once you have `gsutil` installed and authenticated, you can download a dataset using the `gsutil -m cp` command, where `-m` requests multiprocessing. For example, you can download MIMIC-IV as follows:

```
gsutil -m cp -r gs://mimiciii-1.4.physionet.org ./
```

... which will download all the data (~7 GB) in the MIMIC-III project to your local folder.