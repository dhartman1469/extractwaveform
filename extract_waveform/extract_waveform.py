import matplotlib.pyplot as plt
import os
import xlwt
from tempfile import TemporaryFile

def subtract_cord(coord1, coord2):
    return [coord1[0]-coord2[0], coord1[1]-coord2[1]]


#ch = html
cdir = os.getcwd()
dir = 'extract_waveform/'
print cdir
html_dir = "HTML"  # dir "HTML"
html_files = next(os.walk(html_dir))[2]
html_paths = [html_dir + '/' + files for files in html_files]
short_html_files = [files for files in html_files]
for idx, path in enumerate(html_paths):
    print(idx)
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1')
    name2 = path + '_' + 'EXCEL' + '.xls' 
    name = 'EXCEL/' + short_html_files[idx] + '_' + 'EXCEL' + '.xls'  #  dir

    
    f=open(path)    
    #f=open('HTML/F273392_20130617_105242.html')
    #f=open('M108690_20130607_145648.html')
    #f=open('M128422_20130612_130100.html')
    ch=f.read()

    dict = {}
    lst =  [line for line in (ch.splitlines(True)) ] # x
    i = 0;
    dict[0] = ['']
    ###
    skip_flag = False
    ###
    begin_path_flag = False
    line_width_flag = False
    for indx, itm in enumerate(lst):
        if "ctx.lineWidth" in itm:
            if "ctx.lineWidth = 1.647640" in itm:
                line_width_flag = True
            else:
                line_width_flag = False
        elif line_width_flag:
            ###
            #print len(lst)
            if "ctx.clip" in itm:
                skip_flag = False
            elif "ctx.beginPath" in itm and "ctx.save" in lst[indx-1]:
                skip_flag = True
            elif skip_flag:
                continue
            ###
            elif "ctx.beginPath" in itm: # if
                begin_path_flag = True
            elif 'ctx.moveTo' in itm and begin_path_flag:
                coord = (itm[12:-3])
                split_coord = coord.split(', ')
                split_coord_float = [float(x) for x in split_coord]
                if split_coord_float != dict[i][-1]: # not repeated
                    i+=1 # go onto next graph
                    dict[i] = []
                    dict[i].append(split_coord_float)
                    begin_path_flag = False
                # if it is repeated then skip    
            elif 'ctx.moveTo' in itm:  # begin_path_flag = false
                coord = (itm[12:-3])
                split_coord = coord.split(', ')
                dict[i].append([float(x) for x in split_coord])  
            elif 'ctx.lineTo' in itm:
                coord = (itm[12:-3])
                split_coord = coord.split(', ')
                dict[i].append([float(x) for x in split_coord])
    imax = i

    order_height = [dict[i][0][1] for i in xrange(1,imax+1)]
    max_value = max(order_height)
    max_index = order_height.index(max_value)
    ## really del dict1 dict 2
    '''del dict[max_index+1]
    del dict[0]
    if 1 in dict.keys(): 
        del dict[1]
    else:
        del dict[2]'''
    ##
    del dict[0]
    del dict[1]
    del dict[2]
    if max_index != 0:
        del dict[max_index+1]
        
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    column_idx = 0
    for i in dict.keys():
        dict_x = [itm[0] for itm in dict[i]]
        for p,e in enumerate(dict_x):
            sheet1.write(p,column_idx,e)
            
        column_idx+=1
        
        dict_y = [itm[1] for itm in dict[i]]
        for p,e in enumerate(dict_y):
            sheet1.write(p,column_idx,e)
            
        column_idx+=2
        ax1.plot(dict_x, dict_y)
    ''' EXCEL '''    
    book.save(name)
    book.save(TemporaryFile())    
    #plt.show()
f.close()





