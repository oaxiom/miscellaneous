import glob,os,gzip,sys

for f in glob.glob(sys.argv[1]):
    head = os.path.split(f)[1].replace('.fq.gz','')
    print(head,f)
    
    o = gzip.open('/public/home/jphe/rnaseq/mouse/scRNA/10X/GSE98969/fqs/%s.fq.gz'%head,'rt')
    p1 = gzip.open('%s.p1.fq.gz'%head,'wt')
    i = 0
    for line in o:
        i += 1
        if i == 1:
            l = line.strip().split(' ')[1].split('-')
            
            p1.write(line)
            p1.write('%s%s\n'%(l[-2],l[-1]))
            p1.write('+\n')
            p1.write('%s%s\n'%(l[-4],l[-5]))
        
        if i == 4:
            i=0
    
    o.close()
    p1.close()
