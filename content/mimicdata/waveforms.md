+++
date = "2015-10-25T13:37:00-04:00"
title = "Waveforms"
linktitle = "Waveforms"
weight = 5
toc = "true"

[menu]
  [menu.main]
    parent = "MIMIC data"

+++

# Waveforms vs. clinical data

This website is primarily dedicated to the MIMIC-III clinical database. It is worth noting that, in conjunction with the clinical database, high resolution waveforms and numerics (second by second derived values from the waveforms) are collected. This latter database is known as the MIMIC-III waveform database.

The MIMIC-III waveform database and the MIMIC-III clinical database are separate entities which are accessed through the same portal, PhysioNet, but through distinct means. This has primarily arisen for two reasons: the very different storage and analysis methods used for high resolution waveforms sampled at consistent frequencies versus heterogenous unevenly sampled clinical data, and the lack of integration of waveforms and clinical data at the source. Implied by the latter point, and now explicitly stated, is that the waveform and clinical database are *separate* databases and special procedures must be taken to match records between the two.

The clinical data can be accessed through PhysioNetWorks as detailed [here](gettingstarted/access).

The waveform data can be accessed through PhysioNetBank, and requires no log-in, [here](http://physionet.org/bank/mimic3wdb).

Detail on how to match records from the clinical database and the waveform database is provided on PhysioNetBank [here](http://physionet.org/bank/mimic3cdb).
