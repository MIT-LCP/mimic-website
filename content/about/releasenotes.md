+++
date = "2015-09-01T19:33:17-04:00"
title = "Release notes"
linktitle = "Release notes"
weight = 3
toc = "true"

[menu]
  [menu.main]
    parent = "About"

+++

# Release notes

This page will contain changes implemented in sequential updates to the MIMIC database in reverse chronological order. Due to the large number of changes between MIMIC-II and MIMIC-III, we have documented those updates [in a separate section](/archive/mimic-releases).

Issues are tracked using a unique issue number, usually of the form #100, #101, etc.

# MIMIC III v1.1

MIMIC III v1.1 was released on September 24th, 2015. It was primarily a bug fix release, and addresses the following issues:

* #116 - `CGID` was incorrect in the DATETIMEEVENTS, CHARTEVENTS, IOEVENTS and NOTEEVENTS tables. It has now been corrected.
* #117 - `VALUENUM` for GCS verbal response measurements has been corrected for Metavision (it was offset by -1).
* #118 - `VALUENUM` for all GCS measurements in CareVue is no longer null, and contains the appropriate value in the scale.
* #120 - `DOD` was accidentally set to `DOB` - this has been corrected.
* #121 - IOEVENTS contained incorrect units for certain drugs (sometimes the unit was a rate when the actual observation was an amount, e.g. listed as "mcgkgmin" when it should have been "mg").
* #122 - `DBSOURCE` in the TRANSFERS and ICUSTAYEVENTS tables has been corrected - originally it only contained 'metavision' when a patient was in the ICU, so the same patient would be listed as 'carevue' when out of the ICU and 'metavision' when inside the ICU.
* #123 - Precision in the IOEVENTS table has been fixed at 10 decimal places.


# MIMIC III v1.0

MIMIC III v1.0 was released on August 25th, 2015. It was a preliminary version and not widely publicized to allow for internal testing.
