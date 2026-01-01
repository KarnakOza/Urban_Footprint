# Methodology: Urban Footprint Mapping Using Sentinel-1 SAR


This document explains the complete processing for the generation of MLI (Multi-lookked Imagery)

---
  1.
   - For Urban FootPrint Mapping combination of 2 products are enough regardless or timeperiod, better to keep it around 10-12 days
   - Orbit Files (Precise Orbit Ephemerides)
---

2. ***SNAP Processing Workflow***

3. ***TOPS SPLIT***
  - Subswath
  - Polarization
  - Burst

4. ***Applying Orbit FIles***
  
5. ***Radiometric Calibration***
  - Polarization
  - Output: sigma0(σ^0) band

6. ***TOPS SAR DEBURST***
    -Polarization

7. ***MULTILOOKING***
   -Source Bands: Sigma0(σ^0)_Subswath_Polarization
   -Enabling GR Pixel to get Square Output
   -With No. of Azimuth and Range Looks: 3, 1
   -Mean GR Square Pixel: 13.24
  /MLI Images are always upside down in SNAP.

8. ***GEOCODING***
   ***SAR SIMULATED TERRAIN CORRECTION***
   - DEM: SRTM 3Sec
   - DEM Resampling Method:Bicubic_interpolation
   - Keeping the GCPs: 2000 with Coarse Registration Window Width and Height to be 64 * 64
   - Tolerance for GCPs to be kept at 0.5
   - Bilinear Interpolation for Image Resampling Method
     
   
