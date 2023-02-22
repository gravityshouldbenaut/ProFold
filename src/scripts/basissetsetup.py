from pyscf import gto, scf, cc, fci



#gets the coefficients for a restricted hartree fock via mean field theory, needs xyz inputs
def getHFCoefficients(mol, basisSet):
    mol = gto.M(
        atom = mol, 
        basis = basisSet, 
        symmetry=False,
    )
    m = scf.RHF(mol)
    m.kernel()
    norb = m.mo_energy.size
    return m.mo_coeff

#need to get the orbital rotations for vqe
# print(getHFCoefficients('H 0 0 0; F 0 0 1.1', 'ccpvdz'))

