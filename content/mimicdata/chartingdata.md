
# How is data recorded in the database?

The data in the database is recorded during routine clinical care. As a result, the data is collected for the purpose of patient care, and *not* for the purpose of retrospective data analysis. This is a key point to consider at all times when analyzing the data: while it may not be archived in an optimal way for analysis, this is not the primary purpose of the data. This is partly implied by the nature of this research: *secondary* analysis of electronic health records.

# Types of data in the database

There are two types of data in the database: static data and dynamic data. Static data is recorded once for a given identifier. An example of static data is the `DOB` column in the PATIENTS table. Each patient has only one date of birth, which does not change over time and is not recorded with an associated timestamp. In contrast, an example of dynamic data is a patient's blood pressure, which is aperiodically measured during their stay in the ICU. Note that this distinction between static data and dynamic data is merely a helpful conceptual construct: there is *no* strict technical distinction between date of birth and heart rate. However, static data tends to not have an associated `ITEMID` (as there is no need to repeatedly record values for static data), whereas dynamic data must have an `ITEMID` to facilitate repeated measurements.

## Static

Each patient or hospital admission is associated with a set of "static" data. Often this is demographic, admission, billing or other administrative data. This data is classified as static as it does not change during a patient's stay: it occurs only once for a given `HADM_ID`. The only static data available for a patient is their gender (`GENDER`), date of birth (`DOB`) and various dates of death (`DOD`, `DOD_HOSP`, `DOD_SSN`). These columns all occur in the PATIENTS table.

The following is a list of static data available in the database for `HADM_ID`:
* Admission time
* Discharge time
* Death time
* Admission type


The following is a list of static data available in the database for `ICUSTAY_ID`:
* Admission time
* Discharge time
* First care unit
* Last care unit

TODO: ?? Is this section useful??

## Dynamic

### Recording the time of dynamic observations

Most data, with the exception of patient related demographics, is recorded with a time indicating when the observation was made: `CHARTTIME`. `CHARTTIME` dates back to the use of paper charts: in order to facilitate efficient observations by nursing staff, the day was separated into hourly blocks and observations were recorded within these hourly blocks. Thus, any time one performed a measurement between the hours of 04:00 and 05:00, the data would be charted in the 04:00 block, and so on. This concept has carried forward into the electronic recording of data: even if data is recorded at 04:23, in many cases it is still charted as occurring at 04:00. 

### Automatic synchronization of data

Many of the monitors in the ICU continuously update the ICU database with observations of the patient. For example, patients with an ECG (i.e. almost all ICU patients) have a heart rate continuously input into the database every minute. However, casual inspection of the database will indicate that heart rate is measured far less frequently than once per minute. In fact, it is usually measured once per hour. The reason for this is because the minute by minute heart rate values are not *validated*. The process of data validation involves a nurse manually right clicking the observation and selecting "validate" from a drop down menu. All charted values in the database have been validated by a nursing staff. In routine clinical practice for vital signs, the nurse only inspects the patient's hourly observations and only validates the patient's hourly observations. As a result, only these hourly observations constitute the data available in the database. The time at which the data is validated is recorded in the database in the `STORETIME` field. Note that a nurse can validate multiple observations at the same time. The user who validates the data is typically recorded in the `CGID` column - linking this to the `CAREGIVERS` table allows one to inspect the role of the caregiver who validated the data (RN, etc).

Putting this all together, lets consider recording the heart rate of a single patient. The heart rate will be continuously uploaded to the ICU database. Nurse A decides to review the flowsheet of the patient they are assigned at 19:41 (note that the "flowsheet" summarizes all the patient observations and is essentially a front end to the database). Nurse A notes that for the past three hours the heart rate has not been validated (it appears as italic text). The nurse will review the measurements, ensure that they are physiologically reasonable and match their observations of the patient for the past three hours. Then, nurse A selects the past three hours of heart rate measurements (17:00, 18:00 and 19:00) and selects "validate" from a drop down menu. Visually, the text of these measurements changes from italics to bold weight. Technically, the data has been marked as validated and will be archived in the database. The `CHARTTIME` for these three measurements will be 17:00, 18:00 and 19:00. The `STORETIME` for all three measurements will be 19:41. 

### Manual input of data

Not all data in the ICU is recorded automatically by monitors and synchronized with the database. For example the Glasgow Coma Scale, a measurement of neurological disfunction, requires interaction and observation with the patient by a member of the clinical staff. These observations must be manually recorded in the database. Typical workflow for data of this type is to record the observation on paper, and later transcribe a batch of data to the database. Again, the data would appear with a `CHARTTIME` corresponding to the hour of the measurement, and data entered contemporaneously would share the same `STORETIME`.


### Summing up: `CHARTTIME` vs. `STORETIME`

`CHARTTIME` is the time at which a measurement is *charted*. In almost all cases, this is the time which best matches the time of actual measurement. In the case of continuous vital signs, the `CHARTTIME` is usually exactly the time of measurement. `STORETIME` is the time at which the data is recorded in the database: logically it occurs after `CHARTTIME`, often by hours, but usually not more than that. 

