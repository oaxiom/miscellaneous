#PBS -l walltime=336:00:00
#PBS -l nodes=c41:ppn=1
#PBS -j oe
#PBS -q cv3
#PBS -o ${out}.log
#PBS -V 

cd $PBS_O_WORKDIR

pwd

python 1.modi.py $inp

