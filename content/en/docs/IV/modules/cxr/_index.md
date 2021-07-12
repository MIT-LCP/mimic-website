---
title: "CXR"
linkTitle: "CXR"
date: 2020-08-10
weight: 50
description: >
  The CXR module provides lookup tables linking patient identifiers with MIMIC-CXR `study_id` and `dicom_id`, allowing analysis of patient chest x-rays to be linked with the clinical data from other MIMIC-IV modules.  
---


{{% pageinfo %}}
In order to access this module, you must sign the data use agreement for MIMIC-CXR and request access to MIMIC-CXR data on BigQuery via the [MIMIC-CXR PhysioNet project page](https://physionet.org/content/mimic-cxr/).
{{% /pageinfo %}}


MIMIC-CXR contains 227,835 imaging studies for 64,588 patients presenting to the Beth Israel Deaconess Medical Center Emergency Department between 2011 - 2016. A total of 377,110 images are available in the dataset.
Each imaging study can contain one or more images, usually a frontal view and a lateral view.
Studies are made available with a semi-structured free-text radiology report that describes the radiological findings of the images, written by a practicing radiologist contemporaneously during routine clinical care.
All images and reports have been de-identified to protect patient privacy.

A records file, `cxr-record-list.csv.gz`, provides a mapping between the image (dicom_id), the study (study_id), and the patient (subject_id).
Another records file, `cxr-study-list.csv.gz`, provides a mapping between the studies (`study_id`) and patients (`subject_id`).

All patient identifiers begin with the digit 1 and have a total length of 8 digits.
All study identifiers begin with the digit 5 and have a total length of 8 digits.
DICOM file names are unique 40 character hexadecimal strings with dashes separating groups of eight characters.

Images are provided in DICOM format; see the [image](#images) section for more information about the images.

Reports are provided as plain text files; see the [reports](#deidentified-free-text-radiology-reports) section for more information about the reports.

## Data Organization

Data files are made available in a hierarchical strcture.
The following block lists the first patient's records as an demonstrative example (MIMIC-CXR v2.0.0):

```
files/
 p10/
   p10000032/
    s50414267/
      02aa804e-bde0afdd-112c0b34-7bc16630-4e384014.dcm.gz
      174413ec-4ec4c1f7-34ea26b7-c5f994f8-79ef1962.dcm.gz
    s53189527/
      2a2277a9-b0ded155-c0de8eb9-c124d10e-82c5caab.dcm.gz
      e084de3b-be89b11e-20fe3f9f-9c8d8dfe-4cfd202c.dcm.gz
    s53911762/
      68b5c4b1-227d0485-9cc38c3f-7b84ab51-4b472714.dcm.gz
      fffabebf-74fd3a1f-673b6b41-96ec0ac9-2ab69818.dcm.gz
    s56699142/
      ea030e7a-2e3b1346-bc518786-7a8fd698-f673b44c.dcm.gz
    s50414267.txt
    s53189527.txt
    s53911762.txt
    s56699142.txt
 ...
 ```

You will note a high level folder: `p10`. This is done to avoid having many files in a single directory.
All patient folders are stored in a higher level folder which is identical to the first 3 characters of their folder name, i.e. `p10000032` will be in folder `p10`, `p11000011` will be in `p11`, and so on.


Above, this patient (`10000032`) has four studies. Most of the studies have two scans (usually a frontal and a lateral chest x-ray), but one study `56699142` has only one image.
Each study is associated with a de-identified free-text radiology report (e.g. s56699142.txt).
Note that the identifiers are random, and do not indicate order of the studies in any way.

## Images

Chest radiographs were sourced from the hospital picture archiving and communication system (PACS) in Digital Imaging and Communications in Medicine (DICOM) format.
DICOM is a common format which facilitates interoperability between medical imaging devices. Put simply, the DICOM format contains structured meta-data associated with one or more images, and the DICOM standard stipulates strict rules around the structure of this information.
The DICOM standard is updated regularly each year. MIMIC-CXR is built according to the [DICOM Standard version 2017e](http://dicom.nema.org/medical/dicom/2017e/).

<!--
If you have never worked with DICOM images before, we highly recommend you work through our [tutorial on working with DICOMs]() 


The PACS workstation used by clinicans to view images allows for dynamic adjustment of the mapping between pixel value and grey-level display (``windowing''), side-by-side comparison with previous imaging, overlaying of patient demographics, and overlaying of imaging technique. Reports are  transcribed during reading of an image series using a real-time computer voice recognition service.
-->

## Deidentified free-text radiology reports

During routine care, radiologists will review chest radiographs and document their interpretation electronically.
When reviewing a radiograph, radiologists have access to: (1) brief text written by another clinician summarizing the underlying medical condition, (2) the reason for examination, and (3) prior imaging studies performed.

Reports in MIMIC-CXR are semi-structured, and have linebreaks to ensure individual lines are no longer than 79 characters.
As reports are templated, structure is seeded in the reports, but radiologists are free to modify it as they will before saving.
Most reports will contain a ``FINDINGS'' and ``IMPRESSION''. The findings section details the radiologists assessment of the image, while the impression section acts as a summary of the most pertinent findings.

Reports sometimes have addendums at the top. Addenums are added after the radiology report has already been written, and are intended to clarify language as necessary. Addendums are delimited from the original report by underscores which span an entire line.

Radiology reports have been de-identified to protect patient privacy. All patient information has been replaced with three underscores (`___`). Provider information has also been removed.

The following is an example radiology report from MIMIC-CXR:

```
                                 FINAL REPORT
 EXAMINATION:  CHEST (PA AND LAT)
 
 INDICATION:  ___ year old woman with ?pleural effusion  // ?pleural effusion
 
 TECHNIQUE:  Chest PA and lateral
 
 COMPARISON:  ___
 
 FINDINGS: 
 
 Cardiac size cannot be evaluated.  Large left pleural effusion is new.  Small
 right effusion is new.  The upper lungs are clear.  Right lower lobe opacities
 are better seen in prior CT.  There is no pneumothorax.  There are mild
 degenerative changes in the thoracic spine
 
 IMPRESSION: 
 
 Large left pleural effusion
```

## MIMIC-CXR v2.0.0

The current version of the database is v2.0.0. When referencing this version, we recommend using the full title: MIMIC-CXR v2.0.0.

MIMIC-CXR v2.0.0 is the first release of the images in their native format, DICOM, and the first release of the free-text radiology reports associated with these images. All data has been de-identified prior to release to protect patient privacy.


## Past versions

#### MIMIC-CXR v1.0.0

MIMIC-CXR v1.0.0 was released on 22 January 2019.
The data contains only JPG format images and 14 structured labels extracted from an NLP tool.
The images are identical to MIMIC-CXR v2.0.0, and we no longer distribute v1.0.0.
Researchers interested in JPG format images with NLP derived labels can find them in the [MIMIC-CXR-JPG project](https://physionet.org/content/mimic-cxr-jpg/).