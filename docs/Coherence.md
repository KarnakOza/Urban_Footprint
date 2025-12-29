# Methodology: Urban Footprint Mapping Using Sentinel-1 SAR 

This document completely explains the processes of Generation of interferometric coherence

--- 

1. ***Co-registration of SLC pairs***
   - S-1 Back Geocoding: DEM(SRTM 3Sec)
   - DEM Resampling Method: Bicubic Interpolation
   - Resampling Type: BISNIC 5 Point Interpolation


2. ***Coherence Estimation***
   - Range Coherence window size: 10
   - Coherence Azimuth Window size: 3

3. ***S-1 Tops Deburst***
   - Polarization

4. ***MultiLooking***
   - Source: Coherence_Subswath_Pre_Post
   - GR Square Pixel
  
5. ***GEOCODING***
   - Geometric: Terrain Correction : SAR Simulation Terrain Correction
 
