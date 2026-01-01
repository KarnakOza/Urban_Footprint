# Preprocessing

-Radiometric Calibration: Pixel Values that are directly related to radar backscatter, Level 1 product usually suffer from a certain radiometric bias.

RC: enables comparison of SAR images acquired with different sensors, or acquired from the same sensors but at different times, in different modes, or processed by different processors.

-TOPS DEBURST: To remove the gaps in the image, but in more depth TOPSAR IW SLC products, each product consists of one image pper swath per polarization and IW product have 3 swaths.
Each sub-swath image consists of a series of bursts, hwere each burst was processed as a separate SLC image. The individually focused complex burst image, in Azimuth-time order, into a single subswath image, with black-fill demarcation in betweem, similar to the ENVISAT ASAR Wide ScanSAR SLC products.

For IW, a focused burst has a duration of 2.75 sec and a burst overlap of ~50-100 samples.
Images for all bursts in all subswaths of an IW SLC products are re-sampled to a common pixel spacing grid in range and azimuth.
Burst synchronisation is ensured for IW products.
