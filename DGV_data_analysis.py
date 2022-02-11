# Example
# 4
# Gain 10 18503049 18509274
# Gain 16 47329823 47605913
# Gain 18 34589110 34596630
# Gain X 130241823  130249134
print("Enter the total number of CNV/coordinates to be analyzed")
m = int(input())
print("Copy everything", m, "CNV from CHAS like: Gain X	130184930 130192367")
for i in range(0,m):
    inf = open("GRCh38_hg38.txt", "r")
    #We are working with the hg38 version of the genome.
    # You can download any version if you wish.
    # http://dgv.tcag.ca/dgv/app/downloads   DGV download
    l,a,b,c = input().split()
    a = str(a) #chromosome
    b = int(b) #first coordinate
    c = int(c) #second coordinate
    Full_CNV_coverage = 0
    Full_CNV_coverage2 = []
    Covers_the_first_CNV_coordinate = 0
    Covers_the_first_CNV_coordinate2 = []
    Covers_the_second_CNV_coordinate = 0
    Covers_the_second_CNV_coordinate2 = []
    DGV_is_inside_CNV = 0
    DGV_is_inside_CNV2 = []
    for x in range(825428): # Exactly so many lines in GRCh38_hg38.txt. our search algorithm will run through each line
        x = inf.readline()
        x = x.split()
        if a == x[1]:
            f1 = x[2]
            f2 = x[3]
            f1 = int(f1)
            f2 = int(f2)
            if (b >= f1 and b <= f2) and (c >= f1 and c <= f2): # when both coordinates, or cnv, are in the region of\
                # coordinates of a non-pathogenic genomic variation
                Full_CNV_coverage += 1  # Their number
                Full_CNV_coverage2 += x[0], x[5]  # name and type of anomaly
            if (b >= f1 and b <= f2) and (c > f1 and c > f2):
                Covers_the_first_CNV_coordinate += 1
                Covers_the_first_CNV_coordinate2 += x[0], x[5]
            if (b < f1 and b < f2) and (c >= f1 and c <= f2):
                Covers_the_second_CNV_coordinate += 1
                Covers_the_second_CNV_coordinate2 += x[0], x[5]
            if (f1 >= b and f1 <= c) and (f2 >= b and f2 <= c):
                DGV_is_inside_CNV += 1
                DGV_is_inside_CNV2 += x[0], x[5]
    print("CNV molecular coordinates ","chr",a,":(", b,"_", c,")×", l, sep="")
    if Full_CNV_coverage > 0:
        print("Full_CNV_coverage", Full_CNV_coverage)
        print(Full_CNV_coverage2)
    if Covers_the_first_CNV_coordinate > 0:
        print("Covers_the_first_CNV_coordinate",Covers_the_first_CNV_coordinate)
        print(Covers_the_first_CNV_coordinate2)
    if Covers_the_second_CNV_coordinate > 0:
        print("Covers_the_second_CNV_coordinate",Covers_the_second_CNV_coordinate)
        print(Covers_the_second_CNV_coordinate2)
    if DGV_is_inside_CNV > 0:
        print("DGV_is_inside_CNV",DGV_is_inside_CNV)
        print(DGV_is_inside_CNV2)
    if Full_CNV_coverage == 0 and Covers_the_first_CNV_coordinate == 0 and Covers_the_second_CNV_coordinate == 0 and DGV_is_inside_CNV == 0:
        print("There are no matches in the DGV database")
    print()
    print()
    print()