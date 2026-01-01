# Preprocessing
---
# Radiometric Calibration:
Pixel Values that are directly related to radar backscatter, Level 1 product usually suffer from a certain radiometric bias.

RC: enables comparison of SAR images acquired with different sensors, or acquired from the same sensors but at different times, in different modes, or processed by different processors.
---
# TOPS DEBURST: 
To remove the gaps in the image, but in more depth TOPSAR IW SLC products, each product consists of one image pper swath per polarization and IW product have 3 swaths.
Each sub-swath image consists of a series of bursts, hwere each burst was processed as a separate SLC image. The individually focused complex burst image, in Azimuth-time order, into a single subswath image, with black-fill demarcation in betweem, similar to the ENVISAT ASAR Wide ScanSAR SLC products.

For IW, a focused burst has a duration of 2.75 sec and a burst overlap of ~50-100 samples.
Images for all bursts in all subswaths of an IW SLC products are re-sampled to a common pixel spacing grid in range and azimuth.
Burst synchronisation is ensured for IW products.

Unlike ASAR WSS which contains large overlap between beams, for S-1 TOPSAR, the imagined ground area of adjacent bursts will only margainally overlap in azimuth just enough to provide contiguous coverage of the ground. This is due to the one natural azimuth look inherent in the data.

For GRD products, the bursts are concatenated and sub-swaths are merged to form one image. Bursts overlap minimally in azimuth and sub-swaths overlap minimally in range. Bursts for all beams have been resampled to a common grid during azimuth post-processing.

In the range direction, for each line in all sub-swaths with the same time tag, marge adjacent sub-swaths. For the overlappin region in range, merging is done midway between subswath.

In the azimuth direction, burst are merged according to their zero Doppler time. Note that black-fill demarcation is not distinctly zero at the end or start of the burst. Due to resamping, the data faded into zero and out. The merge time is determined by the average of the last line of the burst and the first line of the next burst. For each range cell, the merging time is quantised to the nearest output azimuth cell to eliminate any fading to zero data.

---
# Multi-looking: Spatial averaging over multiple range/azimuth resolution cells, 
Pupose for that are Speckle resolution and Creation of squared pixels

How: Choosing appropriate number of looks in range and azimuth where in general you will need
- pixel spacing in azimuth
- pixel spacing in slant range
- look angle at scene centre
Note: MLI is mirrored and upside down in compare with Google Earth Image
---

# Geocoding


