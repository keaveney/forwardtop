#Script to automate the running of MG5_aMC@NLO
#repeatledy while scanning model parameters.
import subprocess
from subprocess import call


f = open('run-config.txt', 'w')

f.write('import model Monotops_UFO --modelname \n')
f.write('define tt = t t~ \n')
f.write('generate p p > v > t psi psibar  \n')
f.write('output \n')
f.write('launch \n')
f.write('set MFM 50.0 \n')
f.write('set Mphi 1000.0 \n')
f.write('set Mpsi 1000.0 \n')
f.write('0 \n')
f.write('0 \n')

#proc = subprocess.Popen(['./../MadGraph/MG5_aMC_v2_4_2/bin/mg5_aMC run-config.txt', '"to stdout"'], 
 #                       stdout=subprocess.PIPE,
 #                       )

call(["./../MadGraph/MG5_aMC_v2_4_2/bin/mg5_aMC run-config.txt"], shell=True)
