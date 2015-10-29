+++
date = "2015-09-01T19:33:17-04:00"
title = "Releases of MIMIC-III"
linktitle = "Releases of MIMIC-III"
weight = 2
toc = "true"

[menu]
  [menu.main]
    parent = "About"

+++

# Release notes

The MIMIC-III database will be periodically updated as more data becomes available, as data linkage and extraction methods improve, and when the community provides feedback regarding the database content.
To ensure transparency in this process, updates to the database will be made in batch, and the version number of the MIMIC-III database will be updated.
This page lists the current version, and all previous versions which have existed,  in sequential, reverse chronological order.
Each version will address a finite set of updates which are tracked using a unique issue number, usually of the form #100, #101, etc.

Note that the changes between MIMIC-II and MIMIC-III are not listed here, due to the large number of differences between the databases. A separate document has been provided for that purpose [here](/mimicdata/whatsnew). The release notes for MIMIC-II versions is available [here](/archive/mimic-releases).

# Current version

The current version of the database v1.1. When referencing this version, we recommend using the full title: MIMIC-III v1.1.

## MIMIC III v1.1

MIMIC III v1.1 was released on September 24th, 2015. It was primarily a bug fix release, and addresses the following issues:

* #116 - `CGID` was incorrect in the DATETIMEEVENTS, CHARTEVENTS, IOEVENTS and NOTEEVENTS tables. It has now been corrected.
* #117 - `VALUENUM` for GCS verbal response measurements has been corrected for Metavision (it was offset by -1).
* #118 - `VALUENUM` for all GCS measurements in CareVue is no longer null, and contains the appropriate value in the scale.
* #120 - `DOD` was incorrectly set to `DOB` - this has been fixed.
* #121 - IOEVENTS contained incorrect units for certain drugs (sometimes the unit was a rate when the actual observation was an amount, e.g. listed as "mcgkgmin" when it should have been "mg").
* #122 - `DBSOURCE` in the TRANSFERS and ICUSTAYEVENTS tables has been corrected - originally it only contained 'metavision' when a patient was in the ICU, so the same patient would be listed as 'carevue' when out of the ICU and 'metavision' when inside the ICU.
* #123 - Precision in the IOEVENTS table has been fixed at 10 decimal places.

# Past versions

This section lists past versions in reverse chronological order.

## MIMIC III v1.0

MIMIC III v1.0 was released on August 25th, 2015. It was a preliminary version and not widely publicized to allow for internal testing. As this was the first release of the database, and the successor of the MIMIC-II database, no changes are listed here. An overview of changes between MIMIC-II and MIMIC-III is provided [here](/mimicdata/whatsnew).

(test comment)
