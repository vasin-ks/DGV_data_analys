
Script name: DGV_data_analysis


Description and tasks: This script is written to work with CNV (deletions, duplications)  from Chromosome Analysis Suite 4.3 (ChAS 4.3)  and 
                      compares the data with Database of Genomic Variants.  


1-We are working with the hg38 version of the genome. So  we download hg38 version of the genome  from Database of Genomic Variants
  You can download any version if you wish. # http://dgv.tcag.ca/dgv/app/downloads   DGV download

2-First you enter how much CNV there is in the your program. We usually have 100-200 CNV per patient. 
  Write out the number from the program: 124

3-Next, you will copy all (124) the data for this CNV Columns from the CHAS program.  4 column from.
  1:Type 2:Chromosome 3:Min 4:Max


 Example

first step

Number of CNV:4

second step: copy 4 cnv =   1:Type 2:Chromosome 3:Min 4:Max

Gain 10 18503049 18509274
Gain 16 47329823 47605913
Gain 18 34589110 34596630
Gain X 130241823  130249134

third step: result

CNV molecular coordinates chr10:(18503049_18509274)×Gain

Full_CNV_coverage 2
['nsv4339713', 'sequence', 'nsv550042', 'gain']
DGV_is_inside_CNV 1
['nsv4560907', 'line1']

CNV molecular coordinates chr16:(47329823_47605913)×Gain

Full_CNV_coverage 1
['nsv4252047', 'deletion']
Covers_the_first_CNV_coordinate 8
['dgv518e214', 'loss', 'esv2758644', 'gain', 'nsv4532515', 'deletion', 'esv3638553', 'gain', 'esv3638554', 'loss', 'esv3638556', 'loss', 'esv3638557', 'gain', 'nsv833217', 'gain']
Covers_the_second_CNV_coordinate 4
['esv34317', 'gain', 'nsv520355', 'gain', 'nsv525976', 'gain', 'esv3638564', 'loss']
DGV_is_inside_CNV 43
['esv3359649', 'insertion', 'esv3638558', 'loss', 'nsv4250494', 'deletion', 'nsv4243623', 'deletion', 'esv3652100', 'complex', 'esv3657310', 'insertion', 'nsv572537', 'loss', 'nsv4250466', 'deletion', 'nsv4245431', 'deletion', 'nsv4512831', 'alu', 'esv3657311', 'insertion', 'nsv1138449', 'deletion', 'nsv4232504', 'deletion', 'nsv4505415', 'alu', 'nsv4508628', 'alu', 'nsv4241480', 'deletion', 'esv3638561', 'gain', 'nsv4252113', 'duplication', 'nsv4236893', 'deletion', 'nsv4512094', 'alu', 'esv3892856', 'loss', 'nsv4241791', 'deletion', 'nsv1059367', 'loss', 'esv2761905', 'loss', 'nsv4513756', 'alu', 'nsv4234903', 'deletion', 'nsv4499246', 'alu', 'nsv4498347', 'alu', 'esv3638563', 'loss', 'nsv4249455', 'duplication', 'nsv4235586', 'deletion', 'nsv4241287', 'deletion', 'nsv4532580', 'deletion', 'nsv4503816', 'alu', 'esv3638565', 'loss', 'nsv4243818', 'deletion', 'nsv974811', 'duplication', 'nsv4233196', 'deletion', 'nsv4506304', 'alu', 'nsv4565238', 'line1', 'nsv4566385', 'line1', 'nsv974812', 'duplication', 'esv3657312', 'insertion']

CNV molecular coordinates chr18:(34589110_34596630)×Gain

Full_CNV_coverage 1
['nsv4336672', 'sequence']
DGV_is_inside_CNV 2
['nsv4254634', 'deletion', 'nsv4556750', 'insertion']

CNV molecular coordinates chrX:(130241823_130249134)×Gain

Full_CNV_coverage 1
['nsv528290', 'gain']
Covers_the_first_CNV_coordinate 3
['esv3577252', 'gain', 'dgv2425e212', 'loss', 'dgv2426e212', 'gain']
DGV_is_inside_CNV 1
['nsv4032843', 'deletion']



4-If there are no matches and CNV is not in the DGV 

the result will be: There are no matches in the DGV database

5-Important. The program is running very slowly.
It took me about 1~2 minute to analyze 174 cnv

6-this script is an addition to determining the uniqueness and frequency of occurrence of CNV.
 WE use the comparison first of all with the cohort of our children and secondly with the base
 Database of Genomic Variants


	Thank you all for your attention. 

	With you was 
	Vasin Kirill Sergeevich, MD., Phd. 
	My contacts:

	drvasinks@gmail.com

	telegram @DrKvasin

	https://www.linkedin.com/in/kirill-vasin-ba654a104/

