from basissetsetup import getHFCoefficients
from basissetselector import find_optimal_basis_sets


#need to use obabel to get the xyz using obabel because RDKit xyz converter leaves out hydrogens 
def getHFCoefficientsBasedOnBestBasisSets(molFile, name):
	outputJSON = find_optimal_basis_sets(molFile, name, 95, "False")
	basisSet = outputJSON["Best Basis Sets Based on Ground State Precision"][0]
	print(basisSet)
	fileName = name + ".xyz"
	ouptutCoefficients = getHFCoefficients(fileName, basisSet)
	return ouptutCoefficients

print(getHFCoefficientsBasedOnBestBasisSets("proline.pdb", "proline"))	