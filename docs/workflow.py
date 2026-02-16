##Applying Orbit File 
 
parameters = HashMap()
GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
parameters.put('orbitType', 'Sentinel Precise (Auto Download)')
parameters.put('polyDegree', '3')
parameters.put('continueOnFail', 'false')
apply_orbit_file = GPF.createProduct('Apply-Orbit-File', parameters, product)
return imgplot


-#/for GRDH file terrain correction 

parameters = HashMap()
parameters.put('demName', 'SRTM 3Sec')
parameters.put('pixelSpacingInMeter', 10.0)
parameters.put('sourceBands', 'Sigma0_VV')
speckle_filter_tc = GPF.createProduct("Terrain-Correction", parameters,
speckle_filter)
plotBand(speckle_filter_tc, 'Sigma0_VV', 0, 0.1)
