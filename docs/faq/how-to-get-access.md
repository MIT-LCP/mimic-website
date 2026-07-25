---
title: How do I access MIMIC?
layout: default
nav_order: 10
parent: FAQ
---

# How do I get access to MIMIC?

Getting access to MIMIC data requires completing human subjects training and signing a data use agreement. Here is the step-by-step process:

## Step 1: Complete PhysioNet Credentialing

1. **Create a PhysioNet account** at [physionet.org](https://physionet.org)
2. **Complete the credentialing process**:
   - Take the required training course in human subjects research
   - Provide your institutional affiliation
   - Submit reference information (required for students/postdocs)
3. **Wait for approval**. Please be patient, we try to process applications within 1-2 weeks.

{: .important }
> **Students and Postdocs**: You must provide your supervisor's contact information as a reference. Do not list yourself as a reference.

## Step 2: Sign the Data Use Agreement

Once credentialed:

1. **Log in** to your PhysioNet account
2. **Navigate** to the dataset page you need:
   - [MIMIC-IV](https://physionet.org/content/mimiciv/)
   - [MIMIC-IV-Note](https://physionet.org/content/mimic-iv-note/)
   - [MIMIC-IV-ED](https://physionet.org/content/mimic-iv-ed/)
   - [MIMIC-IV-ECG](https://physionet.org/content/mimic-iv-ecg/)
   - [MIMIC-CXR](https://physionet.org/content/mimic-cxr/)
   - [MIMIC-III](https://physionet.org/content/mimiciii/)
3. **Review and sign** the Data Use Agreement (DUA)
4. **Download** or access data through cloud platforms

## Step 3: Choose Your Access Method

### Cloud Access (Recommended)
- **Google Cloud (BigQuery)**: Easiest for SQL queries
- **AWS**: Available for MIMIC-III
- **Google Cloud Storage**: Direct access to data within GCP

### Local Download
- Download individual CSV files
- Set up a local PostgreSQL database
- Requires more setup but provides full control

## Common Questions

### How long does credentialing take?
Typically 1-2 weeks if all information is complete. Incomplete applications may be delayed or rejected.

### Can I access data immediately after signing the DUA?
Yes, for cloud platforms. Local download may take additional time depending on file sizes.

### Do I need separate access for each dataset?
Yes, you need to sign separate DUAs for MIMIC-III, MIMIC-IV, MIMIC-CXR, MIMIC-IV-Note, MIMIC-IV-ED, and MIMIC-IV-ECG.

## Troubleshooting

### Application Rejected
- Ensure all required fields are completed
- Provide a valid institutional email address (not required, but helpful)
- Include the correct CITI training: make sure it is "Data or Specimens Only Research"
- Include the CITI *Completion Report*, not just the certificate
- Include proper reference information
- Contact credentialing at PhysioNet if issues persist

### Can't Find Reference Information
- Use your supervisor or department head
- Must be someone who can verify your affiliation
- Should not be yourself or a peer student

## Next Steps

Once you have access:

1. **Start with the [Getting Started guide](/docs/gettingstarted/)** to set up your access method
2. **Understand the data** - Read the [Core concepts](/docs/iv/about/concepts/) page
3. **Join the community** - Follow the [Community guidelines](/docs/community/)

---

{: .highlight }
> Remember: The Data Use Agreement is legally binding. Make sure you understand and can comply with all terms before signing.
