+++
date = "2015-09-08T06:58:18-04:00"
title = "Understanding IOEVENTS"
linktitle = "Understanding IOEVENTS"
weight = 4
toc = "true"

[menu]
  [menu.main]
    parent = "MIMIC data"

+++

# IOEVENTS

The IOEVENTS table is one of the most useful, and most complicated, tables available in the MIMIC-III data. Recall that the MIMIC-III database contains information from two distinct clinical information systems: Philips CareVue and iMDSoft Metavision. These two databases were not guaranteed to store data in a similar fashion, and the IOEVENTS table reflect the merging of two very distinct data archiving techniques. In the descriptions in this document, data will be referred to as being sourced either from "CareVue" or "Metavision" to help differentiate between the different methods in which the data was stored.

# How to use IOEVENTS

IOEVENTS has two types of data: inputs and outputs. Inputs are any fluids which have been administered to the patient: most commonly these are intravenous solutions containing medications. Outputs are fluids which have either been excreted by the patient, such as urine output, or extracted from the patient, for example through a drain.

## Outputs

Outputs are recorded in a reasonably consistent manner in both the CareVue and Metavision data. The time of the output is recorded in the `ENDTIME` column. The `STARTTIME` column is null as there is no start time recorded with outputs. The volume of output is recorded in the `AMOUNT` column, and the unit of measurement is provided in the `AMOUNTUOM` column (usually milliliters, or mL).
It is reasonable to assume that any output recorded is for the previous hour.

## Inputs

Inputs are handled differently by CareVue and Metavision. For CareVue data, only the `ENDTIME` is available. Second, the `RATE` and `AMOUNT` columns are *asynchronous*. Volumes of input (e.g. 50 mL of normal saline) would be stored in one table, and would usually be recorded every hour (though sometimes the period was longer). Conversely, the `RATE` of the drug would be stored separately, and only updated when a change or verification of the rate was made by clinical staff. As a result, the raw data looked something similar to:

CHARTTIME | VOLUME | VOLUMEUOM | CHARTTIME | RATE | RATEUOM
---- | ---- | ---- | ---- | ---- | ----
 | | | 09:00 | 1 | mL/hr
10:00 | 60 | mL | | |
11:00 | 60  | mL | | |
 | | 11:30 | 0.5 | mL/hr |
12:00 | 45 | mL | | |

Here, the volume is recorded only every hour, and no start time is available. However, it's reasonable to assume that the volume measurement corresponds to an hour. Next, we can see that the rate was titrated to 0.5, and for the period between 11:00 to 12:00 there was half an hour of delivery at 1 mL/hr, and half an hour of delivery at 0.5 mL/hr, resulting in a total volume of 45 mL delivered for the past hour.

Summing up, for CareVue data, the rate and volume will be asynchronous, and only the `ENDTIME` will be available.

For Metavision data, there is no concept of a volume in the database: only a `RATE`. Furthermore, all inputs are recorded with a `STARTTIME` and an `ENDTIME`. As a result, the volumes in the database for Metavision patients are *derived* from the rates. Furthermore, exact start and stop times for the drugs are easily deducible.

<!--
TODO: ORDERID description, ORIGINALAMOUNT, etc.
-->

# Details of the merging process

The difficulty in merging the databases arose due primarily to two factors: the lower resolution of information archiving in the CareVue system, and the different definition of an 'order' in the databases.

The aim of this section is to provide all the detail into how these data were merged: this information is not necessary to understand for the purposes of using the database, but will provide insight into the format of the IOEVENTS table. We always welcome suggestions from the community on improving the format and usability of the table.

## Philips CareVue

The CareVue system stored input/output (IO) data across five tables: IOEVENTS, MEDEVENTS, ADDITIVES, SOLUTIONS and DELIVERIES. Each time a new order for a drug was recorded in the database, the ADDITIVES, SOLUTIONS and DELIVERIES tables would be populated with information regarding the order. The data archival format is best described with an example.

Patient A has been recently admitted to the ICU and is to be administered noradrenaline to restore their blood pressure to a value of at least 60 mmHg. The route of administration is intravenous, i.e. the drug is to be pumped into the patient's blood stream directly through a line inserted in a vein. The nurse would prepare a solution of 250 mL sodium chloride (NaCl) to contain the drug. The SOLUTIONS table would consequently contain an entry of 250 mL NaCl for patient A at the time the nurse prepared the solution. The nurse would then mix in the drug into the solution: in this case 8 mg of noreadrenaline is appropriate. The 8 mg of noradrenaline would be recorded in the ADDITIVES table, and an identifier would be recorded which linked the 8 mg of noradrenaline to the 250 mL solution of NaCl. Finally, the nurse would optionally set an initial delivery rate and route: in this case it could be 10 mL/hr intravenously. These would populate the `RATE` and `ROUTE` columns in the DELIVERIES table. Note this data was not consistently recorded.

Now that the solution has been prepared, the nurse can begin administering the drug to the patient. The time is now 18:20. An initial entry of 0 mL is recorded in the IOEVENTS table at 18:00 (this usually occurs, but it has not been verified that this *always* occurs). The nurse begins at a rate of 1 mcg/kg/min. The MEDEVENTS contains an entry at a `CHARTTIME` of 18:20 for a rate of 1 mcg/kg/min. Five minutes later, at 18:25, the nurse notes that the blood pressure is still lower than the desired 60 mmHg and increases the dose. The nurse raises the dose to 2 mcg/kg/min, and MEDEVENTS records the new dose of 2 mcg/kg/min at 18:25. The nurse checks again and notes that the blood pressure has reached the target value of 60 mmHg and ceases titration of the drug. At 19:00, the volume of drug administered to the patient is recorded. If the patient weighed 100 kg, then the amount of drug administered would be equal to:

5 min * 1 mcg/kg/min * 100 kg + 25 min * 2 mcg/kg/min * 100 kg
= 500 mcg + 5000 mcg
= 5500 mcg = 5.5 mg

The amount of solution administered would be equal to:

( 5 min * 1 mcg/kg/min * 100 kg + 25 min * 2 mcg/kg/min * 100 kg ) * 250 mL / 8 mg
= 5.5 mg * 250 mL / 8 mg
= 171.875 mL

Consequently, IOEVENTS would record 171.875 mL at 19:00. If the patient continued at the same rate for this drug, then IOEVENTS would record (60 * 2 * 100 * 250 / 8000) = 375 mL at 20:00. Note that:

 - Unless the rate is updated, no new entry in MEDEVENTS exists
 - IOEVENTS always records a value on an hourly basis, regardless of how long the IO event has been present
 - 375 mL is larger than the original 250 mL bag: somewhere during administration the nurse would need to replace the empty bag with a new solution of the same formulation

Note that the changing of the bag is sometimes, but not always, recorded in the ADDITIVES/SOLUTIONS/DELIVERIES table as a new order.

## Metavision

Metavision records IO data using two tables: RANGESIGNALS and ORDERENTRY. These tables do not appear in MIMIC-III as they have been merged to form the IOEVENTS table. RANGESIGNALS contains recorded data elements which last for a fixed period of time. Furthermore, the RANGESIGNALS table recorded information for each component of the drug separately. For example, for a noradrenaline administration there would be two components: a main order component (noradrenaline) and a solution component (). ???
